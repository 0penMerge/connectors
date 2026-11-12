"""ServiceNow connector mechanics for the OpenMerge Ticketing category.

Generated pagination policy lives in ``PAGING``; transport, auth, retries and
checkpoint commits stay in OpenMerge core. Requests are always relative to the
declared ``api.base_url``.
"""
from dataclasses import replace
from urllib.parse import parse_qsl, urlsplit

from openmerge_connectors import ConnectorPlugin, HttpRequestSpec, PullPage
from openmerge_connectors.core.capabilities import PullMode, ReadCapability

# mode: cursor | page | offset | next_url | graphql | rpc | single
PAGING = {   '*': {   'mode': 'offset',
             'param': 'sysparm_offset',
             'records': 'result',
             'size': 500,
             'size_param': 'sysparm_limit'}}


class ServiceNowPlugin(ConnectorPlugin):
    """Declarative list reads with provider-specific pagination.

    Core owns parent fan-out (``object.parent``) and calls these page hooks for
    the parent list and for each parent's children.
    """

    def _paging(self, model):
        return PAGING.get(model) or PAGING["*"]

    def build_page_request(self, model, state):
        paging = self._paging(model)
        if paging["mode"] == "graphql":
            return self._graphql_request(model, paging, state.page_cursor)
        if paging["mode"] == "rpc":
            if state.page_cursor is None:
                return HttpRequestSpec("POST", paging["path"], json_body=dict(paging.get("body") or {}))
            return HttpRequestSpec("POST", paging["continue_path"], json_body={"cursor": state.page_cursor})
        request = super().build_page_request(model, replace(state, page_cursor=None))
        params = dict(request.params)
        cursor = state.page_cursor
        if paging["mode"] == "next_url" and cursor:
            parts = urlsplit(cursor)
            if not parts.path.startswith("/"):
                raise ValueError(f"{self.slug}/{model}: continuation URL is not absolute")
            return HttpRequestSpec("GET", parts.path, params=dict(parse_qsl(parts.query)),
                                   headers=request.headers)
        if paging["mode"] in {"page", "offset"}:
            first = paging.get("first", 1 if paging["mode"] == "page" else 0)
            params[paging["param"]] = str(cursor if cursor is not None else first)
            if paging.get("size_param"):
                params[paging["size_param"]] = str(paging["size"])
        elif paging["mode"] == "cursor" and cursor is not None:
            params[paging["param"]] = cursor
        return HttpRequestSpec(request.method, request.path, params=params,
                               headers=request.headers, json_body=request.json_body)

    def _graphql_request(self, model, paging, cursor):
        variables = {"first": paging["size"]}
        if cursor is not None:
            variables["after"] = cursor
        return HttpRequestSpec("POST", paging["path"],
                               json_body={"query": paging["query"], "variables": variables})

    def parse_page_response(self, model, state, body):
        paging = self._paging(model)
        records = body if isinstance(body, list) else self._lookup(body, paging.get("records"))
        if records is None and paging.get("optional_records"):
            records = []
        if not isinstance(records, list) or any(not isinstance(row, dict) for row in records):
            raise TypeError(f"{self.slug}/{model}: provider records path is not an object array")
        # Continuation is decided on the full provider page; the record filter
        # only splits mixed listings (e.g. files and folders) between models.
        next_cursor = self._continuation(paging, state.page_cursor, body, records)
        records = [self._escaped(paging, row) for row in records if self._selected(paging, row)]
        if next_cursor is not None and next_cursor == state.page_cursor:
            raise ValueError("provider pagination did not advance")
        candidate = self._checkpoint_candidate(
            model, state.working_checkpoint or state.source_checkpoint, records)
        full = state.mode in {PullMode.INITIAL, PullMode.RECONCILE} or self.read_strategy(model) in {
            ReadCapability.FULL_SNAPSHOT, ReadCapability.HASH_SNAPSHOT}
        return PullPage(
            records=tuple(dict(row) for row in records),
            next_page_cursor=next_cursor,
            checkpoint_candidate=candidate,
            done=next_cursor is None,
            authoritative_full_inventory=full and self.authoritative_inventory(model, state.mode),
        )

    def _continuation(self, paging, current, body, records):
        mode = paging["mode"]
        if mode == "single":
            return None
        if mode in {"page", "offset"}:
            if len(records) < int(paging["size"]):
                return None
            first = paging.get("first", 1 if mode == "page" else 0)
            position = int(current) if current is not None else int(first)
            return str(position + (1 if mode == "page" else len(records)))
        if isinstance(body, list):
            return None
        has_more = paging.get("has_more")
        if has_more:
            flag = self._lookup(body, has_more)
            if not isinstance(flag, bool):
                return None
            if paging.get("has_more_invert"):
                flag = not flag
            if not flag:
                return None
        value = self._lookup(body, paging.get("next"))
        return None if value in (None, "") else str(value)

    def _lookup(self, body, path):
        """Literal keys win, so OData names such as ``@odata.nextLink`` resolve."""
        if path and isinstance(body, dict) and path in body:
            return body[path]
        return self._deep_get(body, path)

    @staticmethod
    def _escaped(paging, row):
        """Make dotted provider keys (``System.Title``) addressable as ``System__Title``."""
        for key in paging.get("escape_keys") or ():
            value = row.get(key)
            if isinstance(value, dict):
                row = {**row, key: {name.replace(".", "__"): item for name, item in value.items()}}
        return row

    @staticmethod
    def _selected(paging, row):
        """Optional split of mixed listings: ``where`` equality and ``has`` key presence."""
        where = paging.get("where") or {}
        if any(row.get(key) != value for key, value in where.items()):
            return False
        has = paging.get("has")
        return has is None or row.get(has) is not None

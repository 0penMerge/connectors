# Shortcut

Sync Shortcut epics, members, teams, labels and files through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **API key**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Collection | `epics` | hash_snapshot | — |
| User | `members` | hash_snapshot | — |
| Team | `groups` | hash_snapshot | — |
| Tag | `labels` | hash_snapshot | — |
| Attachment | `files` | hash_snapshot | — |

Not synced: Ticket (No complete GET inventory of stories: GET /search/stories is capped at 1000 results and POST /stories/search is not a GET list; stories are otherwise listed per epic/project only); Comment (Story comments are listed per story only); Role (Member roles are an attribute of each member, not listable objects).

## Authentication

Static credentials (`api_key` preset).
- `api_token` — API token

## Notes

- Members, groups, labels and files return bare arrays without pagination; epics use the paginated endpoint (page/page_size up to 250, records under data). Stories are not declared: the search API caps paging at 1000 results and the full query endpoint is a POST, so neither yields a complete inventory. Shortcut has no public OAuth authorization-code flow; users create an API token under Settings > API Tokens. Shortcut documents the token in a Shortcut-Token header (the token query parameter is deprecated), not in Authorization.

Provider API reference: https://developer.shortcut.com/api/rest/v3

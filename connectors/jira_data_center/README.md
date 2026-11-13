# Jira Data Center

Sync self-hosted Jira Data Center issues, projects, users and roles through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `issues` | hash_snapshot | — |
| Collection | `projects` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Role | `roles` | hash_snapshot | — |
| Comment | `issue_comments` | hash_snapshot, per Ticket | — |

Not synced: Attachment (Attachments are only exposed per issue (fields.attachment on GET /rest/api/2/issue/{id}); there is no attachment list endpoint); Team (Groups come from /rest/api/2/groups/picker, which returns name-only matches (no stable id, capped results); Advanced Roadmaps teams need a separate plugin API); Tag (Jira DC has no label list endpoint (only label suggestions per field); labels stay on Ticket.tags); Account (Jira Data Center has no customer account concept); Contact (Jira Data Center has no customer contact concept (JSM DC customers are users)).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `READ`.
- `host` — Jira Data Center host name (e.g. jira.example.com) (asked before the redirect)

## Notes

- Jira Data Center OAuth 2.0 provider (incoming application link, Jira 8.22+). The admin creates an External application link with redirect URL = the OpenMerge callback; endpoints are per instance at https://{host}/rest/oauth2/latest/{authorize,token}. host is the instance origin without scheme and may include a context path (e.g. jira.example.com or example.com/jira). PKCE (S256) is supported but not required. Access tokens live 2 hours; refreshing invalidates the previous access and refresh token pair. The instance must be reachable from OpenMerge over HTTPS.
- REST API v2. Issue search uses GET /rest/api/2/search with startAt/maxResults (max 100 per page by default, jira.search.views.default.max). Users use /rest/api/2/user/search?username=. (wildcard); on Jira 10.x this endpoint caps results at 100 and startAt >= 100 is unreliable (JRASERVER-78520) - on 10.13.3+/11.x prefer /rest/api/2/user/list. Projects and roles return bare arrays without paging. Per-instance OAuth URLs need the connect flow to interpolate {host} before redirecting.

Provider API reference: https://developer.atlassian.com/server/jira/platform/rest/

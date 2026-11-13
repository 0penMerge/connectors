# Wrike

Sync Wrike account tasks, folders and projects, contacts, user groups and account through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `tasks` | hash_snapshot | — |
| Collection | `folders` | hash_snapshot | — |
| User | `contacts` | hash_snapshot | — |
| Team | `groups` | hash_snapshot | — |
| Account | `account` | hash_snapshot | — |

Not synced: Comment (GET /comments returns at most 1000 comments for a created-date window of 7 days or less with no pagination, so a full inventory is impossible; otherwise comments are per task or folder); Attachment (GET /attachments only covers a bounded created-date range (max 31 days) without pagination; otherwise attachments are per task or folder); Role (Wrike exposes no role list; access roles are per-sharing settings); Tag (Wrike has no tag object (folders are used as tags)); Contact (Wrike contacts are internal users and are mapped to User).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `Default wsReadOnly amReadOnlyGroup`.
- `host` — Wrike API host (returned by the token endpoint)

## Notes

- Wrike OAuth 2.0 (v4 authorize endpoint). Access tokens last one hour; each refresh returns a new refresh token and invalidates the old one. The token response carries 'host' (e.g. www.wrike.com or app-eu.wrike.com): store it as connection_config.host, since API calls must go to https://<host>/api/v4 while refresh stays on login.wrike.com.
- Responses wrap records as {kind, data}. Task queries page with pageSize (max 1000) and nextPageToken, and optional fields must be repeated on every page (they live in list_path). The folder tree, contacts, groups and account endpoints return everything in one response; cursor paging stops when nextPageToken is absent. Task date filters take JSON InstantRange objects, not a plain timestamp, so reads are full hashed snapshots.

Provider API reference: https://developers.wrike.com/api/v4/

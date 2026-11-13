# Basecamp

Sync Basecamp to-dos, projects, people and to-do comments through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `todos` | hash_snapshot | — |
| Comment | `comments` | hash_snapshot | — |
| Collection | `projects` | hash_snapshot | — |
| User | `people` | hash_snapshot | — |

Not synced: Attachment (Basecamp uploads live in Docs & Files vaults and inline rich-text attachments, not as a to-do attachment list); Team (Basecamp has no team object; project membership is per project (GET /projects/{id}/people.json)); Role (Basecamp exposes only admin/owner/client flags on people, no role list); Tag (Basecamp has no tags); Account (Basecamp has no customer account object); Contact (Client users are people records and are mapped to User).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `default`.
- After connecting, the account picks `account_id` from the provider's list.

## Notes

- 37signals Launchpad OAuth 2. Launchpad expects type=web_server on the authorize and code-exchange requests and type=refresh (with refresh_token) on refresh. Access tokens last two weeks; refresh tokens are long-lived. account_id comes from GET https://launchpad.37signals.com/authorization.json (accounts[].id with product bc3).
- Basecamp 4 (bc3) API. Every request must send a User-Agent naming the app and a contact URL or email, or it gets 400. Collections use geared pagination (15, 30, 50, then 100 per page) advertised in the Link header; page pagination walks ?page=N and stops on a page shorter than 15, which may cost one extra empty request. Recordings endpoints default to status=active, so archived and trashed items are treated as absent. No updated-since filter exists, so reads are hashed snapshots.

Provider API reference: https://github.com/basecamp/bc3-api

# Intercom

Sync Intercom conversations, contacts, companies, admins, teams and tags through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `conversations` | hash_snapshot | — |
| Contact | `contacts` | hash_snapshot | create, update |
| Account | `companies` | hash_snapshot | — |
| User | `admins` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |
| Tag | `tags` | hash_snapshot | — |

Not synced: Comment (Conversation parts are only returned inside a single conversation (GET /conversations/{id})); Attachment (Attachments live inside conversation parts; no workspace-wide list); Role (No role list endpoint in the Intercom REST API); Collection (Intercom has no ticket container; Help Center collections hold articles, not tickets).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `default`.

## Notes

- Authorization-code flow; the token endpoint takes code, client_id and client_secret in the body and returns a non-expiring access token (no refresh token). EU and AU workspaces authorize at app.eu.intercom.com / app.au.intercom.com.
- Send Intercom-Version (2.11 or later) to pin the API version; otherwise the app's default version applies. US region host only: EU/AU workspaces use api.eu.intercom.io / api.au.intercom.io. Conversations and contacts use cursor pagination (pages.next.starting_after); companies use page/per_page (max 60, at most 10,000 companies, and only companies with at least one contact are listed). Timestamps are Unix integers, so created/updated datetimes stay in remote_data. Intercom's separate Tickets object is only reachable through POST /tickets/search and is not synced; conversations are the Ticket source.

Provider API reference: https://developers.intercom.com/docs/references/rest-api/api.intercom.io

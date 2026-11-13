# Gorgias

Sync Gorgias tickets, messages, customers, users, teams and tags through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `tickets` | hash_snapshot | update |
| Comment | `messages` | hash_snapshot | — |
| Contact | `customers` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |
| Tag | `tags` | hash_snapshot | — |

Not synced: Attachment (Attachments are embedded in messages; no workspace-wide list endpoint); Account (Gorgias has no company/organization object); Role (User roles are an attribute on users; no role list endpoint); Collection (Views are saved filters, not ticket containers; no Collection equivalent).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `openid offline tickets:read customers:read users:read tags:read`.
- `subdomain` — Gorgias subdomain (the part before .gorgias.com) (asked before the redirect)

## Notes

- Per-tenant OAuth on {subdomain}.gorgias.com: the subdomain must be collected before redirecting (the token response does not return it). Token requests use HTTP Basic client_id:client_secret. Access tokens last 24 hours; refresh tokens (offline scope) do not expire and rotation is undocumented. state and nonce are recommended authorize parameters; PKCE is not supported.
- Lists return {data:[...], meta:{next_cursor, prev_cursor}} with cursor/limit (max 100). No updated-since filter exists on list endpoints, so every model is a full hash snapshot. GET /tickets includes trashed tickets by default (trashed=true). Ticket messages are listed account-wide via GET /messages. Message 'public' (false = internal note) and sender ids (user or customer, depending on from_agent) stay in remote_data because they cannot be mapped without inversion/branching.

Provider API reference: https://developers.gorgias.com/reference/introduction

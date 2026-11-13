# Slack

Sync Slack conversations, users and user groups through the OpenMerge chat model.

Category: **Chat** (`chat@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Conversation | `conversations` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Group | `usergroups` | hash_snapshot | — |
| Message | `messages` | hash_snapshot, per Conversation | — |

Not synced: Member (Members are only listable per channel (conversations.members requires channel)).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `channels:read groups:read im:read mpim:read users:read usergroups:read channels:history groups:history im:history mpim:history`.

## Notes

- Slack OAuth v2 with bot-token scopes (comma-separated scope parameter). Bot tokens do not expire unless token rotation is enabled on the Slack app; if rotation is enabled, refresh tokens rotate on every refresh.
- Slack Web API methods accept GET with query arguments. conversations.list and users.list use cursor paging (cursor / response_metadata.next_cursor, empty string at the end). Slack returns HTTP 200 with ok=false on errors; timestamps are epoch numbers, so created/updated are left in remote_data. Rate limits are per method tier and signalled with HTTP 429 + Retry-After.

Provider API reference: https://docs.slack.dev/reference/methods

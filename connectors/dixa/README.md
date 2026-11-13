# Dixa

Sync Dixa agents, teams, end users and tags through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **API key**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| User | `agents` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |
| Contact | `endusers` | hash_snapshot | — |
| Tag | `tags` | hash_snapshot | — |

Not synced: Ticket (No workspace-wide GET list of conversations: GET /v1/search/conversations requires a text query, POST search needs a filter body, and the bulk export API is on a different host (exports.dixa.io)); Comment (Messages and internal notes are only listable per conversation (GET /v1/conversations/{conversationId}/messages|notes)); Attachment (Attachments only appear inside per-conversation messages); Collection (Queues (GET /v1/queues) are routing queues rather than ticket collections; not mapped); Role (Agent roles are plain strings on the agent; there is no role list endpoint); Account (Dixa has no organization/company object).

## Authentication

Static credentials (`api_key` preset).
- `api_token` — API token

## Notes

- Rate limit is 10 requests/second per token with bursts of 4. Paginated lists return data[] plus meta.next, a path-relative URL carrying an opaque pageKey; teams and tags return data[] without pagination. Conversations have no plain list endpoint: GET /v1/search/conversations requires a free-text query and the full conversation export lives on a separate host (https://exports.dixa.io/v1/conversation_export), so tickets are not inventoried by this connector. Create an API token in Dixa under Settings > Integrations > API Tokens (Dixa API version v1). The token is sent in the Authorization header as 'Authorization: Bearer <api_token>' (the OpenAPI security scheme is an apiKey in the Authorization header).

Provider API reference: https://docs.dixa.io/openapi/dixa-api/v1/

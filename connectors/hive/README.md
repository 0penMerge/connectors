# Hive

Sync Hive workspace actions, projects, users, labels and teams through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **API key**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `actions` | hash_snapshot | — |
| Collection | `projects` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Tag | `labels` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |

Not synced: Comment (Comments are only listable per action (GET /actions/{actionId}/comments)); Attachment (Attachments are only listable per action (GET /actions/{actionId}/attachments)); Role (Hive exposes no role list endpoint); Account (Hive has no customer account object); Contact (External users are workspace guests, not ticket contacts).

## Authentication

Static credentials (`api_key` preset).
- `workspace_id` — Workspace ID

## Notes

- Hive REST API v2. Every list is workspace-scoped and returns a connection object {edges:[{cursor,node}], pageInfo:{endCursor,hasNextPage}}; records are the edges, so mapped fields read from node.*. Pages request first=200 (the maximum) and follow pageInfo.endCursor via 'after'. There is no updated-since filter, so reads are hashed snapshots. Node schemas are untyped in the v2 spec; field names follow the documented Hive object model (_id, title, deadline, checkedDate, createdBy, ...). Hive API keys are generated under Profile > API info (which also shows the workspace id). The v2 API accepts either an 'api_key' header or 'Authorization: Bearer <token>'; this connector sends the key as a Bearer token. If a key is rejected as Bearer, the runtime must send it in the api_key header instead.

Provider API reference: https://developers.hive.com/reference

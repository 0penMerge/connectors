# SpotDraft

Sync SpotDraft contracts (as tickets), counterparties, users and roles through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **API key**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `contracts` | hash_snapshot | — |
| Account | `counter_parties` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Role | `roles` | hash_snapshot | — |

Not synced: Comment (Contract comments are only listable per contract (GET /api/v2.1/public/contracts/{contract_id}/comments/)); Attachment (Contract documents/attachments are only reachable per contract); Contact (Counterparty contacts are nested inside each counterparty record; there is no workspace-wide contact list); Collection (Contract types/templates are definitions rather than ticket containers; not mapped); Team (No team endpoint in the public API); Tag (No tag list endpoint in the public API).

## Authentication

Static credentials (`api_key` preset).
- `region_host` — Regional API host
- `client_id` — Client ID
- `client_secret` — Client secret

## Notes

- Public v2.1 list routes page with 1-based page and limit (default 10) and return {page, limit, total_results, results}. The rate limit is 10 requests/second per workspace. Keep calls on the workspace's region host. Generate an API credential in SpotDraft under Settings > Developer settings. Server-to-server calls send two headers: 'client-id: <Client ID>' and 'client-secret: <Client Secret>' (optionally 'user-email' to act as a workspace member). SpotDraft documents no OAuth authorization-code flow for third parties; the public routes also accept 'Authorization: Bearer <OAuth JWT>' for workspace-user tokens issued by SpotDraft.

Provider API reference: https://api.spotdraft.com/api/docs

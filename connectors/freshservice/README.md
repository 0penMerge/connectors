# Freshservice

Sync Freshservice tickets, requesters, agents, departments, agent groups and roles through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **HTTP Basic**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `tickets` | hash_snapshot | update |
| Contact | `requesters` | hash_snapshot | — |
| User | `agents` | hash_snapshot | — |
| Account | `departments` | hash_snapshot | — |
| Team | `groups` | hash_snapshot | — |
| Role | `roles` | hash_snapshot | — |
| Comment | `ticket_conversations` | hash_snapshot, per Ticket | — |

Not synced: Attachment (Attachments are embedded in tickets/conversations; no workspace-wide list endpoint); Tag (No tag list endpoint; tags are a ticket attribute returned only with include=tags); Collection (Workspaces/projects are not a clean ticket container with a mappable workspace-wide list in the v2 ticket API).

## Authentication

Static credentials (`basic` preset).
- `subdomain` — Freshservice subdomain (the part before .freshservice.com)
- `api_key` — API key

## Notes

- Lists are wrapped ({tickets:[...]}, {requesters:[...]}, ...) and paged with page/per_page (max 100). GET /tickets only returns tickets created in the last 30 days unless updated_since is supplied, so the list path pins updated_since to the epoch. Ticket lists can only be ordered by created_at, so tickets use a full hash snapshot rather than a timestamp delta. Tags and other embeds need include=... (2 extra credits each) and are not requested. Ticket status/priority are integers and stay in remote_data. Agent groups default to the primary workspace on multi-workspace accounts. Requesters and agents carry first_name/last_name only (no full-name field), so the unified name is left to remote_data. Authenticates with an agent's API key over HTTP Basic auth: Authorization: Basic base64('<api_key>:X'). The worker sends 'Authorization: Basic <token>', so the stored token must be the Base64 of '<api_key>:X'. Freshservice also gained Freshworks-org OAuth (scopes such as freshservice.tickets.view) in 2024, but it is tied to the customer's *.myfreshworks.com org host and Freshworks app registration; API key remains the documented default for server-to-server access.

Provider API reference: https://api.freshservice.com/

# Freshdesk

Sync Freshdesk tickets, contacts, agents, companies, groups and roles through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **HTTP Basic**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `tickets` | timestamp_delta | create, update |
| Contact | `contacts` | hash_snapshot | — |
| User | `agents` | hash_snapshot | — |
| Account | `companies` | hash_snapshot | — |
| Team | `groups` | hash_snapshot | — |
| Role | `roles` | hash_snapshot | — |
| Comment | `ticket_conversations` | hash_snapshot, per Ticket | — |

Not synced: Attachment (Attachments are embedded in tickets and conversations; no workspace-wide list endpoint); Tag (Freshdesk v2 exposes no tag list endpoint; tags exist only as ticket/contact attributes); Collection (Freshdesk has no project/list container for tickets).

## Authentication

Static credentials (`basic` preset).
- `subdomain` — Freshdesk subdomain (the part before .freshdesk.com)
- `api_key` — API key

## Notes

- Lists return bare JSON arrays paged with page/per_page (max 100). GET /tickets only returns tickets created in the last 30 days unless updated_since is given, so the snapshot path pins updated_since to the epoch and orders by updated_at ascending; incremental reads replace updated_since with the checkpoint. Freshdesk caps ticket listing at 300 pages (30,000 tickets) per query, so initial/reconcile inventories of larger accounts are truncated. include=description costs extra API credits. Ticket status and priority are integers (status 2 Open/3 Pending/4 Resolved/5 Closed; priority 1-4) and stay in remote_data because the unified fields are strings. Ticket listing stops at 300 pages (30,000 tickets), so a full inventory cannot prove absence: tickets sync by updated_since without absence-based deletion. Freshdesk v2 has no third-party authorization-code OAuth flow; it authenticates with an agent's API key over HTTP Basic auth: Authorization: Basic base64('<api_key>:X') (any password, conventionally X). The worker sends 'Authorization: Basic <token>', so the stored token must be the Base64 of '<api_key>:X', not the raw key. Data visibility follows the key owner's agent permissions.

Provider API reference: https://developers.freshdesk.com/api/

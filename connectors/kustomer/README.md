# Kustomer

Sync Kustomer conversations, customers, companies, messages, users and teams through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **API key**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `conversations` | hash_snapshot | — |
| Contact | `customers` | hash_snapshot | — |
| Account | `companies` | hash_snapshot | — |
| Comment | `messages` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |

Not synced: Tag (Kustomer exposes no workspace-wide conversation tag list endpoint in the public API (only /v3/kb/tags for knowledge-base articles); conversation tags are stored as tag ids on the conversation); Attachment (Attachments are only listable per conversation (GET /v1/conversations/{id}/attachments) or fetched by id; there is no workspace-wide list); Collection (Kustomer has no project/list concept exposed through a list endpoint); Role (Roles are plain strings on users; there is no role list endpoint).

## Authentication

Static credentials (`api_key` preset).
- `orgname` — Organization name (the <orgname> in <orgname>.kustomerapp.com)

## Notes

- JSON:API style responses: records are in data[] with fields under attributes and references under relationships.<name>.data.id. Lists paginate with page/pageSize and return a path-relative links.next URL (null on the last page). PATCH /v1/conversations/{id} documents Content-Type application/json-patch+json while accepting a merge object; PUT /v1/conversations/{id} with application/json is the plain alternative. Kustomer API keys are created in Settings > Security > API Keys and sent as 'Authorization: Bearer <API key>'. The key needs the read roles org.permission.conversation.read, org.permission.customer.read, org.permission.company.read, org.permission.message.read, org.permission.user.read and org.permission.team.read (or their legacy org.user.* equivalents); writes need org.permission.conversation.update.

Provider API reference: https://developer.kustomer.com/api/core-resources

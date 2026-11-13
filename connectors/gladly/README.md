# Gladly

Sync Gladly agents, teams, inboxes and topics through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **HTTP Basic**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| User | `agents` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |
| Collection | `inboxes` | hash_snapshot | — |
| Tag | `topics` | hash_snapshot | — |

Not synced: Ticket (Conversations (GET /api/v1/customers/{customerId}/conversations) and tasks (GET /api/v1/customers/{customerId}/tasks) are only listable per customer; there is no workspace-wide list endpoint (bulk data only via asynchronous export jobs)); Contact (GET /api/v1/customer-profiles is a lookup that requires an email, phone or externalCustomerId filter; there is no workspace-wide customer list); Comment (Conversation items, notes and task comments are only listable under a single conversation or task); Attachment (Attachments are only reachable per conversation item); Account (Gladly has no account/company object); Role (No role list endpoint is exposed).

## Authentication

Static credentials (`basic` preset).
- `organization` — Organization (the <organization> in <organization>.gladly.com)
- `agent_email` — API user email
- `api_token` — API token

## Notes

- Agent, team, inbox and topic list endpoints return a bare JSON array with no pagination. Conversations and tasks are only listable per customer (GET /api/v1/customers/{customerId}/conversations|tasks) and customers can only be looked up by email/phone/externalCustomerId, so they are not inventoried here; bulk conversation data is available through the asynchronous Export API (/api/v1/export/jobs). Gladly uses token-based HTTP Basic auth: user name = the email of a Gladly user with the API User permission, password = that user's API token (Settings > API Tokens). Send 'Authorization: Basic base64(<agent_email>:<api_token>)'; the stored credential must be the base64 of that pair because the worker prefixes it with the 'Basic' scheme. Sandbox orgs live at https://<organization>.gladly.qa.

Provider API reference: https://developer.gladly.com/rest/

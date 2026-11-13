# Re:amaze

Sync Re:amaze conversations, contacts, staff and channels through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **HTTP Basic**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `conversations` | hash_snapshot | — |
| Contact | `contacts` | hash_snapshot | — |
| User | `staff` | hash_snapshot | — |
| Collection | `channels` | hash_snapshot | — |

Not synced: Comment (GET /api/v1/messages lists messages brand-wide, but the documented message payload carries no stable message id (origin_id is only set for some origins), so records cannot be keyed reliably); Tag (There is no tag list endpoint (tags only appear as tag_list strings on conversations and in the tags report); tag names are mapped onto Ticket.tags instead); Attachment (Attachments are only embedded in message payloads, with no list endpoint or ids); Team (Re:amaze exposes no team endpoint); Role (The staff role is a permissions hash; Re:amaze states the Role resource is not supported by the API); Account (Re:amaze has no account/company object in the API).

## Authentication

Static credentials (`basic` preset).
- `brand` — Brand (the <brand> in <brand>.reamaze.io)
- `login_email` — Login email
- `api_token` — API token

## Notes

- Re:amaze requires either an 'Accept: application/json' header or a .json suffix on the resource URL; the declared paths use the .json suffix. Lists return a fixed page of 30 records with page_size/page_count/total_count and are paged with ?page=N (1-based). Conversations are identified by slug, staff and contacts by email (the documented list payloads carry no numeric id). Conversation status is an integer code (0 Open, 1 Responded, 2 Done, 3 Spam, 4 Archived, 5 On Hold, 6 Auto-Done, ...) and stays in remote_data. Rate limits are per API token (HTTP 429). All Re:amaze API authentication is HTTP Basic with '<login-email>:<api-token>' (token from Settings > Developer > API Token). Send 'Authorization: Basic base64(<login_email>:<api_token>)'; the stored credential must be that base64 value because the worker prefixes it with the 'Basic' scheme. Requests are brand-scoped by host.

Provider API reference: https://www.reamaze.com/api

# Help Scout

Sync Help Scout conversations, customers, organizations, users, teams, tags and mailboxes through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `conversations` | timestamp_delta | — |
| Contact | `customers` | hash_snapshot | — |
| Account | `organizations` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |
| Tag | `tags` | hash_snapshot | — |
| Collection | `mailboxes` | hash_snapshot | — |
| Comment | `conversation_threads` | hash_snapshot, per Ticket | — |

Not synced: Attachment (Attachments hang off individual threads; no workspace-wide list); Role (Roles are a user attribute (role string); there is no role list endpoint).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `default`.

## Notes

- Authorization-code flow (Mailbox API 2.0). Access tokens last 2 days; each refresh returns a new refresh token that must replace the stored one.
- HAL responses: records under _embedded.<collection>, continuation in _links.next.href (absent on the last page). Conversations page at 25, everything else at 50. Conversations need status=all (default is active only) and read incrementally with modifiedSince + sortField=modifiedAt asc; the record carries userUpdatedAt (<= modifiedAt), which is used as the checkpoint, so overlap re-reads are possible but nothing is skipped. Customers use the cursor-based v3 list Help Scout recommends. Customers and users have firstName/lastName only, so the unified name is left to remote_data.

Provider API reference: https://developer.helpscout.com/mailbox-api/

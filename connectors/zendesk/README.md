# Zendesk

Sync Zendesk Support tickets, end users, agents, organizations, groups, tags and custom roles through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `tickets` | hash_snapshot | update |
| Contact | `end_users` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Account | `organizations` | hash_snapshot | — |
| Team | `groups` | hash_snapshot | — |
| Tag | `tags` | hash_snapshot | — |
| Role | `custom_roles` | hash_snapshot | — |
| Comment | `ticket_comments` | hash_snapshot, per Ticket | — |

Not synced: Attachment (Attachments are embedded in ticket comments and have no workspace-wide list endpoint); Collection (Zendesk Support has no project/list container exposed through a workspace-wide endpoint that maps cleanly to Collection).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `read`.
- `subdomain` — Zendesk subdomain (the part before .zendesk.com) (asked before the redirect)

## Notes

- Per-tenant OAuth: authorization and token URLs live on the customer's {subdomain}.zendesk.com host, so the subdomain must be collected before redirecting (the token response does not return it). Zendesk issues expiring access tokens with single-use refresh tokens (each refresh returns a new refresh token and invalidates the old pair). Resource-scoped variants (tickets:read, users:read, organizations:read) exist if narrower grants are wanted.
- Tickets come from the cursor-based incremental export (/api/v2/incremental/tickets/cursor) starting at start_time=0 because GET /api/v2/tickets omits archived tickets (closed > 120 days), which would look like deletions in a full inventory. The incremental export needs an admin-role token and is limited to 10 requests/minute (30 with the High Volume add-on); deleted tickets stay in the stream with status 'deleted'. Other lists use cursor pagination (page[size]/page[after], meta.has_more). Zendesk has no single agents-only list that survives a single role filter, so User lists every user (agents, admins and end users) and Contact lists end users only; end users therefore appear in both. Custom roles require the Enterprise plan.

Provider API reference: https://developer.zendesk.com/api-reference/ticketing/introduction/

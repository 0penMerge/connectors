# Zoho Desk

Sync Zoho Desk tickets, contacts, accounts, agents, departments, teams and roles through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `tickets` | hash_snapshot | update |
| Contact | `contacts` | hash_snapshot | — |
| Account | `accounts` | hash_snapshot | — |
| User | `agents` | hash_snapshot | — |
| Collection | `departments` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |
| Role | `roles` | hash_snapshot | — |
| Comment | `ticket_comments` | hash_snapshot, per Ticket | — |

Not synced: Attachment (Ticket attachments are only listable per ticket (GET /api/v1/tickets/{ticket_id}/attachments)); Tag (Ticket tags are listed per ticket or via /api/v1/tags/search, which requires a departmentId).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `Desk.tickets.READ Desk.contacts.READ Desk.accounts.READ Desk.basic.READ`.
- After connecting, the account picks `org_id` from the provider's list.

## Notes

- Zoho Accounts OAuth (server-based client from api-console.zoho.com). access_type=offline returns a non-rotating refresh token. The authorization URL above is the US data center; EU/IN/AU/JP/CA/SA/CN accounts use the matching accounts.zoho.<tld> host, which this spec format cannot express (the Zoho CRM bundle's endpoint_regions pattern should be copied when promoted).
- Every endpoint except /organizations needs the orgId header, rendered from the org_id connection value (GET /api/v1/organizations lists the ids). Lists page with from (zero-based index) + limit (tickets/contacts/accounts max 100; agents/departments/teams max 200; roles max 500) and wrap rows in data (teams in teams). An empty page returns HTTP 204. US data center host desk.zoho.com; other regions use desk.zoho.eu/.in/.com.au/.jp/.sa/.ae/.sg/zohocloud.ca/.com.cn. Calls cost API credits per edition.

Provider API reference: https://desk.zoho.com/DeskAPIDocument

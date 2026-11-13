# ServiceNow

Sync ServiceNow incidents, journal comments, attachments, users, groups, roles and companies through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `incident` | hash_snapshot | create, update |
| Comment | `sys_journal_field` | hash_snapshot | — |
| Attachment | `sys_attachment` | hash_snapshot | — |
| User | `sys_user` | hash_snapshot | — |
| Team | `sys_user_group` | hash_snapshot | — |
| Role | `sys_user_role` | hash_snapshot | — |
| Account | `core_company` | hash_snapshot | — |

Not synced: Contact (Incident callers are sys_user references (already in User); dedicated customer contacts live in customer_contact, which only exists with the Customer Service Management plugin, so a portable list endpoint is not guaranteed); Collection (Incidents have no project/list container in the core Table API); Tag (Tags (label/label_entry) are per-user by default and not a reliable workspace-wide inventory).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `useraccount`.
- `instance` — ServiceNow instance (the part before .service-now.com) (asked before the redirect)

## Notes

- Per-instance OAuth: an admin registers an 'OAuth API endpoint for external clients' in System OAuth > Application Registry with redirect URL = the OpenMerge callback. Authorize at https://{instance}.service-now.com/oauth_auth.do and exchange at /oauth_token.do (client_id/client_secret in the body). instance is the subdomain (e.g. dev12345). Refresh tokens do not rotate (default lifespan 100 days, access token 30 minutes, set per registry entry). The authorizing user needs itil (incidents) plus read access to sys_journal_field and sys_attachment.
- Table API (/api/now/table/{table}) with sysparm_offset/sysparm_limit paging; records are in result. sysparm_exclude_reference_link=true makes reference fields plain sys_id strings and sysparm_display_value=false returns raw values (state/priority are choice codes such as '1'..'8', booleans are 'true'/'false' strings, unset fields are empty strings, datetimes are UTC 'YYYY-MM-DD HH:MM:SS'). Ordered by sys_created_on for stable offsets. Per-instance OAuth URLs need the connect flow to interpolate {instance} before redirecting. Instance rate limits are admin-configured (X-RateLimit-* headers only when a rate-limit rule applies).

Provider API reference: https://developer.servicenow.com/dev.do#!/reference/api/latest/rest/c_TableAPI

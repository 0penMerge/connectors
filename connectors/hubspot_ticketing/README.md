# HubSpot Ticketing

Sync HubSpot Service Hub tickets, owners, companies and contacts through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `tickets` | hash_snapshot | create, update |
| User | `owners` | hash_snapshot | — |
| Account | `companies` | hash_snapshot | — |
| Contact | `contacts` | hash_snapshot | — |
| Collection | `ticket_pipelines` | hash_snapshot | — |

Not synced: Comment (Ticket conversation (notes/emails/threads) are engagements linked through associations or the Conversations inbox API; there is no comment list with a scalar ticket id); Attachment (Ticket files are Files API objects linked through note engagements; no per-ticket attachment list); Team (Teams are only exposed inside owner records (teams[]) or via the settings users API with a different scope; no stable list in the CRM API); Role (Roles are only available through the account settings users/roles API (settings.users.read), not the ticket scope set); Tag (HubSpot tickets have no tag object; Merge lists Tag without fields for HubSpot).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `oauth tickets crm.objects.owners.read crm.objects.companies.read crm.objects.contacts.read`.

## Notes

- HubSpot public app OAuth (same app conventions as the HubSpot CRM connector). Refresh tokens do not rotate; access tokens live 30 minutes.
- CRM v3 object lists page with limit + after; the next cursor is paging.next.after. Requested properties are listed explicitly (unrequested ones are omitted). The list endpoint has no updated-since filter (only the POST search API does), so models are hash snapshots. hs_pipeline_stage and hs_pipeline are internal ids, not labels.

Provider API reference: https://developers.hubspot.com/docs/guides/api/crm/objects/tickets

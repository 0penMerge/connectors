# Salesforce Service Cloud

Sync Salesforce Service Cloud cases, case comments, accounts, contacts, users, queues/groups and roles through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `Case` | hash_snapshot | — |
| Comment | `CaseComment` | hash_snapshot | — |
| Account | `Account` | hash_snapshot | — |
| Contact | `Contact` | hash_snapshot | — |
| User | `User` | hash_snapshot | — |
| Team | `Group` | hash_snapshot | — |
| Role | `UserRole` | hash_snapshot | — |

Not synced: Attachment (Case files are ContentDocumentLink rows, which SOQL only allows with a LinkedEntityId/ContentDocumentId filter (per case); the legacy Attachment object is superseded by Files); Collection (Cases have no project/list container; queues are modeled as Team); Tag (Salesforce Topics/Tags are not enabled on Case by default and have no portable workspace-wide case tag list).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `api refresh_token`.

## Notes

- Same connected app / External Client App conventions as the Salesforce CRM connector: S256 PKCE required by External Client Apps; sandboxes authorize at test.salesforce.com. instance_url comes from the token response. Refresh-token rotation depends on the app policy; OpenMerge treats it as rotating.
- All lists are SOQL queries on /services/data/v67.0/query; pages follow nextRecordsUrl (path-relative on the instance host) until done=true. Rows carry an 'attributes' object. SOQL cannot take an updated-since query parameter, so every model is a hash snapshot. Service Cloud (Case) requires a Service Cloud or Sales Cloud edition with API access. Sforce-Limit-Info reports api-usage=used/limit for a 24h rolling window (no reset header).

Provider API reference: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_query.htm

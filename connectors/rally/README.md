# Rally

Sync Rally (Broadcom Agile Central) work items, projects, users, tags, discussions and attachments through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `artifacts` | hash_snapshot | — |
| Collection | `projects` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Tag | `tags` | hash_snapshot | — |
| Comment | `conversationposts` | hash_snapshot | — |
| Attachment | `attachments` | hash_snapshot | — |

Not synced: Account (Rally has no customer account object); Contact (Rally has no external contact object); Team (Rally teams are projects (mapped as Collection); there is no separate team object); Role (Rally permissions (ProjectPermission/WorkspacePermission) are per-object grants, not a role catalog).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `alm`.

## Notes

- Create an OAuth client in Rally under Settings > Access > OAuth Clients (client id, client secret, callback URL). Authorization-code grant: GET /login/oauth2/auth with response_type=code, client_id, redirect_uri, scope=alm, state; then POST form-encoded code, redirect_uri, grant_type=authorization_code, client_id, client_secret to /login/oauth2/token. Rally expects the resulting access token in a 'ZSESSIONID: <token>' request header (the same header used for Rally API keys), not 'Authorization: Bearer'.
- The OAuth access token is sent in the ZSESSIONID header (api.auth_headers). Queries return {QueryResult: {Results: [...], TotalResultCount, StartIndex, PageSize}} and page with 1-based start plus pagesize (max 2000). Queries run against the authorizing user's default workspace unless a workspace=/workspace/<ObjectID> parameter is added. References are objects with _ref, _refObjectUUID and _refObjectName; records are keyed by ObjectUUID. Explicit fetch lists are used instead of fetch=true per Broadcom WSAPI best practice.

Provider API reference: https://rally1.rallydev.com/slm/doc/webservice/

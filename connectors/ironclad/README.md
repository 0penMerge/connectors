# Ironclad

Sync Ironclad contract workflows (as tickets), users and groups through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `workflows` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Team | `groups` | hash_snapshot | — |

Not synced: Comment (Workflow comments are only listable per workflow (GET /public/api/v1/workflows/{id}/comments)); Attachment (Workflow documents are only reachable per workflow (GET /public/api/v1/workflows/{id}/documents)); Collection (Workflow templates/schemas are definitions, not ticket containers; not mapped); Account (Counterparties are workflow attributes, not a listable object); Contact (No contact object in the public API); Role (Workflow roles are per-workflow assignments; there is no role catalog endpoint); Tag (No tag object in the public API).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `public.workflows.readWorkflows scim.users.readUsers scim.groups.readGroups`.

## Notes

- Register an OAuth client app in Ironclad (Company Settings > API). Authorization-code grant: GET https://ironcladapp.com/oauth/authorize (response_type=code, client_id, redirect_uri, space-separated scope, state) and POST https://ironcladapp.com/oauth/token with client_id/client_secret. Access tokens last 6 hours; each refresh returns a new refresh token (rotation). EU (eu1.ironcladapp.com) and demo (demo.ironcladapp.com) need their own app registration and host.
- Workflows live under /public/api/v1 and users/groups under the SCIM base /scim/v2 on the same host. GET /public/api/v1/workflows defaults to status=active, so the list path requests all four statuses; it pages with zero-based page and pageSize (max 100) and returns {page, pageSize, count, list}. SCIM lists page with 1-based startIndex and count (max 1000) and return Resources. The workflow lastUpdated query parameter filters by update time but the endpoint documents no ascending sort, so workflows are read as a full snapshot.

Provider API reference: https://developer.ironcladapp.com/reference/list-all-workflows

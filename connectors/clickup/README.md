# ClickUp

Sync ClickUp Workspace tasks, Spaces and custom roles through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `tasks` | hash_snapshot | — |
| Collection | `spaces` | hash_snapshot | — |
| Role | `custom_roles` | hash_snapshot | — |

Not synced: User (No Workspace member list endpoint: members are only nested inside GET /api/v2/team (authorized Workspaces), and GET /team/{team_id}/user/{user_id} is per-user (Enterprise)); Team (User groups are listed at GET /api/v2/group?team_id=..., which needs team_id as a query parameter outside the Workspace-scoped base URL); Comment (Comments are only listable per task, list or view (GET /task/{task_id}/comment)); Attachment (Attachments are only exposed nested in a task record; there is no list endpoint); Tag (Tags are only listable per Space (GET /space/{space_id}/tag)); Account (ClickUp has no customer account object); Contact (ClickUp has no external contact object).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `default`.
- After connecting, the account picks `team_id` from the provider's list.

## Notes

- ClickUp OAuth (authorization code). The token endpoint takes client_id, client_secret and code. team_id is the Workspace id returned by GET /api/v2/team after authorization.
- API v2. All reads are Workspace-scoped (/team/{team_id}/...). OAuth tokens are sent as 'Authorization: Bearer'. Filtered team tasks return 100 tasks per zero-based page; ClickUp timestamps are Unix-millisecond strings, so date fields stay in remote_data. Custom roles require a plan with custom roles (Enterprise).

Provider API reference: https://developer.clickup.com/reference

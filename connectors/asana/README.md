# Asana

Sync Asana workspace projects, users, teams and tags through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| User | `users` | hash_snapshot | — |
| Collection | `projects` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |
| Tag | `tags` | hash_snapshot | — |

Not synced: Ticket (Asana has no paginated workspace-wide task list: GET /tasks needs a project, tag, section or assignee+workspace, and GET /workspaces/{gid}/tasks/search is premium-only, capped at 100 results with no next_page, so a full inventory cannot be guaranteed); Comment (Comments are task stories, only listable per task (GET /tasks/{task_gid}/stories)); Attachment (Attachments are only listable per parent object (GET /attachments?parent={task_gid})); Role (No workspace-path role list reachable from the workspace-scoped base URL); Account (Asana has no customer account object); Contact (Asana has no external contact object).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `users:read projects:read teams:read tags:read`.
- After connecting, the account picks `workspace_gid` from the provider's list.

## Notes

- Asana OAuth with granular scopes (the app must be configured for specific scopes; apps on full permissions use scope 'default'). Access tokens last one hour; refresh tokens are long-lived and not rotated. workspace_gid is chosen after authorization from GET /api/1.0/workspaces.
- All lists are workspace-scoped (/workspaces/{workspace_gid}/...). Pagination requires limit (1-100) and follows next_page.offset. Compact records only carry gid/name/resource_type, so every list passes opt_fields. GET /workspaces/{gid}/teams only works for organization workspaces. GET /workspaces/{gid}/users takes no limit and returns at most 2000 users (alphabetical), following next_page.offset if present.

Provider API reference: https://developers.asana.com/reference/rest-api-reference

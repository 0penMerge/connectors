# Bitbucket

Sync Bitbucket Cloud workspace projects and members through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Collection | `projects` | hash_snapshot | — |
| User | `workspace_members` | hash_snapshot | — |

Not synced: Ticket (Issues are listed per repository only (/repositories/{workspace}/{repo_slug}/issues); there is no workspace-wide issue list); Comment (Issue comments are listed per issue only); Attachment (Issue attachments are listed per issue only); Role (Workspace permissions are membership attributes (owner/collaborator/member), not listable role objects); Team (Bitbucket Cloud 2.0 has no workspace group list endpoint (groups were 1.0-only)).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `default`.
- After connecting, the account picks `workspace` from the provider's list.

## Notes

- Bitbucket Cloud OAuth consumer, authorization code grant. Access tokens expire after 1 hour; refresh tokens rotate on use. workspace is the workspace slug chosen by the user after authorization.
- OAuth calls must go to api.bitbucket.org with a Bearer token. Collections use page/pagelen with records under values. Issues are only listed per repository (/repositories/{workspace}/{repo_slug}/issues), so Ticket is not declared.

Provider API reference: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/

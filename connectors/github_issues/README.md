# GitHub Issues

Sync GitHub issues, repositories and teams visible to the authorizing user through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `issues` | timestamp_delta | — |
| Collection | `repositories` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |

Not synced: User (No workspace-wide user list without an organization context (/users enumerates all of GitHub; members are per org at /orgs/{org}/members)); Comment (Issue comments are listed per repository (/repos/{owner}/{repo}/issues/comments) or per issue only); Tag (Labels are listed per repository only (/repos/{owner}/{repo}/labels)); Role (Repository/organization roles are listed per organization only); Attachment (GitHub has no attachment API for issues).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `default`.

## Notes

- GitHub App user access tokens via the web application flow. With token expiration enabled, access tokens last 8 hours and each refresh returns a new refresh token while invalidating the previous one (6-month refresh lifetime). The token endpoint must be called with Accept: application/json.
- Send Accept: application/vnd.github+json and X-GitHub-Api-Version: 2022-11-28. Pagination uses page/per_page (max 100); bodies are bare arrays. GET /issues treats pull requests as issues; rows carrying a pull_request key are pull requests. Issue writes need owner/repo/number paths, so none are declared. Organization member and repository-label lists need an org/repo context and are not declared.

Provider API reference: https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28

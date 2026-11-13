# GitLab

Sync GitLab group issues, projects, subgroups, labels and members through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `issues` | timestamp_delta | — |
| Collection | `projects` | hash_snapshot | — |
| Team | `groups` | hash_snapshot | — |
| Tag | `labels` | hash_snapshot | — |
| User | `members` | hash_snapshot | — |

Not synced: Comment (Notes are listed per issue only (/projects/:id/issues/:iid/notes)); Role (GitLab access levels are fixed integers on memberships; custom member roles are an Ultimate-only, group-admin feature); Attachment (Issue uploads are embedded in markdown and have no list endpoint).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `read_api`.
- After connecting, the account picks `group_id` from the provider's list.

## Notes

- GitLab.com OAuth 2.0 authorization code flow (PKCE recommended). Access tokens last 2 hours; each refresh revokes the previous access and refresh tokens. group_id is the top-level group's numeric id or URL-encoded full path, chosen by the user after authorization.
- All reads are bounded by one group (including subgroups), because the root GET /issues?scope=all can be rejected on GitLab.com. Offset pagination with page/per_page (max 100); bodies are bare arrays. Issue writes need project id + iid paths, so none are declared. Member emails are only returned to group owners for enterprise users.

Provider API reference: https://docs.gitlab.com/api/issues/

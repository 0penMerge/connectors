# Jira

Sync Jira Cloud issues, projects, users and roles through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `issues` | hash_snapshot | — |
| Collection | `projects` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Role | `roles` | hash_snapshot | — |
| Comment | `issue_comments` | hash_snapshot, per Ticket | — |

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `read:jira-work read:jira-user offline_access`.
- After connecting, the account picks `cloud_id` from the provider's list.

## Notes

- Atlassian 3LO. cloud_id is the site id returned by https://api.atlassian.com/oauth/token/accessible-resources after authorization.
- Issues use enhanced JQL search with nextPageToken; project and user lists use startAt/maxResults offsets.

Provider API reference: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

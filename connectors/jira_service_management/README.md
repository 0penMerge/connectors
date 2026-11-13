# Jira Service Management

Sync Jira Service Management requests, service projects, customer organizations, users and roles through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `requests` | hash_snapshot | — |
| Collection | `service_projects` | hash_snapshot | — |
| Account | `organizations` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Role | `roles` | hash_snapshot | — |
| Comment | `issue_comments` | hash_snapshot, per Ticket | — |

Not synced: Contact (Customers are only listable per service desk (GET /rest/servicedeskapi/servicedesk/{id}/customer, experimental) or per organization (/organization/{id}/user); there is no workspace-wide customer list. Customer accounts still appear in User via /rest/api/3/users/search (accountType=customer)); Attachment (Attachments are only listable per request/issue (/rest/servicedeskapi/request/{issueIdOrKey}/attachment)); Team (Atlassian Teams live in the separate organization-level Teams API (api.atlassian.com/gateway/api/public/teams) keyed by org id, not reachable with the site cloud_id); Tag (GET /rest/api/3/label returns a page of bare strings, not objects with ids; labels stay on Ticket.tags).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `read:jira-work read:jira-user read:servicedesk-request manage:servicedesk-customer offline_access`.
- After connecting, the account picks `cloud_id` from the provider's list.

## Notes

- Atlassian 3LO (same app type as Jira Cloud), with the Jira Service Management API scopes enabled on the app. cloud_id is the site id returned by https://api.atlassian.com/oauth/token/accessible-resources after authorization.
- Requests are the Jira issues of service projects, read through enhanced JQL search filtered with projectType = service_desk (nextPageToken paging) so agents see every request, not only the ones they participate in (GET /rest/servicedeskapi/request is scoped to the calling user's involvement). Service Management list endpoints (organization) page with start/limit and isLastPage; platform lists page with startAt/maxResults. Requires a Jira Service Management agent licence for the connecting user.

Provider API reference: https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/

# Zoho BugTracker

Sync Zoho BugTracker projects and portal users through the OpenMerge ticketing model (bugs are project-scoped; see omitted).

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Collection | `projects` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |

Not synced: Ticket (Bugs are only listable per project (GET /restapi/portal/{portal}/projects/{project}/bugs/); there is no portal-wide bug list, so a fan-out over Collection is required, which this spec format cannot express); Comment (Bug comments are per bug (/projects/{project}/bugs/{bug}/comments/) or per batch of at most 25 bug ids within one project); Attachment (Attachments are per bug (/projects/{project}/bugs/{bug}/attachments/)); Tag (Tags are only exposed through the V3 API (/api/v3/portal/{portal}/tags), not the legacy REST base used here); Role (Roles appear only as role/role_name attributes on users; no list endpoint in the BugTracker REST API); Team (No team/user-group list endpoint in the BugTracker REST API); Account (Client companies are a Zoho Projects feature, not exposed by BugTracker); Contact (BugTracker has no customer contact object).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `ZohoBugTracker.portals.READ ZohoBugTracker.projects.READ ZohoBugTracker.users.READ`.
- After connecting, the account picks `portal_id` from the provider's list.

## Notes

- Zoho Accounts OAuth with ZohoBugTracker.* scopes; tokens minted with ZohoBugTracker scopes only work against bugtracker.zoho.com (not projectsapi.zoho.com) and vice versa. US data center shown; other regions use accounts.zoho.<tld> / bugtracker.zoho.<tld>. portal_id is not part of the token response: resolve it from GET /restapi/portals/ after authorization.
- Legacy REST API (Zoho marks it 'will be deprecated soon' in favor of V3). GET lists take index (1-based position of the first record) and range (default 100, max 200). Rate limit: 100 calls per API per 2 minutes, then a 30-minute lock.

Provider API reference: https://www.zoho.com/projects/help/rest-api/zohoprojectsapi.html

# Linear

Sync Linear issues, projects, teams, users, labels, comments, attachments and customers through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `issues` | hash_snapshot | — |
| Collection | `projects` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Tag | `issue_labels` | hash_snapshot | — |
| Comment | `comments` | hash_snapshot | — |
| Attachment | `attachments` | hash_snapshot | — |
| Account | `customers` | hash_snapshot | — |

Not synced: Role (Linear has no role objects; admin/guest status is a boolean on User); Contact (Customer contacts are not exposed as a workspace-wide list).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `read`.

## Notes

- Linear OAuth 2.0 authorization code flow; scopes are comma-separated in the authorize request. Access tokens expire after 24 hours; refresh tokens rotate on every refresh (30-day lifetime) and a replayed refresh within 30 minutes returns the same replacement credentials. PKCE (S256) is supported.
- GraphQL only: every read is a POST to /graphql with Relay connections (first/after, pageInfo.hasNextPage/endCursor). Archived records are excluded by default. Writes are GraphQL mutations, so none are declared. Customers require the Customer Requests feature; the list is empty otherwise.

Provider API reference: https://linear.app/developers/graphql

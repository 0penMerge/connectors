# Teamwork.com

Sync Teamwork.com tasks, projects, people, teams, tags and task comments through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `tasks` | timestamp_delta | update |
| Collection | `projects` | hash_snapshot | — |
| User | `people` | hash_snapshot | — |
| Tag | `tags` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |
| Comment | `comments` | hash_snapshot | — |

Not synced: Attachment (Task files are only listed per project or task (v3 has no account-wide task attachment list filtered to tasks)); Role (Teamwork job roles are not ticket access roles; no matching role list); Account (Client companies are not modelled here; Merge does not map Teamwork accounts); Contact (Teamwork has no external contact object in Projects).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `default`.

## Notes

- Teamwork App Login Flow. The code exchange is a JSON POST with code, client_id, client_secret and redirect_uri. The token response's installation.apiEndPoint (e.g. https://acme.teamwork.com/) gives the site: store its host (acme.teamwork.com, acme.eu.teamwork.com or a custom domain) as connection_config.site_host.
- Projects API v3 (/projects/api/v3/...) for tasks, projects, people, tags and comments; teams only exist in v1 (/teams.json). Lists use page/pageSize (default 50, kept at 50 so a short page reliably means the last page). Tasks support updatedAfter (date-time) with orderBy=updatedat&orderMode=asc for incremental reads.

Provider API reference: https://apidocs.teamwork.com/docs/teamwork/v3

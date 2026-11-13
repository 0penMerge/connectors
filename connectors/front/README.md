# Front

Sync Front conversations, contacts, accounts, teammates, teams, tags and inboxes through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `conversations` | hash_snapshot | — |
| Contact | `contacts` | hash_snapshot | — |
| Account | `accounts` | hash_snapshot | — |
| User | `teammates` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |
| Tag | `tags` | hash_snapshot | — |
| Collection | `inboxes` | hash_snapshot | — |
| Comment | `conversation_messages` | hash_snapshot, per Ticket | — |

Not synced: Attachment (Attachments are embedded in messages; no workspace-wide list); Role (Front exposes no workspace-wide role list endpoint).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `default`.

## Notes

- Token exchange and refresh authenticate with HTTP Basic client_id:client_secret. Access tokens last 60 minutes; refresh tokens last 6 months and the same refresh token is returned on refresh until its final 24 hours, when a new one (new 6-month window) is issued, so always store the refresh_token from each response.
- Lists return {_results:[...], _pagination:{next}} where next is a full api2.frontapp.com URL (null on the last page); limit max 100. Conversation timestamps are Unix epoch numbers, so created/updated datetimes stay in remote_data. Conversation contact, assignee and tags are nested objects/link URLs, not scalar ids, so they stay in remote_data. Teams are shown as Workspaces in the Front UI but keep the /teams endpoint.

Provider API reference: https://dev.frontapp.com/reference/introduction

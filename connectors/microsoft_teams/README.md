# Microsoft Teams

Sync Microsoft Teams chats, teams and directory users through the OpenMerge chat model.

Category: **Chat** (`chat@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Conversation | `chats` | hash_snapshot | — |
| Group | `teams` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Message | `chat_messages` | hash_snapshot, per Conversation | — |
| Member | `chat_members` | hash_snapshot, per Conversation | — |

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `offline_access Chat.ReadBasic Team.ReadBasic.All User.ReadBasic.All`.

## Notes

- Microsoft identity platform v2.0, work or school accounts only (Teams APIs do not support personal accounts). Each refresh returns a new refresh token; superseded tokens stay valid until their own expiry.
- Microsoft Graph v1.0; list paths carry the /v1.0 prefix so @odata.nextLink continuation paths resolve against the host-only base_url. GET /teams populates only id, displayName, description and visibility. Conversation covers the signed-in user's chats; channels are per team and not included.

Provider API reference: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0

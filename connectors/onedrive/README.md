# OneDrive

Sync OneDrive drives plus the Microsoft 365 directory users and groups through the OpenMerge file storage model.

Category: **File Storage** (`filestorage@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Drive | `drives` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |
| Group | `groups` | hash_snapshot | — |
| File | `driveItems_files` | hash_snapshot | — |
| Folder | `driveItems_folders` | hash_snapshot | — |

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `offline_access Files.Read User.ReadBasic.All GroupMember.Read.All`.

## Notes

- Microsoft identity platform v2.0 (common tenant). Each refresh returns a new refresh token; superseded tokens stay valid until their own expiry. User and Group listing need a work or school account; GroupMember.Read.All needs tenant admin consent.
- Microsoft Graph v1.0; list paths carry the /v1.0 prefix so @odata.nextLink continuation paths resolve against the host-only base_url. File and Folder share one /me/drive/root/delta enumeration and are split by the file/folder facet; the final page carries @odata.deltaLink instead of @odata.nextLink, which ends the walk. Deleted items (deleted facet without file/folder) are dropped and disappear through full-inventory reconciliation.

Provider API reference: https://learn.microsoft.com/en-us/graph/api/resources/onedrive?view=graph-rest-1.0

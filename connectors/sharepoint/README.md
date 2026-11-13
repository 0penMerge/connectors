# SharePoint

Sync SharePoint tenant users and groups through the OpenMerge file storage model.

Category: **File Storage** (`filestorage@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| User | `users` | hash_snapshot | — |
| Group | `groups` | hash_snapshot | — |

Not synced: Drive (Document libraries are only listable per site (/v1.0/sites/{site-id}/drives); there is no tenant-wide drive list, and a site_id connection field cannot be used because list paths are not interpolated and next_url paging needs a host-only base_url); File (Files are only listable per drive (/drives/{id}/root/delta), mixed with folders, under per-site drives); Folder (Folders are only listable per drive and come mixed with files from delta; no tenant-wide folder endpoint).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `offline_access Sites.Read.All User.ReadBasic.All GroupMember.Read.All`.

## Notes

- Microsoft identity platform v2.0 (work or school accounts). Each refresh returns a new refresh token; superseded tokens stay valid until their own expiry. GroupMember.Read.All needs tenant admin consent.
- Microsoft Graph v1.0; list paths carry the /v1.0 prefix so @odata.nextLink continuation paths resolve against the host-only base_url.

Provider API reference: https://learn.microsoft.com/en-us/graph/api/resources/sharepoint?view=graph-rest-1.0

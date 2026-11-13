# Box

Sync Box enterprise users and groups through the OpenMerge file storage model.

Category: **File Storage** (`filestorage@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| User | `users` | hash_snapshot | — |
| Group | `groups` | hash_snapshot | — |

Not synced: File (Box has no workspace-wide file list: /2.0/folders/{id}/items lists one folder level only and /2.0/search requires a query term; full inventory needs recursive traversal); Folder (Same as File: folders are only listable per parent folder (/2.0/folders/{id}/items), with no recursive or enterprise-wide GET endpoint); Drive (Box has no drive concept; all content lives under the root folder 0).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `root_readonly manage_managed_users manage_groups`.

## Notes

- Box OAuth 2.0 user authentication. Scopes must also be enabled on the Box app in the Developer Console; the scope parameter can only narrow them. Refresh tokens are single-use: every refresh returns a new refresh token and invalidates the old one.
- Box API 2.0. Users use marker pagination (usemarker=true, next_marker) because offset is capped at 10000; groups use offset/limit (max 1000). Enterprise listings require an admin or co-admin connection.

Provider API reference: https://developer.box.com/reference/

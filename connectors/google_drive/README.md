# Google Drive

Sync Google Drive files, folders and shared drives through the OpenMerge file storage model.

Category: **File Storage** (`filestorage@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| File | `files` | hash_snapshot | — |
| Folder | `folders` | hash_snapshot | — |
| Drive | `drives` | hash_snapshot | — |

Not synced: User (Drive API has no user directory list; workspace users require the Admin SDK Directory API (admin-only, separate product)); Group (Groups are only listable through the Admin SDK Directory API, not the Drive API).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `https://www.googleapis.com/auth/drive.metadata.readonly`.

## Notes

- Google OAuth 2.0 web-server flow. access_type=offline with prompt=consent guarantees a refresh token; refresh tokens do not rotate. Drive metadata scopes are restricted and require Google app verification for external users.
- Drive API v3. files.list is split into File and Folder with q=mimeType filters across all drives (corpora=allDrives, includeItemsFromAllDrives, supportsAllDrives); trashed items are excluded. Pagination uses pageToken/nextPageToken. Drive int64 values (size) are JSON strings, so size stays in remote_data. Users and groups need the Admin SDK and are not declared.

Provider API reference: https://developers.google.com/workspace/drive/api/reference/rest/v3

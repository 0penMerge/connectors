# Dropbox

Sync Dropbox files, folders, team members and groups through the OpenMerge file storage model.

Category: **File Storage** (`filestorage@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| File | `files` | hash_snapshot | — |
| Folder | `folders` | hash_snapshot | — |
| User | `team_members` | hash_snapshot | — |
| Group | `team_groups` | hash_snapshot | — |

Not synced: Drive (Dropbox has no drive concept; team spaces are namespaces (POST /2/team/namespaces/list) that do not match Merge's Drive).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `account_info.read files.metadata.read`.

## Notes

- Dropbox OAuth 2 code flow; token_access_type=offline returns a long-lived refresh token that does not rotate.
- Dropbox API v2 list calls are POST RPCs: rpc pagination posts the initial body to list_path and continues with {cursor} on the matching /continue endpoint while has_more is true. File and Folder share one recursive list_folder walk split by .tag. Dropbox entries carry parent paths, not parent ids, so folder references stay in remote_data. User and Group use the team endpoints and require a team-linked app (members.read, groups.read).

Provider API reference: https://www.dropbox.com/developers/documentation/http/documentation

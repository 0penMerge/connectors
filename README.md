# OpenMerge connectors

Connector source managed through OpenMerge. Changes are made on review branches and
merged through pull requests; pull a branch in OpenMerge (Integrations → Connector
development) to edit it.

## Layout

```
connectors/<name>/plugin.py        # provider mechanics (pagination, request shaping)
connectors/<name>/connector.yaml   # identity, auth, API transport, setup UI
connectors/<name>/schema.yaml      # models, read strategy, mappings to the unified catalog
catalog/default/<category>/*.json  # unified (Merge-compatible) category models
```

## Unified categories

The catalogs follow Merge's published unified common models
(`docs.merge.dev/openapi/{ticketing,file-storage,chat}.json`): Merge bookkeeping
fields (`id`, `created_at`, `modified_at`, `field_mappings`, `remote_was_deleted`) are
owned by OpenMerge, and `remote_data`, `remote_data_path` and `remote_fields` carry
provider passthrough exactly as in the CRM catalog. Merge's open enums (ticket status,
priority, access level, conversation type, …) are strings whose normalized values are
listed in each field description.

### Ticketing (`ticketing@1`)

Models: Account, Attachment, Collection, Comment, Contact, Role, Tag, Team, Ticket, User

| Connector | Slug | Auth | Models | Writes | Not synced |
|---|---|---|---|---|---|
| Aha! | `aha` | API key | Ticket, Collection, User | Ticket.update | Comment, Attachment, Tag, Role, Team |
| Asana | `asana` | OAuth 2.0 | User, Collection, Team, Tag | — | Ticket, Comment, Attachment, Role, Account, Contact |
| Azure DevOps | `azure_devops` | OAuth 2.0 | Ticket, Collection, Team | — | User, Comment, Attachment, Tag, Role |
| Basecamp | `basecamp` | OAuth 2.0 | Ticket, Comment, Collection, User | — | Attachment, Team, Role, Tag, Account, Contact |
| Bitbucket | `bitbucket` | OAuth 2.0 | Collection, User | — | Ticket, Comment, Attachment, Role, Team |
| ClickUp | `clickup` | OAuth 2.0 | Ticket, Collection, Role | — | User, Team, Comment, Attachment, Tag, Account, Contact |
| Dixa | `dixa` | API key | User, Team, Contact, Tag | — | Ticket, Comment, Attachment, Collection, Role, Account |
| Freshdesk | `freshdesk` | API key | Ticket, Contact, User, Account, Team, Role | Ticket.create, Ticket.update | Comment, Attachment, Tag, Collection |
| Freshservice | `freshservice` | API key | Ticket, Contact, User, Account, Team, Role | Ticket.update | Comment, Attachment, Tag, Collection |
| Front | `front` | OAuth 2.0 | Ticket, Contact, Account, User, Team, Tag, Collection | — | Comment, Attachment, Role |
| GitHub Issues | `github_issues` | OAuth 2.0 | Ticket, Collection, Team | — | User, Comment, Tag, Role, Attachment |
| GitLab | `gitlab` | OAuth 2.0 | Ticket, Collection, Team, Tag, User | — | Comment, Role, Attachment |
| Gladly | `gladly` | API key | User, Team, Collection, Tag | — | Ticket, Contact, Comment, Attachment, Account, Role |
| Gorgias | `gorgias` | OAuth 2.0 | Ticket, Comment, Contact, User, Team, Tag | Ticket.update | Attachment, Account, Role, Collection |
| Help Scout | `help_scout` | OAuth 2.0 | Ticket, Contact, Account, User, Team, Tag, Collection | — | Comment, Attachment, Role |
| Hive | `hive` | API key | Ticket, Collection, User, Tag, Team | — | Comment, Attachment, Role, Account, Contact |
| HubSpot Ticketing | `hubspot_ticketing` | OAuth 2.0 | Ticket, User, Account, Contact, Collection | Ticket.create, Ticket.update | Comment, Attachment, Team, Role, Tag |
| Intercom | `intercom` | OAuth 2.0 | Ticket, Contact, Account, User, Team, Tag | Contact.create, Contact.update | Comment, Attachment, Role, Collection |
| Ironclad | `ironclad` | OAuth 2.0 | Ticket, User, Team | — | Comment, Attachment, Collection, Account, Contact, Role, Tag |
| Jira | `jira` | OAuth 2.0 | Ticket, Collection, User, Role | — | — |
| Jira Data Center | `jira_data_center` | OAuth 2.0 | Ticket, Collection, User, Role | — | Comment, Attachment, Team, Tag, Account, Contact |
| Jira Service Management | `jira_service_management` | OAuth 2.0 | Ticket, Collection, Account, User, Role | — | Contact, Comment, Attachment, Team, Tag |
| Kustomer | `kustomer` | API key | Ticket, Contact, Account, Comment, User, Team | Ticket.update | Tag, Attachment, Collection, Role |
| Linear | `linear` | OAuth 2.0 | Ticket, Collection, Team, User, Tag, Comment, Attachment, Account | — | Role, Contact |
| Rally | `rally` | OAuth 2.0 | Ticket, Collection, User, Tag, Comment, Attachment | — | Account, Contact, Team, Role |
| Re:amaze | `reamaze` | API key | Ticket, Contact, User, Collection | — | Comment, Tag, Attachment, Team, Role, Account |
| Salesforce Service Cloud | `salesforce_service_cloud` | OAuth 2.0 | Ticket, Comment, Account, Contact, User, Team, Role | — | Attachment, Collection, Tag |
| ServiceNow | `servicenow` | OAuth 2.0 | Ticket, Comment, Attachment, User, Team, Role, Account | Ticket.create, Ticket.update | Contact, Collection, Tag |
| Shortcut | `shortcut` | API key | Collection, User, Team, Tag, Attachment | — | Ticket, Comment, Role |
| SpotDraft | `spotdraft` | API key | Ticket, Account, User, Role | — | Comment, Attachment, Contact, Collection, Team, Tag |
| Teamwork.com | `teamwork` | OAuth 2.0 | Ticket, Collection, User, Tag, Team, Comment | Ticket.update | Attachment, Role, Account, Contact |
| Trello | `trello` | API key | Ticket, Collection, Tag, User | — | Comment, Attachment, Team, Role, Account, Contact |
| Wrike | `wrike` | OAuth 2.0 | Ticket, Collection, User, Team, Account | — | Comment, Attachment, Role, Tag, Contact |
| Zendesk | `zendesk` | OAuth 2.0 | Ticket, Contact, User, Account, Team, Tag, Role | Ticket.update | Comment, Attachment, Collection |
| Zoho BugTracker | `zoho_bugtracker` | OAuth 2.0 | Collection, User | — | Ticket, Comment, Attachment, Tag, Role, Team, Account, Contact |
| Zoho Desk | `zoho_desk` | OAuth 2.0 | Ticket, Contact, Account, User, Collection, Team, Role | Ticket.update | Comment, Attachment, Tag |

### File Storage (`filestorage@1`)

Models: Drive, File, Folder, Group, User

| Connector | Slug | Auth | Models | Writes | Not synced |
|---|---|---|---|---|---|
| Box | `box` | OAuth 2.0 | User, Group | — | File, Folder, Drive |
| Dropbox | `dropbox` | OAuth 2.0 | File, Folder, User, Group | — | Drive |
| Google Drive | `google_drive` | OAuth 2.0 | File, Folder, Drive | — | User, Group |
| OneDrive | `onedrive` | OAuth 2.0 | Drive, User, Group, File, Folder | — | — |
| SharePoint | `sharepoint` | OAuth 2.0 | User, Group | — | Drive, File, Folder |

### Chat (`chat@1`)

Models: Conversation, Group, Member, Message, User

| Connector | Slug | Auth | Models | Writes | Not synced |
|---|---|---|---|---|---|
| Microsoft Teams | `microsoft_teams` | OAuth 2.0 | Conversation, Group, User | — | Message, Member |
| Slack | `slack` | OAuth 2.0 | Conversation, User, Group | — | Message, Member |

## Conventions

- Reads default to `hash_snapshot` (authoritative full inventory, deletion by absence);
  providers with an ISO-8601 *updated since* filter use `timestamp_delta` with a daily
  full-inventory reconciliation.
- Array references (`assignees`, `collections`, `members`, …) stay in `remote_data` until
  the lens gains an array form of `ref`; scalar references are resolved through identity maps.
- Models that a provider only exposes under a parent object (e.g. comments per issue)
  are listed under *Not synced*, as are models the provider does not offer; nested ones need parent fan-out support in the runtime.
- API-key connectors use the `api_key` driver; `api.notes` documents how each key is sent.

Validate a bundle locally from the OpenMerge mono-repo:

```
openmerge connector lint connectors/<name> --catalog catalog/default
```

# OpenMerge connectors

Declarative connector packages published by OpenMerge. Each `connectors/<slug>/` directory is one
releasable package (layout v2): no provider code, only data that the OpenMerge runtime executes.
Changes are made on review branches and merged through pull requests; a release is cut by tagging
`<slug>@<semver>` (or `<slug>/v<semver>`), which runs the release builder (fixtures, lens laws,
category conformance) before the package is offered in the marketplace.

## Layout

```
openmerge.yaml                         # publisher metadata (name, default visibility, listing)
connectors/<slug>/connector.yaml       # identity, categories, capabilities, API transport, declarative pagination
connectors/<slug>/auth.yaml            # auth recipe (preset + overrides: inputs, discovery, request signing)
connectors/<slug>/lenses/<Model>.yaml  # one lens per unified model: read endpoint, paging, field mapping, writes
connectors/<slug>/fixtures/<Model>/*.json  # recorded list responses + expected unified values
connectors/<slug>/README.md            # what is synced, auth, provider notes
```

The unified models and categories (`ticketing@1`, `filestorage@1`, `chat@1`, Merge-compatible) ship
with OpenMerge itself; a lens names its target as `<category>.<Model>@<major>`. The package namespace
is the lower-cased GitHub owner of this repository and is stamped at release time (`0penmerge.zendesk`).

## Ticketing (`ticketing@1`)

| Connector | Slug | Auth | Models | Writes | Not synced | Fixtures |
|---|---|---|---|---|---|---|
| Aha! | `aha` | API key | Collection, Ticket, User | Ticket.update | Comment, Attachment, Tag, Role, Team | 1 |
| Asana | `asana` | OAuth 2.0 | Collection, Tag, Team, User | — | Ticket, Comment, Attachment, Role, Account, Contact | 2 |
| Azure DevOps | `azure_devops` | OAuth 2.0 | Collection, Team, Ticket | — | User, Comment, Attachment, Tag, Role | 1 |
| Basecamp | `basecamp` | OAuth 2.0 | Collection, Comment, Ticket, User | — | Attachment, Team, Role, Tag, Account, Contact | 1 |
| Bitbucket | `bitbucket` | OAuth 2.0 | Collection, User | — | Ticket, Comment, Attachment, Role, Team | 1 |
| ClickUp | `clickup` | OAuth 2.0 | Collection, Role, Ticket | — | User, Team, Comment, Attachment, Tag, Account, Contact | 1 |
| Dixa | `dixa` | API key | Contact, Tag, Team, User | — | Ticket, Comment, Attachment, Collection, Role, Account | 1 |
| Freshdesk | `freshdesk` | HTTP Basic | Account, Comment, Contact, Role, Team, Ticket, User | Ticket.create, Ticket.update | Attachment, Tag, Collection | 1 |
| Freshservice | `freshservice` | HTTP Basic | Account, Comment, Contact, Role, Team, Ticket, User | Ticket.update | Attachment, Tag, Collection | 1 |
| Front | `front` | OAuth 2.0 | Account, Collection, Comment, Contact, Tag, Team, Ticket, User | — | Attachment, Role | 1 |
| GitHub Issues | `github_issues` | OAuth 2.0 | Collection, Team, Ticket | — | User, Comment, Tag, Role, Attachment | 2 |
| GitLab | `gitlab` | OAuth 2.0 | Collection, Tag, Team, Ticket, User | — | Comment, Role, Attachment | 2 |
| Gladly | `gladly` | HTTP Basic | Collection, Tag, Team, User | — | Ticket, Contact, Comment, Attachment, Account, Role | 1 |
| Gorgias | `gorgias` | OAuth 2.0 | Comment, Contact, Tag, Team, Ticket, User | Ticket.update | Attachment, Account, Role, Collection | 1 |
| Help Scout | `help_scout` | OAuth 2.0 | Account, Collection, Comment, Contact, Tag, Team, Ticket, User | — | Attachment, Role | 1 |
| Hive | `hive` | API key | Collection, Tag, Team, Ticket, User | — | Comment, Attachment, Role, Account, Contact | 1 |
| HubSpot Ticketing | `hubspot_ticketing` | OAuth 2.0 | Account, Collection, Contact, Ticket, User | Ticket.create, Ticket.update | Comment, Attachment, Team, Role, Tag | 2 |
| Intercom | `intercom` | OAuth 2.0 | Account, Contact, Tag, Team, Ticket, User | Contact.create, Contact.update | Comment, Attachment, Role, Collection | 2 |
| Ironclad | `ironclad` | OAuth 2.0 | Team, Ticket, User | — | Comment, Attachment, Collection, Account, Contact, Role, Tag | 1 |
| Jira | `jira` | OAuth 2.0 | Collection, Comment, Role, Ticket, User | — | — | 2 |
| Jira Data Center | `jira_data_center` | OAuth 2.0 | Collection, Comment, Role, Ticket, User | — | Attachment, Team, Tag, Account, Contact | 1 |
| Jira Service Management | `jira_service_management` | OAuth 2.0 | Account, Collection, Comment, Role, Ticket, User | — | Contact, Attachment, Team, Tag | 1 |
| Kustomer | `kustomer` | API key | Account, Comment, Contact, Team, Ticket, User | — | Tag, Attachment, Collection, Role | 1 |
| Linear | `linear` | OAuth 2.0 | Account, Attachment, Collection, Comment, Tag, Team, Ticket, User | — | Role, Contact | 2 |
| Rally | `rally` | OAuth 2.0 | Attachment, Collection, Comment, Tag, Ticket, User | — | Account, Contact, Team, Role | 1 |
| Re:amaze | `reamaze` | HTTP Basic | Collection, Contact, Ticket, User | — | Comment, Tag, Attachment, Team, Role, Account | 1 |
| Salesforce Service Cloud | `salesforce_service_cloud` | OAuth 2.0 | Account, Comment, Contact, Role, Team, Ticket, User | — | Attachment, Collection, Tag | 1 |
| ServiceNow | `servicenow` | OAuth 2.0 | Account, Attachment, Comment, Role, Team, Ticket, User | Ticket.create, Ticket.update | Contact, Collection, Tag | 1 |
| Shortcut | `shortcut` | API key | Attachment, Collection, Tag, Team, User | — | Ticket, Comment, Role | 1 |
| SpotDraft | `spotdraft` | API key | Account, Role, Ticket, User | — | Comment, Attachment, Contact, Collection, Team, Tag | 1 |
| Teamwork.com | `teamwork` | OAuth 2.0 | Collection, Comment, Tag, Team, Ticket, User | Ticket.update | Attachment, Role, Account, Contact | 1 |
| Trello | `trello` | OAuth 1.0a | Collection, Tag, Ticket, User | — | Comment, Attachment, Team, Role, Account, Contact | 1 |
| Wrike | `wrike` | OAuth 2.0 | Account, Collection, Team, Ticket, User | — | Comment, Attachment, Role, Tag, Contact | 1 |
| Zendesk | `zendesk` | OAuth 2.0 | Account, Comment, Contact, Role, Tag, Team, Ticket, User | Ticket.update | Attachment, Collection | 2 |
| Zoho BugTracker | `zoho_bugtracker` | OAuth 2.0 | Collection, User | — | Ticket, Comment, Attachment, Tag, Role, Team, Account, Contact | 1 |
| Zoho Desk | `zoho_desk` | OAuth 2.0 | Account, Collection, Comment, Contact, Role, Team, Ticket, User | Ticket.update | Attachment, Tag | 1 |

## File Storage (`filestorage@1`)

| Connector | Slug | Auth | Models | Writes | Not synced | Fixtures |
|---|---|---|---|---|---|---|
| Box | `box` | OAuth 2.0 | Group, User | — | File, Folder, Drive | 1 |
| Dropbox | `dropbox` | OAuth 2.0 | File, Folder, Group, User | — | Drive | 1 |
| Google Drive | `google_drive` | OAuth 2.0 | Drive, File, Folder | — | User, Group | 2 |
| OneDrive | `onedrive` | OAuth 2.0 | Drive, File, Folder, Group, User | — | — | 2 |
| SharePoint | `sharepoint` | OAuth 2.0 | Group, User | — | Drive, File, Folder | 1 |

## Chat (`chat@1`)

| Connector | Slug | Auth | Models | Writes | Not synced | Fixtures |
|---|---|---|---|---|---|---|
| Microsoft Teams | `microsoft_teams` | OAuth 2.0 | Conversation, Group, Member, Message, User | — | — | 2 |
| Slack | `slack` | OAuth 2.0 | Conversation, Group, Message, User | — | Member | 2 |

## Conventions

- Reads default to `hash_snapshot` (authoritative full inventory, deletion by absence); providers
  with an *updated since* filter use `timestamp_delta` with a daily full-inventory reconciliation.
- Pagination is declarative (`api.pagination` in `connector.yaml`, overridden per lens with
  `read.page`): `cursor`, `page`, `offset`, `next_url`, `graphql`, `rpc` or `single`.
- Lenses map provider enums to Merge's normalized values (`map`, with a `put` table when the field is
  writable; unknown values pass through), convert epoch timestamps (`as: datetime`), resolve id
  arrays (`refs`), join first/last names (`join`) and address dotted keys with bracket paths
  (`fields["System.Title"]`). `read.keep` drops tombstones and splits mixed listings (files vs folders).
- Models a provider only lists under a parent (comments per ticket, messages per channel) declare
  `parent`; the runtime walks every parent, then its children, as one inventory and injects the
  parent id (e.g. `_ticket_id`).
- Tenant hosts (`{subdomain}`, `{host}`, `{instance}`) are asked before the OAuth redirect and must match
  the input's pattern; account/site choices (Jira cloud id, Asana workspace, ...) are discovered after
  connecting.

Check a package locally from the OpenMerge mono-repo:

```
openmerge connector release-check <path-to-this-repo> --slug <slug> --version 1.0.0
```

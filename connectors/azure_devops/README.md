# Azure DevOps

Sync Azure DevOps work items, projects and teams for one organization through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 2.0**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `workitems` | hash_snapshot | — |
| Collection | `projects` | hash_snapshot | — |
| Team | `teams` | hash_snapshot | — |

Not synced: User (Organization users are listed on vssps.dev.azure.com (Graph) or vsaex.dev.azure.com (entitlements), outside the dev.azure.com/{organization} base URL; team members are per team); Comment (Work item comments are listed per work item only); Attachment (Attachments are relations on individual work items); Tag (Tags are listed per project only (/{project}/_apis/wit/tags)); Role (Security groups/permissions live on vssps.dev.azure.com and are not role objects).

## Authentication

OAuth 2.0 authorization code (`oauth2.authorization_code`); default scopes: `499b84ac-1321-427f-aa17-267ca6975798/vso.work 499b84ac-1321-427f-aa17-267ca6975798/vso.project offline_access`.
- After connecting, the account picks `organization` from the provider's list.

## Notes

- Microsoft Entra ID delegated OAuth for the Azure DevOps resource (499b84ac-1321-427f-aa17-267ca6975798); legacy Azure DevOps OAuth apps are deprecated. Work/school accounts only (MSA users are not supported by Entra apps for Azure DevOps). organization is the dev.azure.com organization name chosen by the user.
- Every request carries api-version. Work items are read org-wide through the reporting revisions feed with includeLatestOnly=true (one latest revision per work item, continuation by watermark). Work item writes use JSON Patch documents, so none are declared. Users live on vssps.dev.azure.com / vsaex.dev.azure.com, outside this base URL. Work item field reference names contain dots (System.Title), so lenses address them with bracket paths (fields["System.Title"]) and remote_data keeps the provider's keys unchanged. System.Tags ('; '-separated string) stays in remote_data.

Provider API reference: https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.1

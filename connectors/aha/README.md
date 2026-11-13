# Aha!

Sync Aha! features, workspaces and users for one account through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **API key**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `features` | hash_snapshot | update |
| Collection | `products` | hash_snapshot | — |
| User | `users` | hash_snapshot | — |

Not synced: Comment (Comments are listed per record (feature, idea, product) only); Attachment (Attachments are listed per record only); Tag (Tags are plain strings on records; there is no account-wide tag list endpoint); Role (Workspace roles are per-user product permissions, not listable role objects); Team (Teams are scoped to workspaces in Aha! Develop; no verified account-wide team list endpoint).

## Authentication

Static credentials (`api_key` preset).
- `subdomain` — Account subdomain (<subdomain>.aha.io)

## Notes

- All calls go to the account-specific host. Lists use page/per_page (max 200) with records under the resource name plus a pagination object. The feature list returns a slim record unless fields= is given, so the list path requests the mapped fields explicitly. Aha! API keys are sent as Authorization: Bearer <key>. Aha! OAuth2 exists but its token endpoint is account-specific (https://<subdomain>.aha.io/oauth/token), which a fixed token_url cannot express, so an API key is used.

Provider API reference: https://www.aha.io/api

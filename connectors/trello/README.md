# Trello

Sync a Trello board's cards, lists, labels and members through the OpenMerge ticketing model.

Category: **Ticketing** (`ticketing@1`) · Auth: **OAuth 1.0a**

## What's synced

| Model | Native object | Read | Writes |
|---|---|---|---|
| Ticket | `cards` | hash_snapshot | — |
| Collection | `lists` | hash_snapshot | — |
| Tag | `labels` | hash_snapshot | — |
| User | `members` | hash_snapshot | — |

Not synced: Comment (Comments are commentCard actions; GET /boards/{id}/actions?filter=commentCard is capped at 1000 per request and pages only by the last action id (before), which the declarative paging cannot express, so a complete inventory is not guaranteed); Attachment (Attachments are only listable per card (GET /cards/{id}/attachments)); Team (Trello Workspaces (organizations) are listed per member (GET /members/me/organizations), outside the board-scoped base URL); Role (Trello has no role list; membership types are per-board member attributes); Account (Trello has no customer account object); Contact (Trello has no external contact object).

## Authentication

OAuth 1.0a three-legged flow (`oauth1a`); requests are HMAC-SHA1 signed.
- After connecting, the account picks `board_id` from the provider's list.

## Notes

- One connection per board: every list is board-scoped (/1/boards/{board_id}/...). Responses are bare JSON arrays. Trello caps list results at 1000 per request and only pages with before/since object ids, so boards with more than 1000 cards return the first 1000 only. Card creation dates are encoded in the card id and not exposed as a field. Trello uses a Power-Up API key plus a user token (authorized at https://trello.com/1/authorize?key=...&scope=read&expiration=never&response_type=token). Both are sent in one header: 'Authorization: OAuth oauth_consumer_key="<api_key>", oauth_token="<api_token>"' (authorization_scheme OAuth; the stored credential value is the part after 'OAuth '), or alternatively as key/token query parameters. board_id is the board's id or short link.

Provider API reference: https://developer.atlassian.com/cloud/trello/rest/

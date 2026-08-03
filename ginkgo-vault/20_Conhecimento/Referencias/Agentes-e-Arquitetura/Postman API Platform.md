---
title: "Postman API Platform"
source: "https://gschaunoficial-8657702.postman.co/home"
author:
published:
created: 2026-06-27
description: "Postman makes API development easy. Our platform offers the tools to simplify each step of the API building process and streamlines collaboration so you can create better APIs faster."
tags:
  - "clippings"
---
#### Ginkgo AI Systems, how would you like to use Postman today?

Hi there! 👋 Tell me what you're working on and I'll help you get started with Postman. I can help create requests, debug calls, generate tests, and more.

###### Suggestions to get started with:

#### Pick up where you left off

### No recent items

Start working with collections, requests, and workspaces to see them here.

![Datadog](https://res.cloudinary.com/postman/image/upload/t_team_logo/v1629887344/team/cce3460089092278711346c5a8da9d3b85714361377fc9875a860df8fa6102a3)

#### Datadog

Jun 25

### New folders for Statuspage and Salesforce integrations, plus expanded Google Chat, Metrics, Webhooks, Opsgenie, Service Accounts, Teams, and more!

New Feature

Webhooks Integration

Google Chat Integration

+3

- New [Statuspage Integration](https://docs.datadoghq.com/api/latest/statuspage-integration/) requests enable you to manage your Statuspage account connection and per-URL settings
- New [Salesforce Integration](https://docs.datadoghq.com/api/latest/salesforce-integration/) requests enable you to manage connected Salesforce organizations and incident templates
- New [Google Chat Integration](https://docs.datadoghq.com/api/latest/google-chat-integration/) requests enable you to manage organization bindings, delegated users, and target audiences
- New [Metrics](https://docs.datadoghq.com/api/latest/metrics/) requests enable you to create, reorder, and manage tag indexing rules and per-metric exemptions
- New [Webhooks Integration](https://docs.datadoghq.com/api/latest/webhooks-integration/) requests enable you to configure OAuth2 client-credentials authentication methods
- New [Service Accounts](https://docs.datadoghq.com/api/latest/service-accounts/) requests enable you to manage access tokens for service accounts
- New [Teams](https://docs.datadoghq.com/api/latest/teams/) requests enable you to manage team notification rules
- New [Application Security](https://docs.datadoghq.com/api/latest/application-security/) requests enable you to manage In-App WAF policies
- New [Opsgenie Integration](https://docs.datadoghq.com/api/latest/opsgenie-integration/) requests enable you to manage Opsgenie accounts
- New [Cloud Cost Management](https://docs.datadoghq.com/api/latest/cloud-cost-management/) requests enable you to get, generate, and manage tag descriptions
- New [Organizations](https://docs.datadoghq.com/api/latest/organizations/) requests enable you to manage SAML configurations, list global organizations, and set the maximum session duration
- New [RUM Retention Filters](https://docs.datadoghq.com/api/latest/rum-retention-filters/) requests enable you to manage permanent retention filters
- New [Feature Flags](https://docs.datadoghq.com/api/latest/feature-flags/) requests enable you to create, update, and delete feature flag variants
- New [Status Pages](https://docs.datadoghq.com/api/latest/status-pages/) requests enable you to edit and soft-delete degradation updates
- New [Security Monitoring](https://docs.datadoghq.com/api/latest/security-monitoring/) requests enable you to bulk-convert rules to Terraform, mute or unmute findings, and preview notification rules
- Plus new requests for [Reference Tables](https://docs.datadoghq.com/api/latest/reference-tables/) (list rows), [Workflow Automation](https://docs.datadoghq.com/api/latest/workflow-automation/) (list workflows), [Microsoft Teams Integration](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/) (delete user binding), [Slack Integration](https://docs.datadoghq.com/api/latest/slack-integration/) (list user bindings), [Storage Management](https://docs.datadoghq.com/api/latest/storage-management/) (delete configuration), and [Usage Metering](https://docs.datadoghq.com/api/latest/usage-metering/) (available fields)

See the [Datadog API documentation](https://docs.datadoghq.com/api/latest/) for more information.

[Read more](#)

![Postman](https://res.cloudinary.com/postman/image/upload/t_team_logo/v1629869194/team/2893aede23f01bfcbd2319326bc96a6ed0524eba759745ed6d73405a3a8b67a8)

#### Postman

Jun 23

### Postman API v1.43.0 release

Improvement

Postman API

Components

This release of the Postman API has the following updates:

### New endpoints

#### Component Library

Added endpoints that enable you to manage components in your team’s [component library](https://learning.postman.com/docs/design-apis/specifications/component-library). Maintain and standardize your team's commonly used components, without having to redefine them in each specification. Reusable components can include schemas, responses, parameters, and more.

The Postman Component Library is available with [Postman Enterprise plans](https://www.postman.com/pricing/).

**Endpoints:**

- POST `/components` — Creates a new component. The component is created in an active state with an initial draft.
- GET `/components` — Gets a list of all components in the team's component library.
- PATCH `/components/{componentId}` — Updates a component. Operations include updating the name of a component or managing its archived state. Archived components aren't deleted and can't be edited or published, but their existing versions remain accessible.
- GET `/components/{componentId}` — Gets information about a component.
- PATCH `/components/{componentId}/drafts` — Updates a component's draft. Component drafts contain unpublished edits to a component, which may be different from a recently published version.
- GET `/components/{componentId}/drafts` — Gets information about the current working draft of a component, including its content and format.
- POST `/components/{componentId}/versions` — Publishes a new version of a component from the current draft.
- GET `/components/{componentId}/versions` — Gets a list of a component's published versions.
- GET `/components/{componentId}/versions/{versionId}` — Gets a published version of a component.

### Updated endpoints

#### Environments

Implemented support for `secret` and `source` properties in the following endpoints:

- POST `/environments`
- GET PATCH PUT `/environments/{environmentId}`

#### Collections

Implemented support for `secret` and `source` properties in the GET and PATCH `/collections/{collectionId}` endpoint.

[Read more](#)

### Total rebuild os Syrve Server API collection

Breaking Change

Syrve Server API

Whole collection will be fully reconstructed. Some recuests will ne modified and moved, some deleted and replaced and many will be added.

Some examples and maybe requests can be stub, polishing them in todo list. Feel free to comment and tell what is need to be fixed.

Total:

##### 32 entities modified, 312 entities added, 15 entities removed, 13 entities moved.

[Read more](#)

### Seamless ACH REST API — Full Rebrand & Documentation Update

Improvement

Seamless ACH REST API

## What's Changed

The collection has been fully rebranded from **Paynote REST API** to **Seamless ACH REST API**, with updated API URLs, corrected request body fields, expanded documentation, and new FAQ section.

---

### Rebranding — Paynote → Seamless ACH

- **API URL:** `api-paynote.seamlesschex.com/v2` → `api.seamlesschex.com/ach/v2` Legacy URL remains active until **August 23, 2026** — update your integration before that date
- **Checkout.js SDK:** `new PAYNOTE()` → `new SEAMLESSACH()` · `paynoteIframe` → `seamlessachIframe` · `paynoteRedirect` → `seamlesschexRedirect`
- **Docs:** `developers-ach.seamlesschex.com` (old `docs.paynote.io` redirects automatically)
- **Dashboard:** `dashboard.seamlesschex.com/ach/`
- **Support:** `ach@seamlesschex.com` · System emails from `noreply-ach@seamlesschex.com`

---

### New Endpoints

| Endpoint | Description |
| --- | --- |
| `GET /funding-source/balance` | Retrieve Seamless ACH wallet balance |
| `POST /funding-source/processor/plaid` | Add verified bank account via existing Plaid processor token |

New query params: `transfer_speed` (standard / same\_day / RTP) on `POST /check/send` · `search` on `GET /user` · `number` on `GET /check`

---

### Documentation Updates

- **Micro-deposit verification deprecated June 8, 2026** — endpoint returns HTTP 410 for new connections; use Plaid Authorization instead (Auth Waterfall selects best available method automatically)
- **ACH Returns:** expanded from 14 to **80+ NACHA return codes** (R01–R85) with full descriptions
- **Getting Started:** 3-step pattern, payment types table, curl examples, environment setup
- **Checkout SDK:** Environment Mode, Lightbox Customization (7 keys), Event Handlers with code examples
- **ACH Processing Times:** RTP section (instant, 24/7/365) + Balance vs Bank Credit table
- **Online Gaming Guide:** full rewrite — Option 1A (save bank, charge later), 1B (immediate debit), Option 2 (direct API)
- **WooCommerce Plugin:** Webhook Setup & Order Status Sync + Email Notifications sections added
- **18 endpoint descriptions** updated: correct field names, response schemas, Plaid Verification Fields, pagination docs

---

### New: FAQ Folder

- **R01 (NSF) Returns & Plaid** — why insufficient-funds returns still occur despite Plaid balance checks (timing gap, pending transactions, overdraft credit)
- **Duplicate Transactions** — deduplication logic: UI layer 30s / 6 fields · Server API 3min / 4 fields

---

### How to Import Without Losing Forks

1. In Postman, rename your current collection: **Paynote REST API** → **Seamless ACH REST API**
2. Download the updated collection file
3. Import → select file → choose **Replace** (not "Import as Copy")

[Read more](#)

You're all caught up!No more updates from the last 90 days

## 🎉

### All caught up!

Requests to access, edit, and take action on resources, PRs raised by you and ones that require your review, plus other actions that need your attention will appear here.
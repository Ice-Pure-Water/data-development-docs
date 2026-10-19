# Multi-page Document Hub

Use this pattern when a data project has more than one HTML deliverable, especially when readers need to distinguish a stable target solution from changing implementation or test status.

## Pattern

Use a **hub-and-spoke** document set:

- The overview HTML is the hub and the default entry point. It states the subject and expected outcome, presents a compact end-to-end flow, and routes readers to each purpose-specific page.
- Each child page is a spoke with one job: target solution, implementation progress, test/acceptance evidence, or operations. Keep those phases separate unless the user explicitly requests a combined page.
- The hub points to the HTML reading page and the paired Markdown source when that pair exists. Do not copy detailed business rules into the hub; link to the authoritative page.
- Each spoke links back to the hub and to related pages. Repeat navigation in the same order on every page, for example: `文档总览 → 目标方案 → 开发进度 → 测试与验收`.
- Give each route a descriptive label and a short explanation of what readers can answer there. Use links/cards as document routes, not as a substitute for the data-flow diagram.

## Overview page content

Keep the hub concise and useful to readers who have not yet opened a child page:

1. Name the data domain and explain the business outcome in plain language.
2. Show one compact, semantically accurate end-to-end flow or architecture overview.
3. Provide clearly grouped routes to the requested child documents. Put the canonical target solution first; put time-sensitive progress and test evidence in separately named routes.
4. State the audience and use of each route. Show an “as of” date only for time-sensitive progress/evidence content.
5. Provide persistent links to the hub from every child HTML page.

Do not turn the hub into a second full solution document. Do not show current implementation status on the solution route; put status labels and dates on the progress/evidence route only.

## Readability and navigation

- Use regular sans-serif text for prose and monospace only for SQL, identifiers, field names, and literal values.
- Break long explanations into short paragraphs with meaningful headings, labeled callouts, or tables. Keep paragraphs to a readable line length; do not put a whole mapping schema in a code-styled paragraph.
- Make table columns reflect the content. Allow long field names to wrap and reserve horizontal scrolling for genuinely wide tables.
- Keep repeated navigation labels, placement, and order stable across pages. Use descriptive link names and visible keyboard focus.
- Use ordinary links for navigation between documents. Tabs are for switching views inside one page, not for replacing page navigation.

## Research basis

This is a synthesis of established documentation and accessibility patterns, not a claim that one exact visual design is universally preferred:

- Nielsen Norman Group describes hub-and-spoke as a way to organize related website support pages: [Customer-Service Information on Websites: The Hub-and-Spoke Model](https://www.nngroup.com/articles/customer-service-model/).
- MDN describes a landing page as the root of a documentation tree that orients readers and links to detailed API pages: [MDN page types](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Page_structures/Page_types).
- Cloudflare's documentation structure requires an Overview that orients a reader and routes them onward: [Cloudflare information architecture](https://developers.cloudflare.com/style-guide/documentation-content-strategy/information-architecture/).
- W3C guidance says repeated navigation should stay in a consistent relative order, and headings help users orient and navigate: [WCAG 2.2 Consistent Navigation](https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation), [WCAG 2.2 Navigable](https://www.w3.org/WAI/WCAG22/Understanding/navigable).
- GOV.UK explicitly cautions that tabs are not a page-navigation component: [GOV.UK Tabs](https://design-system.service.gov.uk/components/tabs/).

# HTML Presentation and Specification Views

Use this reference when a user requests HTML or when visual presentation or navigation materially helps readers understand a data specification. Markdown remains the editable source of facts. HTML may be a visual presentation, a full specification page, or both as separate views; it must not become a conflicting source of truth.

## Choose the right design help

These skills solve different problems. Route to them by the work required; do not treat one as a substitute for the others.

| Skill | Owns | Does not replace |
|---|---|---|
| `data-development-docs` | Content model, business contract, processing truth, and field lineage | Visual composition or accessibility review |
| `frontend-design` | Audience-specific design direction, visual hierarchy, typography, layout and design critique | Domain source consistency of pipeline rules |
| `diagram-design` | Diagram type, node/edge semantics, topology, spacing and visual encoding | The document's complete explanation or field-level evidence |
| `web-design-guidelines` | Focus, semantics, responsive behavior and interaction/accessibility audit | A distinctive visual concept |

For a substantial HTML redesign, use `frontend-design`. Use `diagram-design` when a flow or lineage view materially improves comprehension. Use `web-design-guidelines` for a focused audit. Keep the data-document skill responsible for factual consistency and reader priorities.

### Reference skill comparison for document-heavy HTML

When choosing a design workflow, compare it against the artifact rather than choosing by visual ambition alone:

| Candidate | Strong fit | Tradeoff for data specifications | Decision |
|---|---|---|---|
| [Effective HTML](https://github.com/plannotator/effective-html) | Routes document, plan, diagram, and interface tasks to different workflows; keeps standalone artifacts responsive and self-contained | Broad collection; only the document/plan and diagram guidance is relevant here | **Preferred reference:** borrow its content-first routing and choose a document or diagram treatment by reading task |
| [Huashu Design](https://github.com/alchaincyf/huashu-design) | Explores multiple visual directions, supplies a broad style library, and supports high-fidelity prototypes and multi-format design critique | Its style selection and prototype/animation breadth can distract from long-form rule and lineage lookup | Use when the user wants a visual concept exploration or polished prototype, not as the default for a dense specification |
| Local `frontend-design` | Establishes a distinct visual direction and critiques generic layouts | Broad UI guidance; does not choose the right document structure or confirm data-flow semantics | Use for visual composition after the content hierarchy is set |
| Local `diagram-design` | Provides diagram-specific topology and connector guidance | Solves the diagram portion only | Use for the overview flow or a focused relationship diagram |

This comparison is routing guidance, not a required external dependency. Choose the interface from its use: a reading task favors a navigable document, while a presentation or walkthrough should lead with the solution diagram and keep primary facts visible as one continuous story. Preserve project and user visual preferences over any reference style library.

## Reader hierarchy

Start from the audience's primary task. For data specification and development documents, use this default priority unless the user gives another order:

1. **Overall solution:** purpose, scope, source systems, transformation stages, and outputs.
2. **Business specification:** grain, keys, business rules, and unresolved decisions.
3. **Processing logic:** ordered steps, selection/merge rules, edge cases, and implementation mapping.
4. **Field lineage:** output field, origin, derivation, responsible step/code, and null/conflict/default behavior.

Keep relevant schema/model details, decisions, and terminology available as supporting sections. Do not add test plans/results, validation, acceptance, progress, release, or operations sections unless the user asks for them. Business, development, and test readers should be able to interpret the specification; data consumers and end-user scenarios are not a default focus. Give the four core areas the strongest navigation and visual priority. Do not hide essential business rules behind accordions or put a long unstructured article ahead of the overview.

## Design and composition

- Before coding, write a short design brief for yourself: subject, readers, primary reading task, visual direction, palette, type scale, layout, and treatment of the central diagram. Ground visual choices in the actual domain and any established user preference.
- For a presentation or walkthrough, build one continuous page around the solution/lineage map. Show the main processing stages, source/configuration/core/result table groups, key business concerns, and important output-field paths in the page itself. Keep database/table inventory in a separate, clearly grouped block outside the process diagram; identify test/development-stage and formal-stage databases and full table names, and mark code references, DDL targets, and confirmed physical objects accurately. Put exhaustive rule text and field details on a separate specification page when useful. Keep the presentation page visual-first while ensuring its primary facts are visible together; both pages must reflect the same canonical facts.
- Let information architecture drive the composition. Avoid generic SaaS card grids, decorative dashboard metrics, repeated eyebrow labels, and unrelated visual chrome. Use cards only when grouping is meaningful.
- Make the presentation overview immediately useful: identify the deliverable and scope, show the true end-to-end path, and place the main tables, business concerns, and field paths in the same continuous page. Reserve a separate document link for exhaustive reference.
- Preserve clear line lengths, whitespace, heading levels, and readable tables. On narrow screens, make wide diagrams and tables locally scrollable and keep navigation usable.
- Prefer an offline-capable page. Avoid remote fonts and network dependencies. Use JavaScript only when a reader task benefits from it. Use motion when it makes flow direction or the relationship between the overview and current detail easier to follow; keep it restrained, make the static paths clear, and support `prefers-reduced-motion`.
- After implementation, critique the page against the brief: can a reader identify scope quickly, follow the actual data path, find the four core sections, and trace an output field without guessing? Remove styling that competes with these tasks.

## Flow and lineage visuals

- Model the actual data semantics. Distinguish sources, configuration/reference inputs, intermediate states, transformations, outputs, and read-only comparison targets.
- For multi-source data, show candidate/state election separately from attribute fusion unless the implementation truly makes them the same operation. Draw both paths and their merge explicitly. Do not imply that the winning row supplies every output attribute unless verified.
- Distinguish confirmed rules, current implementation, planned sources, and unresolved details in text; color alone is insufficient. Do not draw a planned source as part of the current implemented path.
- Choose the diagram form and layout algorithm that fit the topology. For a static directed flow, Graphviz `dot` is a strong default: its layered layout aims edges in one direction and attempts to reduce crossings and edge length. For interactive layered diagrams needing orthogonal routing, ports, or compound groups, consider ELK Layered. For small hand-authored SVGs, apply the same ideas explicitly: order nodes by stage, align branches and joins, route connectors on separate lanes, and split dense views instead of routing every relationship through one crowded canvas. See [Graphviz `dot`](https://graphviz.org/docs/layouts/dot/), [Graphviz edge routing](https://graphviz.org/docs/attrs/splines/), and [Mermaid layout options](https://mermaid.ai/open-source/config/layouts.html).
- Keep overview diagrams small, readable, and free of crossing connectors. If details become dense, retain a simple overview and link to focused tables or process details.
- The overview and details must remain perceptually connected. In a continuous reading page, keep a compact side process navigation visible and link each item to its body anchor. Highlight the active stage from the section in view and associate each detailed section with its stage. This preserves context without opening a drawer or navigating away.
- When a process node has a useful detail section, link the node to that same-page anchor and keep the side navigation, node highlight, and active detail stage in sync. Use ordinary anchors so keyboard readers can follow the relationship.
- For animated flow lines, use a small number of moving packets along the actual connector routes, stagger their timing to avoid synchronized clutter, and color them to match their routes. Adjust static line weight and packet size for emphasis and readability. Honor `prefers-reduced-motion`; the diagram must remain understandable when motion is disabled.
- Fit labels to nodes: wrap long labels across lines, widen/tall the node, or use a concise Chinese display label alongside the exact technical identifier. Never let text escape its box, hide overflow, or truncate a real table/field name.
- Use natural, domain-appropriate Simplified Chinese for reader-facing concepts. Do not mechanically translate English source terms. Preserve exact technical identifiers and source-native codes. Keep a small consistent glossary when one English concept has multiple Chinese renderings.
- For field lineage, make the trace inspectable: output field → source field/value → derivation → processing step or code → material edge behavior. Use a table when readers compare fields; use a graph only when relationships are clearer as a graph.
- Check node labels, edge endpoints, and directions against the source document, code, and DDL.
- If Markdown uses Mermaid or another diagram notation as its editable source, render a visual diagram in reader-facing HTML. Do not leave raw source such as `flowchart LR` as the visible flowchart.

## Accessibility and interaction

- Use semantic `header`, `nav`, `main`, `section`, headings, lists, tables, and links. Include a skip link, descriptive page title, unique section IDs, and a logical heading hierarchy.
- Keep all core content reachable without JavaScript. Use links for navigation and buttons for actions. Make interactive controls keyboard operable and visibly focused.
- Use interaction only when it supports the presentation task. Do not hide main-flow, table, business-rule, or lineage facts behind click-to-reveal panels when the page is meant to tell the complete story continuously.
- Add a focused secondary diagram in the continuous presentation when branching logic, responsibility splits, or multi-hop field lineage is hard to explain in prose or a table. Keep it near the relevant part of the main flow and derive it from the same specification; do not duplicate the full overview or add decorative diagrams.
- Ensure sticky navigation does not cover anchor headings or focused content. Respect `prefers-reduced-motion` whenever motion is present.
- Give diagrams a useful accessible name and description; retain a text explanation or adjacent process table. Do not rely on color alone for state.
- Check contrast, small-screen reflow, table overflow, and focus visibility. Avoid `transition: all` and hover-only meaning.

## Verification

- Parse the HTML; check document structure, unique IDs, valid local anchors, and any script syntax.
- Reconcile headings, business rules, table/field names, scope labels, dates, and implementation statements against Markdown and source materials. HTML layout may reorder sections to support presentation or lookup, but it must not change facts.
- Check that every navigation link resolves and that any search/filter control works by keyboard as well as pointer.
- If a browser render is available and permitted, inspect a normal desktop width and a narrow width. Follow one route from the overview to a rule, process step, and field lineage detail.
- Report source consistency boundaries. Parsing does not prove visual quality or semantic correctness; a screenshot does not prove source-to-field lineage. If browser inspection is unavailable or restricted, state that clearly and do not claim visual QA.

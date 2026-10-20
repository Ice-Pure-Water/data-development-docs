# Document Model

Use one focused specification for a data deliverable. Its default reading path is: understand the overall solution, agree on business meaning, follow processing logic, and trace output fields. Keep schema/model information and unresolved decisions as supporting views. Do not add test plans, validation results, acceptance sections, release procedures, or operations runbooks unless requested.

## Recommended sections

Adapt order and depth to the user's task. Do not add boilerplate sections that do not help readers understand the data solution.

1. **Identity and summary** — name, purpose, business/development/test readers, version/update date, scope, source materials.
2. **Overall solution and data flow** — sources, dependencies, transformations, outputs, and how the parts fit together.
3. **Business specification** — business purpose and scope, grain, keys, definitions, inclusion/exclusion, constraints, precedence, exceptions, resulting values, and open decisions.
4. **Processing and implementation mapping** — named operations, inputs/outputs, joins, filters, mappings, selection/fusion, aggregation, edge behavior, and code/task locations.
5. **Field lineage** — output field meaning, origin, derivation, responsible step, and null/conflict/default behavior.
6. **Table/model details** — source, configuration/dictionary, core/intermediate, and result tables; physical/logical purpose, environment/database, grain, keys, types, relationships, and relevant schema details.
7. **Decisions and terminology** — consequential choices, rationale, consequences, unresolved business choices, and domain vocabulary.

## Stable content contracts

Use these fields as the minimum content contract for each section. Omit a field only when it does not apply or the sources do not establish it; mark a consequential unknown as open instead of filling it by guesswork. The exact Markdown layout can vary, but the facts should remain extractable into HTML without reinterpretation.

### Overall solution and data flow

State the business object and grain, included source families, sequence of processing stages, key branches/merges, target output, and the boundary between the intended solution and the code currently present. Explain whether each path is implemented, planned, or unresolved. Every source named in scope must either have a path in the diagram or an explicit “not connected / needs confirmation” endpoint.

### Business rules

For each result-changing rule, record:

| Rule meaning | Trigger/input boundary | Decision or priority | Resulting value/behavior | Requirement or implementation | Source locator / unresolved point |
|---|---|---|---|---|---|

Describe the comparison direction and tie-breakers explicitly (for example, smallest priority value wins, then latest effective date); a phrase such as “highest priority” is insufficient when the ordering convention could be ambiguous. Keep requirement and observed SQL behavior separate where they differ.

### Table and configuration inventory

Use one row per environment-qualified object, even when the same logical object exists in test and formal databases:

| Stage/environment | Database-qualified object | Category | Read/write role | Grain and key | Purpose/dependencies | SQL reference | DDL target | Physical deployment evidence |
|---|---|---|---|---|---|---|---|---|

Cover source, mapping/configuration/dictionary, core/intermediate, and result objects. “Used in SQL”, “declared by DDL”, and “confirmed deployed” are separate facts. Use “not confirmed” when no direct deployment evidence exists. Keep the inventory outside the process diagram.

### Processing steps

Give each meaningful operation a stable descriptive heading. For the operation itself, state its purpose, input object and filter, join/mapping, transformation order, row-selection or aggregation rule, output object/grain, downstream consumer, code/task locator, and material null/no-match/conflict behavior. A reader should be able to follow the step in order without reconstructing it from scattered SQL fragments.

### Output field lineage

Use one row per important output field and retain these columns:

| Output object.field | Meaning and grain | Source object.field / constant / derivation | Transformation and business rule | Processing step and code locator | Null, default, conflict, or fallback behavior |
|---|---|---|---|---|---|

For multi-source values, state which source supplies the value and how the source is chosen. Link a derived field to both its governing rule and the processing step. Do not use vague origins such as “from upstream tables” or “calculated in SQL.”

### Cross-section links

Keep a direct chain from business rule to its processing step and from that step to affected output fields. Use descriptive labels and existing Markdown anchors; do not invent visible object or rule codes. Reuse the same Chinese terms and exact technical identifiers in Markdown, overview HTML, and full-document HTML.

## Cross-link model

Keep the core chain navigable:

`business purpose → business rule → processing operation → output table/field`

Use descriptive section titles and exact business or schema names. Do not invent visible rule, table, or field codes. Link each rule to the processing step that implements it, and each output field to its source and derivation. Do not add test/runbook destinations by default.

## Claim labels

Distinguish claims by their source:

- **Requirement:** agreed business rule or requested specification condition.
- **Design:** intended solution, not necessarily implemented.
- **Implementation:** behavior visible in code, DDL, or configuration; include a locator when possible.
- **Open:** missing business decision or source detail, with its effect on the solution.

Keep these distinctions local to the relevant rule or field. Avoid one document-wide badge that implies the whole solution is complete. When comparing test/development and formal stages, identify the database and full table name at each stage, and distinguish current SQL references, DDL targets, and confirmed physical objects. Keep this inventory separate from the process diagram.

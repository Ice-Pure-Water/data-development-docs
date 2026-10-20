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

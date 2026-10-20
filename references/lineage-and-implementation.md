# Lineage and Implementation Mapping

Use this reference to make the data solution understandable from business rule to output field. Focus on declared design and implementation sources. Run results, test evidence, and operational evidence belong elsewhere and are outside this skill's default scope.

## Processing map

For each meaningful operation, record its purpose, inputs, outputs, rule/decision, transformation order, filters/joins, grain changes, code/task location, and material edge behavior. Describe lookup and configuration dependencies separately from business source data.

Represent source-specific processing, shared transformations, selection/merging, and output writes as they occur. For multi-source logic, identify which candidate determines the status and which other source attributes still contribute. Draw explicit paths for each branch and merge when using a diagram.

## Field-level lineage

Use one row per important target field. A practical baseline:

| Output table.field | Meaning | Grain/key | Origin table.field or derivation | Transformation/rule | Processing step and code | Null/default/conflict behavior |
|---|---|---|---|---|---|---|

Identify constants, configuration, and rule-only derivations as origins. Describe conditional sources, precedence, aggregation, and provenance; do not reduce a multi-source result to “from source A/B.” Mark proposed logical fields separately from physical schema observations.

## Requirement, design, and implementation

Distinguish these claims:

- **Requirement:** what an agreed business rule or requested data specification requires.
- **Design:** the intended behavior or architecture.
- **Implementation:** behavior visible in code, DDL, or task configuration; include a locator and version/commit when available.
- **Open:** a missing business decision or source detail that affects the solution.

Code inspection describes implementation but does not establish run outcomes. Do not put test results, acceptance metrics, validation procedures, or operational claims in this specification unless the user explicitly expands the scope.

## Incremental behavior when it is part of the processing design

Describe only when relevant to the requested solution:

- change detection and affected-key/range discovery;
- recomputation scope, including late-arriving updates;
- idempotency, partial writes, duplicate prevention, and retry semantics as design/implementation facts;
- deletes, tombstones, retractions and behavior when no active input remains;
- full rebuild and backfill shape;
- cleanup and rollback behavior if they change output semantics.

Do not infer that a task is idempotent just because it can be retried. State only the behavior supported by code/configuration or label it as a design requirement.

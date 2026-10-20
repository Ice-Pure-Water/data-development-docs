# Data Contracts

Read this reference only when the user explicitly includes a producer/consumer data contract in scope. It is optional support material; the default data development specification is centered on the solution, business rules, processing logic, tables, and field lineage.

## Contract dimensions

Include applicable items:

- **Identity and purpose** — dataset/product name, intended use, limitations, document version and scope.
- **Location** — interface or storage location and environment. Avoid recording secrets.
- **Schema and semantics** — logical and physical types, fields, grain, keys, required/nullable behavior, allowed values, definitions, relationships and compatibility.
- **Service expectations** — freshness or delivery timing only when included in the requested contract; record the agreed expectation or mark it open.
- **Change management** — versioning or compatibility only when included in the requested contract.

State business commitments in concrete terms. Mark unknown terms as open decisions rather than inventing thresholds or operating procedures.

## Use standards proportionally

[Open Data Contract Standard (ODCS)](https://docs.datacontract.com/open-data-contract-standard) is a vendor-neutral reference for identity, schema, semantic definitions, team and server/location metadata. Use an existing organization format when one is established. Adopt ODCS or another machine-readable schema only when it fits the team's implementation workflow; a human-readable Markdown contract is still useful when automation is unavailable.

## Contract review questions

- Are the requested contract's grain, keys, field meanings, nullability, and time semantics unambiguous?
- Are grain, keys, field meanings, nullability and time semantics unambiguous?
- Are requested service expectations clear?

## Further reading

- [Open Data Contract Standard](https://docs.datacontract.com/open-data-contract-standard)
- [Open Data Product Specification](https://opendataproducts.org/v4.1/)
- [dbt sources](https://docs.getdbt.com/docs/build/sources)

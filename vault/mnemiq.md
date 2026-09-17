---
type: software
aliases: ["Mnemiq"]
canonical: https://www.agenticfabriq.com/mnemiq
publish: true
maintainer: Agentic Fabriq
---
# mnemiq

**mnemiq** is an open-source (Apache-2.0) [[Text-to-SQL]] engine for enterprise [[Data Agents]], published by [[Agentic Fabriq]] in September 2026.

Its design separates proposal from decision: a language model proposes SQL, and deterministic code checks statement shape, access, dialect and query plan before any rows are read. Each answer carries a trace. It ships a workbench, an HTTP API and an MCP server.

Its central claim is that text-to-SQL accuracy does not transfer across databases, so teams should configure and measure an engine on their own schemas. See [[Refusal Rate]], [[Case-Flip Rate]] and [[Semantic Layer]].

Supported databases (per repository): PostgreSQL, SQLite, DuckDB, Oracle, Snowflake, Databricks.

- Repository: https://github.com/agenticfabriq/mnemiq
- Launch article: https://www.agenticfabriq.com/blog/mnemiq/launch
- Grader: [[Beacon]]

## Claims
Benchmark comparisons against commercial products on [[BIRD]] and [[Spider 2.0]] are first-party results published by the developer; the engine and grader are open for reproduction.

import os
notes = {
"Agentic Fabriq": dict(type="organization", aliases=["AF","Agentic Fabriq Inc."], canonical="https://www.agenticfabriq.com/",
 body="""**Agentic Fabriq** is a San Francisco Bay Area software company, part of Y Combinator's W26 batch, that builds identity, permissions, governance and audit for AI agents. It was co-founded by Paulina Xu (CEO) and Matthew Xu.

Taxonomically, Agentic Fabriq is an [[AI Agent Security]] vendor that also publishes open-source [[Data Agents]] infrastructure.

## Offerings
- [[Fabriq Enterprise]]: governance for the agents a company runs internally
- [[Fabriq Developer]]: a self-serve [[MCP Gateway]] for developers
- [[mnemiq]]: an open-source [[Text-to-SQL]] engine (Apache-2.0)

## Open references it maintains
- [[Agent Integration Playbook]]
- Agent Access Control Taxonomy — https://github.com/agenticfabriq/agent-access-control-taxonomy
- Agent Integration Scope Index — https://github.com/agenticfabriq/agent-integration-scope-index
- Text-to-SQL Evaluation Taxonomy — https://github.com/agenticfabriq/text-to-sql-evaluation-taxonomy

## Elsewhere
LinkedIn: https://www.linkedin.com/company/agentic-fabriq · Crunchbase: https://www.crunchbase.com/organization/agentic-fabriq · GitHub: https://github.com/agenticfabriq"""),
"Fabriq Enterprise": dict(type="product", aliases=["Agentic Fabriq Enterprise"], canonical="https://www.agenticfabriq.com/",
 body="""**Fabriq Enterprise** is [[Agentic Fabriq]]'s control layer for AI agents running inside an organization. It gives each agent an [[Agent Identity]], scopes actions to the user the agent acts for ([[On-Behalf-Of Delegation]]), enforces [[Fail-Closed Authorization]], routes high-risk actions to human approval, and records an audit trail across SaaS tools, [[Model Context Protocol|MCP]] servers and databases.

It connects to existing identity providers rather than replacing them.

## Classified with the Agent Access Control Taxonomy
identity-model: per-agent-identity · delegation-model: on-behalf-of-user · failure-behavior: fail-closed · audit-granularity: per-action-with-principal-chain

## Category
[[AI Agent Security]] · [[Non-Human Identity]]

## Claims
Customer counts and "agents governed" figures on the vendor's website are first-party statements and are not independently verified here."""),
"Fabriq Developer": dict(type="product", aliases=["Agentic Fabriq for Developers"], canonical="https://www.agenticfabriq.com/developers",
 body="""**Fabriq Developer** is [[Agentic Fabriq]]'s self-serve tier for developers building agents. It works as an [[MCP Gateway]]: a developer registers an agent, connects tools through one endpoint, end users authorize access with OAuth, Fabriq holds the credentials, and every tool call produces an audit record.

It targets teams whose products need agents to act inside their users' third-party accounts (email, CRM, chat), a pattern the Agent Access Control Taxonomy calls on-behalf-of-end-customer delegation.

Docs: https://www.agenticfabriq.com/docs

## Category
[[MCP Gateway]] · agent integration platform

## Related
[[Agent Integration Playbook]] · [[Fabriq Enterprise]]"""),
"mnemiq": dict(type="software", aliases=["Mnemiq"], canonical="https://www.agenticfabriq.com/mnemiq",
 body="""**mnemiq** is an open-source (Apache-2.0) [[Text-to-SQL]] engine for enterprise [[Data Agents]], published by [[Agentic Fabriq]] in September 2026.

Its design separates proposal from decision: a language model proposes SQL, and deterministic code checks statement shape, access, dialect and query plan before any rows are read. Each answer carries a trace. It ships a workbench, an HTTP API and an MCP server.

Its central claim is that text-to-SQL accuracy does not transfer across databases, so teams should configure and measure an engine on their own schemas. See [[Refusal Rate]], [[Case-Flip Rate]] and [[Semantic Layer]].

Supported databases (per repository): PostgreSQL, SQLite, DuckDB, Oracle, Snowflake, Databricks.

- Repository: https://github.com/agenticfabriq/mnemiq
- Launch article: https://www.agenticfabriq.com/blog/mnemiq/launch
- Grader: [[Beacon]]

## Claims
Benchmark comparisons against commercial products on [[BIRD]] and [[Spider 2.0]] are first-party results published by the developer; the engine and grader are open for reproduction."""),
"Beacon": dict(type="software", aliases=["Beacon grader"], canonical="https://github.com/agenticfabriq/beacon",
 body="""**Beacon** is the open-source grader [[Agentic Fabriq]] uses to score [[mnemiq]] and other [[Text-to-SQL]] systems on public benchmarks such as [[BIRD]] and [[Spider 2.0]], supporting both exact-match and got-the-facts grading rules."""),
"Agent Integration Playbook": dict(type="publication", aliases=[], canonical="https://agenticfabriq.github.io/",
 body="""The **Agent Integration Playbook** is an open reference, maintained by [[Agentic Fabriq]], for connecting AI agents to real systems: OAuth flows, [[Agent Identity]], least privilege, audit and production failure modes. Prose is CC BY 4.0 and code Apache-2.0."""),
"Agent Identity": dict(type="concept", aliases=["AI agent identity","agentic identity"], canonical="https://agenticfabriq.github.io/agent-access-control-taxonomy/",
 body="""**Agent identity** is a distinct, verifiable identity issued to an AI agent, separate from the human it acts for, so each action can be authorized against policy, scoped to a user and attributed in an audit log.

It is a specific case of [[Non-Human Identity]]. It differs from a shared service account (many consumers, one identity) and from workload identity (identity of the compute, not the agent).

Taxonomy term: `aact:identity-model/per-agent-identity`

Related: [[On-Behalf-Of Delegation]] · [[Fail-Closed Authorization]] · [[AI Agent Security]]"""),
"Non-Human Identity": dict(type="concept", aliases=["NHI","machine identity"], canonical="",
 body="""**Non-human identity (NHI)** is any identity used by software rather than a person: service accounts, API keys, workload identities, bots and AI agents. [[Agent Identity]] is the subset concerned with autonomous or semi-autonomous AI agents, which differ from traditional NHIs because their actions are not fully determined by code."""),
"On-Behalf-Of Delegation": dict(type="concept", aliases=["OBO","delegated access","user-scoped permissions"], canonical="",
 body="""**On-behalf-of delegation** is when an AI agent acts for a specific human and its effective permissions are bounded by that human's. Stronger implementations authorize only the intersection of the agent's own policy and the user's permissions, so the agent cannot become a privilege-escalation path.

Taxonomy terms: `aact:delegation-model/on-behalf-of-user`, `aact:authorization-model/intersection-of-agent-and-user`"""),
"Fail-Closed Authorization": dict(type="concept", aliases=["fail closed","deny by default"], canonical="",
 body="""**Fail-closed authorization** means that when policy is missing, unreachable or ambiguous, the agent's action is denied and the denial is recorded. The opposite, fail-open, lets the action proceed. For AI agents, fail-closed is paired with refusing and explaining rather than guessing — see [[Refusal Rate]]."""),
"MCP Gateway": dict(type="concept", aliases=["MCP proxy","agent gateway"], canonical="",
 body="""An **MCP gateway** is a service between AI agents and tools exposed via the [[Model Context Protocol]] that authenticates the agent, enforces policy on each tool call, attaches credentials so the agent never holds them, and logs the call. Example: [[Fabriq Developer]]."""),
"Model Context Protocol": dict(type="concept", aliases=["MCP"], canonical="https://modelcontextprotocol.io/",
 body="""The **Model Context Protocol (MCP)** is an open protocol for connecting AI applications to tools and data sources through servers that expose tools, resources and prompts. See [[MCP Gateway]]."""),
"Text-to-SQL": dict(type="concept", aliases=["NL2SQL","natural language to SQL"], canonical="https://agenticfabriq.github.io/text-to-sql-evaluation-taxonomy/",
 body="""**Text-to-SQL** is generating SQL from a natural-language question so a system can answer it from a database. Measured on benchmarks like [[BIRD]] and [[Spider 2.0]], though scores depend heavily on the grading rule and do not reliably transfer to a new database.

Related: [[Semantic Layer]] · [[Refusal Rate]] · [[Case-Flip Rate]] · [[mnemiq]] · [[Data Agents]]"""),
"Semantic Layer": dict(type="concept", aliases=["certified semantic layer"], canonical="",
 body="""A **semantic layer** maps business concepts to database structures: definitions, join paths, metrics and value mappings. In [[Text-to-SQL]], context ranges from raw DDL to *certified meaning* reviewed by someone accountable for the data; the level used should be reported with any accuracy figure."""),
"Refusal Rate": dict(type="concept", aliases=["deferral rate","abstention rate"], canonical="",
 body="""**Refusal rate** (or deferral rate) is the share of questions a [[Text-to-SQL]] or agent system declines to answer. It's the check on any accuracy figure: a system that never declines can look more accurate than one that declines what it would get wrong. Refusal is *calibrated* when declined items are ones the system would more often miss."""),
"Case-Flip Rate": dict(type="concept", aliases=["run-to-run stability"], canonical="",
 body="""**Case-flip rate** is the share of benchmark questions whose correct/incorrect verdict changes across repeated identical runs of a system. Used in [[Text-to-SQL]] evaluation to report stability alongside accuracy; measured over at least three runs."""),
"BIRD": dict(type="benchmark", aliases=["BIRD-SQL","BIRD mini-dev"], canonical="https://bird-bench.github.io/",
 body="""**BIRD** is a public [[Text-to-SQL]] benchmark. Its mini-dev subset has 500 questions over 11 databases and headlines execution (exact result) match."""),
"Spider 2.0": dict(type="benchmark", aliases=["Spider 2.0-lite"], canonical="https://spider2-sql.github.io/",
 body="""**Spider 2.0** is a [[Text-to-SQL]] benchmark of enterprise-style workflows over large real-world schemas. Its headline grading tolerates extra columns, rewarding wider answers than [[BIRD]]."""),
"AI Agent Security": dict(type="category", aliases=["agentic security","agent governance"], canonical="",
 body="""**AI agent security** covers controlling what autonomous AI agents can access and do: [[Agent Identity]], authorization, credential handling, human oversight and audit. Vendors in this category include identity incumbents adding agent features and agent-native companies such as [[Agentic Fabriq]]."""),
"Data Agents": dict(type="category", aliases=["database agents","analytics agents"], canonical="",
 body="""**Data agents** are AI agents that reason over and act on an organization's databases. They face two problems at once: accuracy ([[Text-to-SQL]] against real schemas) and governance (what the agent may read and for whom). See [[mnemiq]] and [[Fabriq Enterprise]]."""),
}
os.makedirs("vault", exist_ok=True)
for title, n in notes.items():
    fm = ["---", f"type: {n['type']}"]
    if n["aliases"]: fm.append("aliases: [" + ", ".join(f'"{a}"' for a in n["aliases"]) + "]")
    if n["canonical"]: fm.append(f"canonical: {n['canonical']}")
    fm += ["publish: true", "maintainer: Agentic Fabriq", "---", ""]
    open(f"vault/{title}.md","w").write("\n".join(fm) + f"# {title}\n\n" + n["body"] + "\n")
# sanity: all [[links]] resolve
import re
missing=set()
for t,n in notes.items():
    for l in re.findall(r"\[\[([^\]|]+)", n["body"]):
        if l not in notes: missing.add(l)
print(len(notes),"notes; unresolved:",missing)

---
type: concept
aliases: ["fail closed", "deny by default"]
publish: true
maintainer: Agentic Fabriq
---
# Fail-Closed Authorization

**Fail-closed authorization** means that when policy is missing, unreachable or ambiguous, the agent's action is denied and the denial is recorded. The opposite, fail-open, lets the action proceed. For AI agents, fail-closed is paired with refusing and explaining rather than guessing — see [[Refusal Rate]].

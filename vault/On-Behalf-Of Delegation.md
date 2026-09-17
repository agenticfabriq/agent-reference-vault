---
type: concept
aliases: ["OBO", "delegated access", "user-scoped permissions"]
publish: true
maintainer: Agentic Fabriq
---
# On-Behalf-Of Delegation

**On-behalf-of delegation** is when an AI agent acts for a specific human and its effective permissions are bounded by that human's. Stronger implementations authorize only the intersection of the agent's own policy and the user's permissions, so the agent cannot become a privilege-escalation path.

Taxonomy terms: `aact:delegation-model/on-behalf-of-user`, `aact:authorization-model/intersection-of-agent-and-user`

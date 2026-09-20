# Architecture Decision Records (ADRs)

Document critical architectural decisions to ensure persistent alignment and prevent circular discussions.

---

## ADR-001: Architecture & Folder Structure
- **Date**: {{DATE}}
- **Status**: Accepted
- **Context**: The project requires scalable organization separating route handlers, business domains, and shared infrastructure.
- **Decision**: Adopt the standard feature-based / clean modular architecture defined in `docs/ARCHITECTURE.md`.
- **Consequences**: Features are self-contained. Adding a new domain does not clutter global components or routes.

---

## ADR-002: Tech Stack Selection
- **Date**: {{DATE}}
- **Status**: Accepted
- **Context**: Need a robust, type-safe stack supporting rapid iteration and production scalability.
- **Decision**: Use {{TECH_STACK_SUMMARY}}.
- **Consequences**: Standardized tooling across the team with strict type safety.


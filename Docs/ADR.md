# Architecture Decision Records (ADR) — Guide & Level 1 Implementation

## 1. What is an ADR?

An Architecture Decision Record (ADR) is a short document that captures an important technical decision, including:

* The context (problem)
* The options considered
* The decision made
* The consequences

### Why ADRs Matter

* Preserve reasoning over time
* Prevent repeated debates
* Improve system design clarity
* Help you think like an engineer, not just a coder

---

## 2. How to Use ADRs (Simple Workflow)

1. Identify a decision (e.g., "Which retrieval method?")
2. Write the context (why this matters)
3. List options (at least 2)
4. Choose one
5. Document tradeoffs

---

## 3. ADR Template (Reusable)

```md
# ADR-XXX: <Decision Title>

## Status
Proposed | Accepted | Rejected | Deprecated

## Context
What problem are we solving?
What constraints exist?

## Options Considered
1. Option A
2. Option B
3. Option C

## Decision
What did we choose and why?

## Consequences
### Positive
- Benefits of this decision

### Negative
- Tradeoffs / limitations

## Notes (Optional)
Any additional thoughts
```

---

## 4. Level 1 ADRs (Foundations)

---

# ADR-001: Use Monolithic Architecture for Level 1

## Status

Accepted

## Context

The goal of Level 1 is to build a simple, working RAG system to understand core concepts. The system should be easy to develop, debug, and iterate on.

Constraints:

* Single developer
* Learning-focused project
* Limited complexity required

## Options Considered

1. Monolithic architecture
2. Microservices architecture
3. Layered distributed system

## Decision

Use a monolithic architecture where all components (ingestion, retrieval, generation) exist in a single codebase.

## Consequences

### Positive

* Simple to build and debug
* Fast iteration
* Low overhead

### Negative

* Not scalable
* Tight coupling between components

---

# ADR-002: Use Basic Fixed-Size Chunking

## Status

Accepted

## Context

Documents (PDFs, text) must be split into chunks before embedding. At this stage, simplicity is preferred over optimization.

Constraints:

* No complex parsing required
* Focus on understanding RAG basics

## Options Considered

1. Fixed-size chunking
2. Semantic chunking
3. Section-aware chunking

## Decision

Use fixed-size chunking (e.g., 500 tokens with overlap).

## Consequences

### Positive

* Easy to implement
* Works for most documents

### Negative

* May split important context
* Lower retrieval quality

---

# ADR-003: Use Vector Search (FAISS or Similar)

## Status

Accepted

## Context

The system needs a way to retrieve relevant document chunks based on user queries.

Constraints:

* Simplicity
* Local development

## Options Considered

1. Vector search (FAISS)
2. Keyword search (BM25)
3. Hybrid search

## Decision

Use vector search with embeddings stored in FAISS (or similar lightweight vector DB).

## Consequences

### Positive

* Fast similarity search
* Easy to implement locally

### Negative

* May miss keyword-specific matches
* No hybrid optimization

---

# ADR-004: Use Simple RAG Pipeline

## Status

Accepted

## Context

The system must answer user questions using retrieved documents.

Constraints:

* Keep logic simple
* Focus on learning pipeline flow

## Options Considered

1. Basic pipeline (retrieve → generate)
2. Advanced pipeline (retrieve → rerank → generate → validate)
3. Agent-based system

## Decision

Use a simple pipeline:
Query → Retrieve Top-K → Generate Answer

## Consequences

### Positive

* Easy to understand
* Fast to implement

### Negative

* No validation or guardrails
* Higher hallucination risk

---

# ADR-005: Use Direct LLM Generation Without Guardrails

## Status

Accepted

## Context

At Level 1, the goal is to understand core RAG mechanics, not safety or governance.

Constraints:

* Minimal complexity

## Options Considered

1. Raw LLM generation
2. Guardrail-based generation

## Decision

Use direct LLM generation with retrieved context.

## Consequences

### Positive

* Simplifies system design
* Faster experimentation

### Negative

* No safety controls
* Not suitable for real-world healthcare use

## Context
This defines the processing architecture (data flow), not system structure.

---

## 5. Key Learning Takeaways

From Level 1 ADRs, you should understand:

* Simplicity is intentional at early stages
* Every decision has tradeoffs
* Architecture evolves over time

---

## 6. How This Evolves in Later Levels

| Level   | What Changes         |
| ------- | -------------------- |
| Level 2 | Modularization + API |
| Level 3 | Guardrails + safety  |
| Level 4 | Hybrid retrieval     |
| Level 5 | Scalability          |

---

## 7. Final Note

ADRs are not static documents.
They evolve as your system evolves.

When you upgrade your system:

* Create new ADRs
* Or mark old ones as "Deprecated"

This is how real engineering teams track system evolution.

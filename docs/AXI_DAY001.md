# AXI_DAY001 — Evolving Evaluation Axes
*(EDiE Research Log / Day 1)*

## Notice
This document is an ongoing research log. It may contain provisional hypotheses and incomplete results.

---

## 1. Purpose
This day establishes **AXI** as a research track under **Evolutionary Discovery Engineering (EDiE)**.

AXI explores a radical idea:

> Evaluation axes (metrics, criteria, benchmarks) should not be fixed.  
> They should be **generated, competed, and selected** under evolutionary pressure.

In short:
- We do not only evolve algorithms.
- We evolve **how we evaluate algorithms**.

---

## 2. Motivation
Modern AI progress is heavily shaped by fixed human-designed benchmarks.
This introduces hidden constraints:
- Goodhart effects (optimizing the benchmark, not the capability)
- baked-in assumptions about what “intelligence” is
- narrow task selection bias

EDiE demands one more step:
> Remove an additional layer of human assumptions by evolving the evaluation itself.

---

## 3. AXI Core Concept
### 3.1 Objects
- **Candidate axes**: evaluation rules, test generators, scoring functions
- **Subjects**: models / algorithms / agents
- **Environment**: constraints and contexts under which axes operate

### 3.2 Selection Pressure for Axes
An evaluation axis survives if it is:
- discriminative (separates meaningful differences)
- reproducible (stable under re-runs)
- robust (resistant to trivial gaming)
- actionable (leads to useful discoveries)
- aligned to human value *after the fact* (humans remain final judges)

---

## 4. MVP Plan
We start with **IWR** (Iterative Why Robustness) from WHY as the first axis candidate.
Then we evolve axis variants:
- different “why” operators
- different collapse detectors
- different domains and seed distributions
- different scoring decompositions

Axes compete by how well they:
- produce stable rankings across runs
- detect collapse earlier and more reliably
- reveal new model differences that standard benchmarks miss

---

## 5. Key Hypotheses
- A1: Some axes are inherently more “alive” (more informative) than others.
- A2: Evolved axes will discover failure modes that human-designed benchmarks overlook.
- A3: A small set of survivor axes will generalize across model scales and domains.

---

## 6. Why This Matters
If AXI works, it becomes:
- a new method to build benchmarks without manual curation
- a meta-tool to reduce human assumption bias in evaluation
- a reusable engine across domains (LLMs, edge AI, control, autonomy)

---

## 7. Next Steps
- Build an axis-generation + axis-selection framework
- Define axis fitness functions and anti-gaming checks
- Run the first “axis tournament” using IWR variants
- Publish reproducible code and baseline results

---

## References
- EDiE Manifesto: ../Evolutionary_Discovery_Engineering_MANIFESTO.md
- WHY_DAY001: ./WHY_DAY001.md

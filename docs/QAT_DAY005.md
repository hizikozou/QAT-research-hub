# QAT_DAY005: Experimental Roadmap — From Zero Environment to Quantization Survival Tournament

## Abstract

This chapter defines a concrete, reproducible experimental roadmap
for discovering quantization survival strategies through automated generation and competition.

Unlike prior chapters, this document focuses exclusively on **what will be done next**:
environment setup, models, algorithms, evaluation code, and iteration milestones.

This is an execution plan.

---

## 0. Initial Conditions

- Hardware: RTX 5060 Ti (16GB)
- OS: Local workstation (no prior LLM environment installed)
- Existing software:
  - Python runtime available
  - Stable Diffusion (A1111) previously used on other GPU
- Current state:
  - No LLM runtime
  - No quantization framework installed
  - Near-clean environment

All setup steps will be explicitly documented.

---

## 1. Environment Setup (Milestone M1)

### 1.1 Base Runtime
- Python version fixed (e.g., 3.10)
- Virtual environment creation
- CUDA / driver version verification
- PyTorch GPU build confirmation

### 1.2 Core Libraries
- transformers
- accelerate
- bitsandbytes
- numpy / scipy
- evaluation utilities

**Deliverable:**  
A minimal script confirming GPU inference works on an unquantized model.

---

## 2. Target Models for Quantization (Milestone M2)

Models are selected based on:

- Public availability
- Moderate size (fits on single GPU)
- Existing quantization baselines

Initial candidates include:

- Small-to-mid LLMs (e.g., ~3B–7B range)
- Models commonly used as:
  - Lightweight inference cores
  - Reasoning-focused backbones

Exact model list will be fixed and versioned.

**Deliverable:**  
Baseline inference results without quantization.

---

## 3. Quantization Strategy Representation (Milestone M3)

Each quantization strategy is represented as a structured object containing:

- Layer-wise bit-width assignments
- Scaling / normalization method per layer group
- Arithmetic approximation flags
- Outlier handling rules
- Mixed-precision layout

This representation is independent of any specific algorithm.

**Deliverable:**  
A serializable strategy schema (e.g., JSON or Python object).

---

## 4. Strategy Generation Mechanism (Milestone M4)

Quantization strategies are generated automatically using:

- Constraint-aware random sampling
- Optional prompt-driven generation (LLM-assisted)
- Mutation operators:
  - Bit-width shifts
  - Layer group reassignment
  - Scaling method swaps

Human-designed heuristics are explicitly minimized.

**Deliverable:**  
A generator that produces valid, executable strategies.

---

## 5. Strategy Competition Framework (Milestone M5)

Each strategy is treated as a player.

Competition loop:

1. Apply quantization strategy
2. Run fixed inference tasks
3. Collect evaluation metrics
4. Record failures
5. Assign survival score

All players compete under identical constraints.

**Deliverable:**  
A repeatable tournament loop.

---

## 6. Win / Loss Evaluation Logic (Milestone M6)

Evaluation metrics include:

- Task completion correctness
- Numerical stability
- Inference latency
- VRAM usage
- Failure detection (NaN, divergence, collapse)

A composite survival score is computed.

No human judgment is allowed during evaluation.

**Deliverable:**  
Automated scoring and ranking module.

---

## 7. Statistical Validity and Iteration (Milestone M7)

To ensure significance:

- Each strategy is evaluated multiple times
- Random seeds are controlled and logged
- Results are aggregated statistically

Single-run success is insufficient.

**Deliverable:**  
Statistically meaningful survival rankings.

---

## 8. Evolutionary Loop (Milestone M8)

Surviving strategies are:

- Recombined
- Mutated
- Re-entered into competition

This loop continues until convergence or resource limits.

**Deliverable:**  
Emergent strategy families and survival clusters.

---

## 9. Measurement of Effectiveness (Milestone M9)

Final analysis includes:

- Comparison against standard quantization methods
- Resource vs capability trade-off curves
- Identification of non-intuitive survival patterns

Interpretability is optional, not required.

---

## 10. Termination Conditions

The experiment stops when one of the following occurs:

- No further improvement over N generations
- Resource limits reached
- Clear survival boundary identified

Negative results are explicitly recorded.

---

## 11. Outcome

The goal is not a new hand-designed quantization algorithm.

The goal is evidence that:

> Quantization strategies can be *discovered*, not *designed*,
> and that survivability under constraint defines intelligence limits.

This roadmap defines the transition
from theory to execution.

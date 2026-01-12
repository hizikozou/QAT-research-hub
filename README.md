# Auto-generated Quantization as Survival Strategy (QAT)

I am exploring **auto-generated quantization strategies for large language models**, treating quantization not as a post-processing trick, but as a **survival mechanism under constrained resources**.

## Motivation

Quantization research is often framed as an optimization problem:
- Reduce bit-width
- Preserve accuracy
- Follow human-designed heuristics

This project deliberately questions those assumptions.

Instead, I ask:

> *What if quantization rules themselves were generated, competed, and selected — even if humans cannot fully interpret them?*

## Core Idea

I redefine quantization as a **search and competition problem**.

- Each quantization strategy is treated as an individual
- Evaluation metrics define the environment
- Only strategies that survive under constraints remain

I do not design the strategies.  
I design **the rules of survival**.

## Research Scope

This research consists of three parallel routes:

- **QAT**: Define competition rules and extract AI survival strategies  
- **MIN**: Observe failure modes (AI boundary lines) on real hardware  
- **RCB**: Hands-on experimental hardware diary (R-Cubie series)

This repository focuses on **QAT**.

## Research Logs (Chapters)

- **QAT_DAY001** — Auto-generated quantization as a primary research target  
- **QAT_DAY002** — Initial experimental design for strategy generation  
- **QAT_DAY003** — Who decides the value? The irreducible role of humans  
- **QAT_DAY004** — Evaluation axes, competition rules, and literature map  

(Each chapter will be added under `/docs`.)

## Current Status

- Phase: Pre-experimental design
- Next: GPU-based survival experiments (RTX 5060 Ti)

## Why This Matters

Edge AI, local LLMs, and MicroAI systems face the same bottleneck:

> *If we could remove just one more layer of assumptions, the world would change.*

This research explores whether that layer is **human-designed quantization rules themselves**.

## License

To be determined.

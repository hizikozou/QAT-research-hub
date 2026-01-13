# IWR MVP (Iterative Why Robustness) — Test Template

This folder provides a minimal, reproducible template for measuring **IWR**:
> robustness of an AI system under iterative "why" questioning.

**Goal:** Provide a shared starting point so anyone can run, reproduce, and report IWR results.

## What to publish when you run
- model name / version
- decoding params (temperature, top_p, max tokens)
- max depth K
- seed prompt P0
- full transcript
- IWR depth + collapse type

## Files
- `prompts/seeds_*.txt` : seed questions
- `prompts/why_ops.md` : why-operator variants (follow-up generation rules)
- `scripts/` : pseudocode templates (runner + collapse detector)
- `results/` : place your run logs here (optional)

## Notes
- This is intentionally **simple** and **portable**.
- If you extend it, please keep backward compatibility when possible.

📄 Sheet: README / MANUAL（EN）
IWR Measurement Workbook

Iterative Why Robustness (IWR) – Manual Evaluation Template

1. Purpose

This workbook is designed to manually measure
Iterative Why Robustness (IWR) —
a metric for evaluating how long an AI system can maintain
coherent causal reasoning under repeated “why” questioning.

This template is intended for:

Initial exploratory measurements

Cross-model comparison

Failure pattern collection

Designing future automated benchmarks

2. Core Principles

1 row = 1 step

Log every Why → Answer → Why iteration

Focus on failure modes, not accuracy

IWR is not about correctness.
It measures semantic and causal stability.

3. Sheet Structure
■ Overview

Experiment metadata

Max depth K

Language

WHY template

■ Models

List of tested models

Model_ID is the primary key

■ PO_JA / PO_EN

Seed questions (P0)

Balanced across domains

■ IWR Measurement Log (Main)

Main experimental sheet

Key columns:

Model_Name / Model_ID

Seed ID

k (step index)

Why

Answer

New causal factors [Y/N]

contradiction / deviation / bankruptcy [Y/N]

Bankruptcy type (dropdown)

Notes

■ Bankruptcy type definition

Fixed failure taxonomy

Reduces evaluator drift

4. Manual Protocol

Select a model

Select a seed question (P0)

Start at k = 0

Record the answer

Ask the next “why” targeting:
premise → causation → conclusion

Stop when failure occurs

The final k is the IWR score

5. Failure Criteria

Stop the test when one clearly appears:

Evasion

Logical inconsistency

Circular reasoning

Topic drift

Policy rejection proliferation

Wording-only stagnation

If uncertain, document in Notes.

6. Notes

Do not aim for perfection

10 seeds × a few models is enough initially

Manual friction reveals design insights

7. License & Use

This template is part of
Evolutionary Discovery Engineering (EDiE) research.

Reuse, modification, and derivative work are welcome.
Attribution is appreciated

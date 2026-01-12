# QAT_DAY001: Auto-generated Quantization as a Primary Research Target

## Abstract

Quantization in large language models is typically treated as a secondary optimization step.
This research deliberately reframes quantization as a **primary research target**,
not a post-processing technique.
By removing human-designed assumptions from quantization rules,
I explore whether entirely new performance boundaries can be discovered.

## 1. Background

Most existing quantization research focuses on a familiar objective:

- Reduce bit-width
- Preserve accuracy
- Minimize performance degradation
- Follow interpretable, human-designed heuristics

These approaches have produced strong results,
but they also share an implicit assumption:

> Quantization rules must be understandable and manually designed by humans.

This assumption has rarely been questioned.

## 2. Problem Redefinition

In this research, I redefine quantization as follows:

> Quantization is not a compression technique.  
> It is a **structural constraint imposed on intelligence**.

From this perspective, quantization determines
which internal representations are allowed to survive
under limited computational resources.

Therefore, quantization should not be optimized *after* a model is designed.
It should be studied as a first-class research object.

## 3. Core Hypothesis

I propose the following hypotheses:

**H1**  
If quantization rules are treated as a search space,
there exist strategies that outperform existing human-designed schemes.

**H2**  
Such strategies do not need to be human-interpretable.

**H3**  
Performance boundaries can be shifted
without modifying model architecture or training data,
purely by altering quantization survival rules.

## 4. Research Positioning

This research intersects multiple domains:

- Quantization-aware training
- Neural architecture search
- Edge AI and local inference
- Automated system design

However, it differs in one critical aspect:

I do not search for better models.  
I search for **better survival rules**.

## 5. What Comes Next

The next step is to formalize quantization strategies
as individuals in a competitive environment.

In QAT_DAY002,
I describe the initial design for generating,
mutating, and evaluating quantization strategies automatically.

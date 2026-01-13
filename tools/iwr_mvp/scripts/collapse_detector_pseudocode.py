"""
Collapse detector pseudocode.
Start with simple heuristics; later replace with a learned evaluator.
"""

import re
from typing import Dict, Any, List

AVOID_PATTERNS = [
    r"わかりません", r"不明", r"断定できません",
    r"I don't know", r"cannot answer", r"as an AI",
]
LOOP_PATTERNS = [
    r"つまり", r"in other words", r"要するに",
]

def detect_collapse(history: List[Dict[str, str]]) -> Dict[str, Any]:
    last = history[-1]["content"]

    # Heuristic 1: explicit evasion / refusal
    for p in AVOID_PATTERNS:
        if re.search(p, last, flags=re.IGNORECASE):
            return {"collapsed": True, "type": "evasion_or_refusal"}

    # Heuristic 2: too short / non-answer (tune thresholds later)
    if len(last.strip()) < 20:
        return {"collapsed": True, "type": "non_answer_short"}

    # Heuristic 3: repetition detector (placeholder)
    # TODO: compute similarity to previous answers

    return {"collapsed": False, "type": ""}

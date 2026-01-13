"""
IWR runner pseudocode (minimal).
Replace `call_model()` with your local model / API client.
"""

from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class RunConfig:
    model_id: str
    temperature: float
    top_p: float
    max_tokens: int
    max_depth_k: int
    why_operator_id: str
    language: str

def call_model(history: List[Dict[str, str]], cfg: RunConfig) -> str:
    # TODO: implement for your runtime (local llm / API / edge device)
    raise NotImplementedError

def make_why_question(prev_answer: str, op_id: str, lang: str) -> str:
    # Minimal placeholder: implement per why_ops.md
    if lang == "JA":
        return f"それはなぜ？（前の回答の根拠を、もう一段因果で説明して）"
    return "Why? Please explain one level deeper causally."

def detect_collapse(history: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Return: {"collapsed": bool, "type": str}
    Placeholder: plug in heuristics or an evaluator model.
    """
    return {"collapsed": False, "type": ""}

def run_iwr(seed_prompt: str, cfg: RunConfig) -> Dict[str, Any]:
    history = [{"role": "user", "content": seed_prompt}]
    depth = 0
    collapse_info = {"collapsed": False, "type": ""}

    for k in range(1, cfg.max_depth_k + 1):
        answer = call_model(history, cfg)
        history.append({"role": "assistant", "content": answer})

        collapse_info = detect_collapse(history)
        if collapse_info["collapsed"]:
            break

        why_q = make_why_question(answer, cfg.why_operator_id, cfg.language)
        history.append({"role": "user", "content": why_q})
        depth = k

    return {
        "seed_prompt": seed_prompt,
        "iwr_depth": depth,
        "max_depth_k": cfg.max_depth_k,
        "collapse": collapse_info,
        "history": history,
        "config": cfg.__dict__,
    }

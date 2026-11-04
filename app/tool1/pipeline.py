"""Tool 1 pipeline, option A (DECISIONS.md F1 row 1): judge the draft, rewrite from the scores, judge the rewrite.

The app calls run() for a new draft and rescore() after the writer fills in placeholders.
"""
from dataclasses import dataclass

from app.tool1.judge import JudgeResult, judge
from app.tool1.llm import LLM
from app.tool1.rewriter import RewriteResult, rewrite


@dataclass
class PipelineResult:
    before: JudgeResult
    rewrite: RewriteResult | None
    after: JudgeResult | None


def run(draft: str, message_type: str, llm: LLM | None = None) -> PipelineResult:
    llm = llm or LLM()
    before = judge(draft, message_type, llm=llm)
    if before.abstain:
        return PipelineResult(before, None, None)
    rw = rewrite(draft, before, llm=llm)
    after = judge(rw.rewrite, message_type, llm=llm) if rw.changes else before
    return PipelineResult(before, rw, after)


def rescore(text: str, message_type: str, llm: LLM | None = None) -> JudgeResult:
    """Scores the writer's filled-in version with the same judge (v1.1 pending rule)."""
    return judge(text, message_type, llm=llm or LLM())

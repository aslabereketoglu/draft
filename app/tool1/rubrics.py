"""Loads the approved rubric files and holds the label rules from their "Rule for the label" sections.

The rubric markdown in docs/rubric is the single source of truth for what the judge reads.
The label rule is applied here in Python, so the label never depends on the model doing arithmetic.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

RUBRIC_DIR = Path(__file__).resolve().parent / "rubrics"


@dataclass(frozen=True)
class Rubric:
    message_type: str
    rubric_id: str
    file_name: str
    dimensions: tuple[str, ...]

    def text(self) -> str:
        return (RUBRIC_DIR / self.file_name).read_text(encoding="utf-8")


TASK_INSTRUCTION = Rubric(
    message_type="task_instruction",
    rubric_id="task_instruction_v1.1",
    file_name="rubric_task_instruction.md",
    dimensions=("D1_outcome_specificity", "D2_time_frame", "D3_rationale", "D4_how_to", "D5_progress_check"),
)

PERFORMANCE_FEEDBACK = Rubric(
    message_type="performance_feedback",
    rubric_id="performance_feedback_v1.1",
    file_name="rubric_performance_feedback.md",
    dimensions=("F1_task_focus", "F2_specificity", "F3_progress_vs_standard", "F4_next_step", "F5_no_self_threat"),
)

RUBRICS = {r.message_type: r for r in (TASK_INSTRUCTION, PERFORMANCE_FEEDBACK)}


def label_task_instruction(scores: dict[str, int | None]) -> str:
    """Rule for the label, rubric_task_instruction.md v1.1. Null scores (not assessable) are left out."""
    applicable = {k: v for k, v in scores.items() if v is not None}
    d1, d2 = scores.get("D1_outcome_specificity"), scores.get("D2_time_frame")
    low = sum(1 for v in applicable.values() if v <= 2)
    if (d1 is not None and d1 <= 2) or low >= 2:
        return "needs_work"
    mean = sum(applicable.values()) / len(applicable) if applicable else 0
    if (d1 is not None and d1 >= 4 and d2 is not None and d2 >= 3
            and min(applicable.values()) > 1 and mean >= 3.5):
        return "good"
    return "borderline"


def label_performance_feedback(scores: dict[str, int | None]) -> str:
    """Rule for the label, rubric_performance_feedback.md v1.1."""
    f1, f2, f3, f4, f5 = (scores.get(k) for k in PERFORMANCE_FEEDBACK.dimensions)
    if any(v is None for v in (f1, f2, f3, f4, f5)):
        return "borderline"
    if f1 <= 2 or f5 <= 2 or (f2 <= 2 and f4 <= 2):
        return "needs_work"
    mean = (f1 + f2 + f3 + f4 + f5) / 5
    if f1 >= 4 and f5 >= 4 and f2 >= 3 and f4 >= 3 and mean >= 3.5:
        return "good"
    return "borderline"


LABEL_RULES = {
    "task_instruction": label_task_instruction,
    "performance_feedback": label_performance_feedback,
}

"""Offline tests: label rules and output checks. No model call is made."""
from app.tool1.judge import check_and_label
from app.tool1.rubrics import PERFORMANCE_FEEDBACK, TASK_INSTRUCTION, label_performance_feedback, label_task_instruction

D = TASK_INSTRUCTION.dimensions
F = PERFORMANCE_FEEDBACK.dimensions


def ti(d1, d2, d3, d4, d5):
    return dict(zip(D, (d1, d2, d3, d4, d5)))


def pf(*s):
    return dict(zip(F, s))


def test_task_good():
    assert label_task_instruction(ti(4, 3, 4, None, 4)) == "good"


def test_task_gate_d1():
    assert label_task_instruction(ti(2, 5, 5, None, 5)) == "needs_work"


def test_task_two_low():
    assert label_task_instruction(ti(4, 4, 2, None, 2)) == "needs_work"


def test_task_any_one_blocks_good():
    assert label_task_instruction(ti(5, 5, 5, None, 1)) == "borderline"


def test_task_d4_null_left_out_of_mean():
    assert label_task_instruction(ti(4, 3, 3, None, 3)) == "borderline"  # mean 3.25 over four dimensions
    assert label_task_instruction(ti(4, 3, 3, None, 4)) == "good"        # mean exactly 3.5


def test_feedback_good():
    assert label_performance_feedback(pf(4, 3, 3, 3, 5)) == "good"


def test_feedback_gate_f5():
    assert label_performance_feedback(pf(5, 5, 5, 5, 2)) == "needs_work"


def test_feedback_f2_and_f4_low():
    assert label_performance_feedback(pf(4, 2, 5, 2, 5)) == "needs_work"


def _raw(rubric, statuses_scores, evidence=None, confidence="high"):
    evidence = evidence or {}
    return {
        "rubric_id": rubric.rubric_id,
        "in_scope": True,
        "abstain": {"value": False, "reason": None},
        "scores": {k: {"status": st, "evidence": evidence.get(k, []), "note": "", "score": sc}
                   for k, (st, sc) in zip(rubric.dimensions, statuses_scores)},
        "label": "good",
        "confidence": {"level": confidence, "note": ""},
    }


DRAFT = "pls send the vendor list as a CSV by [due date?] for the audit"


def test_pending_label_and_placeholder():
    raw = _raw(TASK_INSTRUCTION,
               [("scored", 4), ("pending", None), ("scored", 4), ("not_assessable", None), ("scored", 3)],
               evidence={D[1]: ["[due date?]"]})
    r = check_and_label(TASK_INSTRUCTION, DRAFT, raw)
    assert r.label == "pending"
    assert r.warnings == []


def test_low_confidence_is_borderline():
    raw = _raw(TASK_INSTRUCTION, [("scored", 5)] * 5, confidence="low")
    assert check_and_label(TASK_INSTRUCTION, DRAFT, raw).label == "borderline"


def test_evidence_must_be_in_message():
    raw = _raw(TASK_INSTRUCTION, [("scored", 4)] * 5, evidence={D[0]: ["send the vendor list by Friday"]})
    r = check_and_label(TASK_INSTRUCTION, DRAFT, raw)
    assert any("evidence not found" in w for w in r.warnings)


def test_abstain_has_no_label():
    raw = _raw(TASK_INSTRUCTION, [("not_assessable", None)] * 5)
    raw["in_scope"] = False
    r = check_and_label(TASK_INSTRUCTION, DRAFT, raw)
    assert r.abstain and r.label is None


def test_model_label_is_not_trusted():
    raw = _raw(TASK_INSTRUCTION, [("scored", 1)] * 5)  # model wrote "good"
    r = check_and_label(TASK_INSTRUCTION, DRAFT, raw)
    assert r.label == "needs_work" and r.model_label == "good"

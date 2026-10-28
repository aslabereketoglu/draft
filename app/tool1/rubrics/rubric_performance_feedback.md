# Rubric draft for performance feedback messages (Tool 1)

Version 1.1, 2026-10-17. Approved by the team on 2026-10-17 (DECISIONS.md E1). v1.0 was approved as final on 2026-10-16 with the content of v0.3.

Change from v1.0. Added a pending status for dimensions whose only evidence is a writer placeholder such as "[due date?]", a pending label, and a `status` field per dimension in the output (DECISIONS.md F1 row 3a). Dimensions, descriptors, anchors, and cutoffs are unchanged. All additions are team judgment.

Change from v0.2. Every dimension now has a written descriptor and one illustrative anchor for each of the five levels. The level 2 and level 4 descriptors are new. One item moved down a level to fit the ladder. A message that implies a standard without stating it is now F3 level 2. The judge now quotes evidence before giving each score, and the output format lists evidence, then note, then score. All of these changes are team judgment. The label rule is unchanged.

Change from v0.1 to v0.2. Hattie and Timperley (2007, formerly S4) and Shute (2008, formerly S5) were removed. The team ruled out S4 as classroom research, and S5 fails the evidence rule recorded in DECISIONS.md D1 (education review). Three workplace studies were added as S6, S7, and S8. Every element that rested on S4 or S5 was rebased or relabeled as team judgment. The removed sources and the elements that cited them are listed in `sources_verification.md` under "Removed sources".

## How to read this file

Every element carries a provenance tag. A tag such as [S3 p.273] means the element traces to source S3 at printed page 273. The full reference, DOI, exact location, and access status for every tag are in `sources_verification.md`. A tag of **Team judgment** means no source supplies the element. A tag of **Illustrative** marks an example message written for this draft. Illustrative messages are not research data and must not be reused in the evaluation set.

## Why this message type

Performance feedback rests on a large research body that I could open in full. The feedback meta-analysis pools results from a large set of papers [S3 p.258]. Workplace studies of supervisor feedback add evidence on specificity [S6], positive feedback [S7], and forward-looking developmental feedback [S8]. **Team judgment.** The type also bears on the Q12 items about progress and development. The team has limited Tool 1 to task instructions and performance feedback for now (DECISIONS.md C1, row 1).

## Scope

**Team judgment.** The rubric scores a written message (email or chat) from a manager or lead to an employee about a specific piece of work or a recent stretch of performance. It does not cover formal annual reviews, disciplinary notices, or pure thank-you notes. A message that only thanks or praises the person, with no reference to the work, is out of scope and triggers abstention.

**Caution on transfer.** S3 pools studies from many settings, including workplace tasks, and frames its question around what a teacher, manager, or other agent can expect from feedback [S3 p.255]. It is labeled Mixed under the evidence rule (DECISIONS.md D1). S6, S7, and S8 are workplace surveys that measure how employees perceive their supervisor's feedback in general [S6 p.4; S7 p.4; S8 p.6]. None of the sources scores the text of a single written message. Applying their findings to written workplace feedback is a translation that the team has to validate in the pilot. The translation itself is team judgment.

## Scale

**Team judgment.** No source supplies a scale for scoring messages. Each dimension is scored 1 to 5, with a written descriptor and one illustrative anchor for every level. The descriptors for levels 2 and 4 were added in v0.3. Each anchor differs from the one above it by one feature where possible. The pilot tests whether human raters and the LLM judge agree on each level. The five-level wording is the team's design and is not a research finding.

## Dimensions

### F1. Task focus

**Definition.** The feedback addresses the work and how it was done, and does not characterize the person. [S3 p.275]

**Basis.** In S3's moderator analysis, the lower in the attention hierarchy the feedback directs attention (toward the task and away from the self), the stronger its benefit for performance [S3 p.275]. S3 concludes that feedback on a familiar task that keeps attention on the task and carries no cues directing attention to the self is likely to yield large gains [S3 p.278].

**On praise.** In S3, effects on performance were weaker when the feedback included praise than when it did not [S3 p.273, Table 2]. In a workplace study, employees who reported that their supervisor lets them know when they do good work received higher supervisor-rated performance four weeks later [S7 pp.4–5]. **Team judgment.** The rubric therefore scores person-level praise ("you're a rockstar") as self-focused, and scores praise that names what was done well as task-focused. No source tests this split directly. This tension with the recognition item Q04 is noted below and in `not_verified.md`.

**Boundary (Team judgment).** F1 asks what the feedback is about. Discouraging, threatening, or comparative wording belongs to F5.

**Scale descriptors (Team judgment, paraphrasing S3 pp.275 and 278).**
- **5.** Every evaluative statement refers to the work, its parts, or the way it was done.
- **4.** The feedback is about the work, with one passing remark about the person that does not carry the message.
- **3.** The feedback is mostly about the work but includes some statements about the person (positive or negative).
- **2.** The feedback is mainly about the person, with one vague reference to the work.
- **1.** The feedback is about the person ("you're careless", "you're a natural") with little or no reference to the work.

**Anchors (Illustrative).**
- 5. "The exec summary on p1 nails the cost driver. Keep that structure for the Q4 version."
- 4. "The exec summary on p1 nails the cost driver, ur a natural. Keep that structure for the Q4 version."
- 3. "Ur a natural at this honestly. Exec summary nails the cost driver."
- 2. "Ur a natural at this honestly, one of our best. Summary looked good."
- 1. "Honestly you're just not a detail person, which is why stuff like this keeps happening."

**Q12 link.** None asserted. See the note on Q04 below.

### F2. Specificity

**Definition.** The feedback identifies which part of the work it refers to and what specifically is right or needs to change. [S6 pp.4, 7]

**Basis.** In a workplace survey, employees who rated their appraisal feedback as more specific were more likely to accept it as accurate, and acceptance was in turn linked to job satisfaction [S6 p.6, Table 1; p.7, Figure 3]. S6 recommends that managers give clear information about deficiencies and how to remedy them [S6 p.7]. S6 measures specificity with items that include information on how to correct deficiencies [S6 p.4], so its construct overlaps F4.

**Where sources disagree or qualify.** S3 states that the evidence on specificity is not clear, and that feedback that is too specific can direct attention below the level needed for performance [S3 p.268]. S6 is cross-sectional and self-reported, and it links specificity to acceptance and satisfaction, not to performance [S6 p.8]. **Team judgment.** The scale rewards pinpointing the issue. It does not reward the amount of detail, and a long message is never scored higher for its length. With S5 removed, the rule against rewarding length has no source and rests on team judgment alone.

**Boundary (Team judgment).** Saying what to do next belongs to F4. Naming the goal or standard belongs to F3.

**Scale descriptors (Team judgment, paraphrasing S6 p.4 and S3 p.268).**
- **5.** The feedback names the specific part of the work and the specific issue or strength, briefly.
- **4.** The feedback names the specific issue, but its location in the work is only approximate.
- **3.** The feedback names the area ("the slides", "the numbers") but not the specific issue.
- **2.** The feedback names the piece of work only, with a general verdict ("the deck looks a bit off").
- **1.** The feedback is general ("needs work", "looks good") and points to nothing in the work.

**Anchors (Illustrative).**
- 5. "Slide 4 churn # is from Q2 data, swap in Q3 from the dashboard."
- 4. "The churn # in the deck is from Q2 data, swap in Q3 from the dashboard."
- 3. "The churn numbers in the deck look off."
- 2. "The deck looks a bit off."
- 1. "Overall I think there's a lot going on and it could be tighter in places, some parts felt a bit off and the flow wasn't quite there yet, so maybe take another pass when you get a chance and make it stronger overall."

**Q12 link.** None asserted.

### F3. Progress against a goal or standard

**Definition.** The feedback relates the work to a goal, standard, or earlier performance, so the reader can see where they stand. [S1 p.708; S3 p.273]

**Basis.** S1 states that people need summary feedback showing progress toward their goals, and that without it they cannot adjust their effort or strategy [S1 p.708]. In S3, feedback about change from previous performance (velocity feedback) had a larger effect on performance than feedback without it [S3 p.273, Table 2]. S3 also proposes that a stated goal helps most when the feedback alone is hard to interpret [S3 p.269, Proposition 4].

**Boundary (Team judgment).** F3 is about where the work stands. What to do next belongs to F4.

**Scale descriptors (Team judgment, paraphrasing S1 p.708 and S3 p.273).**
- **5.** The feedback states the goal or standard, where the work stands against it, and how it changed from earlier performance.
- **4.** The feedback states the goal or standard and where the work stands, or where it stands and how it changed from before, but not all three.
- **3.** The feedback states the current result only, with no standard or comparison.
- **2.** The feedback implies a standard ("not quite there") without stating it.
- **1.** No reference to any goal, standard, or earlier performance.

**Anchors (Illustrative).**
- 5. "Target is under 2% pick errors. You were at 3.1% last month and 2.4% this month, so moving the right way."
- 4. "Target is under 2% pick errors. You were at 2.4% this month."
- 3. "You were at 2.4% pick errors this month."
- 2. "Pick errors still not quite where they need to be this month."
- 1. "Numbers are kinda meh this month tbh."

**Q12 link.** Q11, someone at work talking about progress. The basis is overlap in wording between S1's description of feedback showing progress toward goals [S1 p.708] and the Q11 item [G1]. No source names Q12, so the mapping is **Team judgment**.

### F4. Next step

**Definition.** The feedback says what to do next or how to improve, or gives the correct version. [S3 p.273; S8 p.3]

**Basis.** In S3, feedback that supplied the correct solution had a larger effect on performance than feedback that did not [S3 p.273, Table 2], and S3 argues that feedback helps learning when it points to what is wrong and how to fix it [S3 p.268]. In a workplace study, supervisor developmental feedback, defined as forward-looking information meant to help the employee learn, develop, and improve on the job, was linked to higher supervisor-rated creativity [S8 p.3; p.9]. S8 takes this definition from Zhou (2003), which I did not open. S8's outcome is creativity, not task performance.

**Boundary (Team judgment).** F4 covers forward-looking guidance. Identifying the current issue belongs to F2.

**Scale descriptors (Team judgment, paraphrasing S3 pp.268 and 273 and S8 p.3).**
- **5.** A concrete next action or corrected version is given.
- **4.** A concrete action is given, with one detail left for the reader to work out.
- **3.** A direction is given without a concrete action ("tighten it up", "be more careful with the numbers").
- **2.** The feedback points to what must change without saying how.
- **1.** No next step. The feedback only judges the work.

**Anchors (Illustrative).**
- 5. "For the next one, put the assumptions table before the forecast so finance sees the inputs first."
- 4. "For the next one, move the assumptions table up."
- 3. "For the next one, make the inputs easier to find."
- 2. "The forecast section needs another pass before the next one."
- 1. "This isn't right. Fix it."

**Q12 link.** Q06 (encouragement of development) and Q12 (opportunities to learn and grow). The basis is overlap in wording between S8's definition of developmental feedback as helping employees learn, develop, and improve [S8 p.3] and those items [G1]. No source names Q12, so the mapping is **Team judgment**.

### F5. Absence of discouraging or self-threatening cues

**Definition.** The feedback avoids wording that discourages the reader, threatens their self-esteem, or compares them unfavorably with coworkers. A high score means these cues are absent. [S3 p.267; S3 p.273]

**Basis.** S3 proposes that cues directing attention to the self, such as normative comparisons, messages designed to discourage, and any cue perceived as a threat to the self, weaken the effect of feedback on performance [S3 p.267]. In S3's results, feedback designed to discourage had a negative effect on performance, while other feedback had a positive one, and feedback high in threat to self-esteem had a much smaller effect than feedback low in threat [S3 p.273, Table 2].

**On comparison with coworkers.** S3 predicted that normative feedback would weaken effects but found the moderator nonsignificant [S3 p.274]. **Team judgment.** The rubric treats comparison with coworkers as a marker that lowers F5, with less weight than discouraging or self-threatening wording. With S5 removed, no remaining source supports penalizing comparisons, so this weighting is team judgment only.

**Boundary (Team judgment).** F5 covers discouraging, threatening, or comparative wording. Whether feedback is about the task or the person belongs to F1. A message can be task-focused and still score low on F5 ("this report is a disaster").

**Scale descriptors (Team judgment, paraphrasing S3 pp.267 and 273).**
- **5.** No discouraging, threatening, or comparative wording.
- **4.** One mild frustration marker that is not aimed at the person ("ugh").
- **3.** One mild comparative or discouraging phrase in otherwise neutral feedback.
- **2.** Discouraging wording aimed at the person, alongside some task content.
- **1.** Clearly discouraging or threatening wording, or an unfavorable comparison with coworkers that carries the message.

**Anchors (Illustrative).**
- 5. "Two calc errors in the variance tab, both quick fixes, details below."
- 4. "Ugh, two calc errors in the variance tab, both quick fixes, details below."
- 3. "Two calc errors in the variance tab again, not great. Details below."
- 2. "Two calc errors in the variance tab again. Not sure you're cut out for the variance work. Details below."
- 1. "Everyone else on the team got this right the first time. Not sure what happened with you on this one."

**Q12 link.** None asserted.

## Note on Q04 (recognition)

The Gallup Q04 item concerns recognition or praise for good work [G1]. In S3, feedback that included praise had a smaller effect on performance than feedback that did not [S3 p.273, Table 2]. In a workplace study, perceived positive supervisor feedback predicted higher supervisor-rated performance [S7 p.5]. **Team judgment.** S3's praise moderator and S7's positive feedback are measured differently, so the two do not directly contradict each other. The rubric does not penalize task-specific praise. Whether a separate recognition rubric is needed is a question for the team.

## Elements considered and left out

The reasons are in `not_verified.md`. In brief, feedback frequency may be an artifact in S3 [S3 p.274], and oral versus written delivery [S3 p.273] is a property of the channel. Feedback timing is left out as **Team judgment**, because a single written message does not show its timing. With S5 removed, no remaining source is cited for the timing evidence.

## Rule for the label

**Team judgment, untested.** No source supplies cutoffs. The rule is a starting point for the pilot.

1. Score all five dimensions on every in-scope message.
2. **Good** requires F1 of 4 or more, F5 of 4 or more, F2 of 3 or more, F4 of 3 or more, and a mean of 3.5 or more.
3. **Needs work** applies when F1 is 2 or less, when F5 is 2 or less, or when both F2 and F4 are 2 or less.
4. **Borderline** covers every other case. It also applies when the judge's confidence is low, whatever the scores.
5. F1 and F5 are gated because S3 reports its largest contrasts for self-directed, discouraging, and threatening cues [S3 p.273]. The choice to gate them is still team judgment.
6. **Pending** applies when any dimension is pending. Once the writer fills in every placeholder, the message is scored again and the normal label rule applies. **Team judgment.**

## Abstention

**Team judgment.** The judge abstains and gives a reason in any of these cases.
- The message contains no evaluation of any work (for example, logistics only).
- The message only thanks or praises the person and refers to no work (out of scope).
- The message has fewer than about 8 words.

## Judge instructions

**Team judgment.**
- For each dimension, quote the evidence first, then write the note, then give the score. If there is no evidence, say so before scoring.
- Quote evidence as exact substrings of the message, each 15 words or fewer.
- Typos, informal tone, emoji, and length do not raise or lower any score.
- Positive and negative feedback are scored on the same dimensions. Neither tone earns points on its own.
- Score only what is in the message. Do not assume context the message does not contain.
- If a dimension's only evidence is a marked placeholder in square brackets ending in a question mark, such as "[due date?]", quote the placeholder, set the status to pending, and give no score.

## Judge output format

**Team judgment.** Each dimension carries a `status` of "scored", "not_assessable", or "pending". A pending dimension has a null score and quotes its placeholder as evidence. The `label` is one of "good", "borderline", "needs_work", or "pending".

```json
{
  "rubric_id": "performance_feedback_v1.1",
  "in_scope": true,
  "abstain": {"value": false, "reason": null},
  "scores": {
    "F1_task_focus": {"status": "scored", "evidence": ["you're just not a detail person"], "note": "person-level judgment", "score": 2},
    "F2_specificity": {"status": "scored", "evidence": ["stuff like this"], "note": "issue not named", "score": 1},
    "F3_progress_vs_standard": {"status": "scored", "evidence": [], "note": "no evidence; no standard referenced", "score": 1},
    "F4_next_step": {"status": "scored", "evidence": [], "note": "no evidence; no action given", "score": 1},
    "F5_no_self_threat": {"status": "scored", "evidence": ["keeps happening"], "note": "discouraging wording aimed at the person", "score": 2}
  },
  "label": "needs_work",
  "confidence": {"level": "high", "note": "short but unambiguous"}
}
```

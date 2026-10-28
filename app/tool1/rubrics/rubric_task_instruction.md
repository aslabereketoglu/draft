# Rubric draft for task instruction messages (Tool 1)

Version 1.1, 2026-10-17. Approved by the team on 2026-10-17 (DECISIONS.md E1). v1.0 was approved as final on 2026-10-16 with the content of v0.3.

Change from v1.0. Added a pending status for dimensions whose only evidence is a writer placeholder such as "[due date?]", a pending label, and a `status` field per dimension in the output (DECISIONS.md F1 row 3a). Dimensions, descriptors, anchors, and cutoffs are unchanged. All additions are team judgment.

Change from v0.2. Every dimension now has a written descriptor and one illustrative anchor for each of the five levels. The level 2 and level 4 descriptors are new. Three items moved down a level to fit the ladder. "Asap" with no window is now D2 level 2, a reason that only asserts importance is now D3 level 2, and "keep me posted" with no time is now D5 level 2. D3 rule 4 changed to match. The judge now quotes evidence before giving each score, and the output format lists evidence, then note, then score. All of these changes are team judgment. The label rule is unchanged.

Change from v0.1 to v0.2. D3 now follows stricter scoring rules and rests on Colquitt et al. (2001, S9) in place of the Latham, Erez, and Locke (1988) finding reported in S1, which the team ruled out as a lab study (DECISIONS.md C1, rows 3 and 4). D3 now states that no source shows a performance benefit, citing S10 and S11. The D1 boundary gained one sentence and one anchor. The label rule and output format are unchanged apart from the version id.

## How to read this file

Every element carries a provenance tag. A tag such as [S1 p.706] means the element traces to source S1 at printed page 706. The full reference, DOI, exact location, and access status for every tag are in `sources_verification.md`. A tag of **Team judgment** means no source supplies the element. A tag of **Illustrative** marks an example message written for this draft. Illustrative messages are not research data and must not be reused in the evaluation set.

## Why this message type

I chose task instructions and performance feedback because both rest on large research bodies that I could open in full. The goal-setting review summarizes 35 years of studies [S1 p.705], and the feedback meta-analysis pools a large set of studies [S3 p.258]. **Team judgment.** Both also bear on the Q12 items about expectations and progress. I also considered recognition messages, project and shift handoffs, change announcements, meeting follow-ups, and requests for input, and set them aside because I did not open adequate research on them within this task.

## Scope

**Team judgment.** The rubric scores a written message (email or chat) in which a manager or lead assigns a piece of work to one person or a small team. It does not cover feedback on finished work (see `rubric_performance_feedback.md`), policy announcements, or messages to customers.

**Caution on transfer.** S1 studies the properties of goals and their effect on performance, and S2 studies how employees perceive their leader's language. Neither source scores the text of written messages. S2 describes motivating language as a set of oral communication dimensions [S2 p.126]. Scoring a written message on these properties is therefore a translation that the team has to validate in the pilot. The translation itself is team judgment.

## Scale

**Team judgment.** No source supplies a scale for scoring messages. Each dimension is scored 1 to 5, with a written descriptor and one illustrative anchor for every level. The descriptors for levels 2 and 4 were added in v0.3. Each anchor differs from the one above it by one feature where possible. The pilot tests whether human raters and the LLM judge agree on each level. The five-level wording is the team's design and is not a research finding. A dimension may be marked not assessable where its applicability rule says so.

## Dimensions

### D1. Outcome specificity

**Definition.** The message states what is to be produced or achieved concretely enough that the reader could tell when the work is done. [S1 p.706; S2 p.126]

**Basis.** S1 reports that do-your-best goals have no external referent, so each person defines them differently, and that a specified goal reduces ambiguity about what is to be attained [S1 p.706]. S1 also states that specificity alone does not guarantee high performance, because specific goals vary in difficulty [S1 p.706]. **Team judgment.** The rubric therefore treats specificity as reducing ambiguity and makes no claim that it raises performance on its own. S2 describes direction-giving language as reducing ambiguity by explaining what needs to be done [S2 p.126]. In S10, specific group goals outperformed nonspecific goals, and field studies showed the same pattern, with no significant difference between lab and field [S10 p.1294, Table 2; p.1295, Table 3; p.1293]. S10 studies goals set for groups, not instructions to one person.

**Boundary (Team judgment).** Deadlines belong to D2, reasons to D3, and methods to D4. A completion condition stays in D1 even when it sits in the same sentence as a reason, for example "so the totals have to tie to the ledger".

**Scale descriptors.** Wording is team judgment that paraphrases the constructs in S1 p.706 and S2 p.126.
- **5.** The deliverable or result is named, with enough detail (format, scope, quantity, or acceptance condition) that no clarifying question is needed about what counts as done.
- **4.** The deliverable is named, and one minor feature is unstated that the reader could reasonably infer.
- **3.** The deliverable is named, but one important feature is vague or missing, so the reader would likely need to ask one question.
- **2.** The object of the work is named, but not the output wanted.
- **1.** The request is general ("look into", "do what you can", "make it better") and the reader cannot tell what result is expected.

**Anchors (Illustrative).**
- 5. "pls send me the cleaned vendor list as a CSV, one row per vendor, dupes removed"
- 5, completion condition. "The totals have to tie to the ledger before you send it."
- 4. "pls send me the cleaned vendor list as a CSV, one row per vendor"
- 3. "pls send me the cleaned vendor list as a CSV"
- 2. "can u clean up the vendor list when u get a sec"
- 1. "Hi! Can you take a look at the vendor stuff when you get a sec and just do what you can with it, try to get it in better shape than it is now. Thanks so much!!"

**Q12 link.** Q01, knowing what is expected at work. The basis is overlap in wording between S2's description of direction-giving language answering what an employee is supposed to do [S2 p.126] and the Q01 item [G1]. No source names Q12, so the mapping is **Team judgment**.

### D2. Time frame

**Definition.** The message states when the work is due, or gives a time frame the reader can act on. [S1 p.705; S2 p.126]

**Basis.** S1 defines a goal as an aim, typically a standard to be reached within a specified time limit [S1 p.705]. S1 reports that tight deadlines produced a faster work pace than loose deadlines in laboratory and field studies [S1 p.707]. S2 lists when as part of what direction-giving messages explain [S2 p.126]. S2 also states that clarifying goals and time guidelines reduces uncertainty, citing Mayfield and Mayfield (2016), which I did not open [S2 p.127]. In S11, a field study, a letter stating a non-binding target date reduced submissions in the last weeks before a deadline [S11 p.7, Table 2]. S11 measures timing only, not the quality of the work.

**Caution.** S1 links deadline tightness to work pace only. The rubric rewards a clear time frame and does not reward tightness. **Team judgment.**

**Boundary (Team judgment).** Check-in points before the deadline belong to D5.

**Scale descriptors (Team judgment, paraphrasing S1 p.705 and S2 p.126).**
- **5.** A specific due date and time is given (for example "Thu 3pm" or "end of day Friday ET").
- **4.** A specific day is given with no time.
- **3.** A rough time frame is given ("this week", "early next week") that the reader can plan around but may need to confirm.
- **2.** An urgency cue is given with no window ("asap", "soon").
- **1.** No time frame, or one that cannot be acted on ("whenever", "no rush").

**Anchors (Illustrative).**
- 5. "Need it by Thurs 3pm so it makes the budget deck."
- 4. "Need it by Thurs so it makes the budget deck."
- 3. "Need it sometime this week so it makes the budget deck."
- 2. "Need it asap so it makes the budget deck."
- 1. "whenever you get a chance, no rush, but sooner is prob better I guess"

**Q12 link.** Q01, on the same basis and with the same Team judgment label as D1.

### D3. Rationale

**Definition.** The message states the purpose the work serves, meaning what it feeds into, who will use it, or what depends on it. [S9 p.436, Table 5; S2 p.126] The page where S9 defines informational justice was not recorded, so the S9 locator points to its results table and is unverified as a definition source.

**Basis.** S9 treats explanations given to people as informational justice. Across its pooled studies, informational justice is linked to trust in the person giving the explanation and to how that person is evaluated [S9 p.436, Table 5]. S2 describes a related dimension, meaning-making language, which answers why the work is important [S2 p.126]. **Team judgment.** D3 is therefore grounded in trust and in how the reader judges the manager.

**What the evidence does not show.** No source shows that giving a reason raises task performance. In S9 the link from informational justice to performance is weak and not reliable [S9 p.436, Table 5], and S9 pools lab and field studies [S9 p.431]. In S10, group goals assigned with a rationale did no better than goals assigned without one [S10 p.1294, Table 2], and the authors note that almost all of the no-rationale comparisons came from lab studies [S10 p.1295]. In S11, a letter telling people the benefit of submitting early did not change when they submitted [S11 p.7, Table 2]. The rubric makes no claim that D3 improves performance.

**Scoring rules (Team judgment).**
1. D3 scores only the purpose clause, meaning what the work feeds into, who uses it, or what depends on it.
2. When the same sentence also states a completion condition, that part goes to D1. A stated time goes to D2.
3. D3 evidence may not repeat D1 evidence. When one sentence carries both, the judge splits it and quotes only the purpose part for D3.
4. A reason that names no specific use or dependency scores 3 at most ("for the meeting", "leadership wants it"). A reason that only asserts importance ("it's important") scores 2.

**Boundary (Team judgment).** D3 concerns why the task matters. What counts as done belongs to D1, and how to do it belongs to D4.

**Scale descriptors (Team judgment, paraphrasing S9 p.436 and S2 p.126).**
- **5.** A concrete use is given, plus who relies on the work or what depends on it.
- **4.** A concrete use is given, with no mention of who relies on it or what depends on it.
- **3.** A generic use is given ("for the meeting", "leadership wants it") with no indication of what depends on it.
- **2.** Importance is asserted with no use named ("it's important", "pls prioritize").
- **1.** No reason is given, or the message refuses one ("just do it the way I said").

**Anchors (Illustrative).**
- 5. "This feeds Monday's audit for the finance team."
- 4. "This feeds Monday's audit."
- 3. "This is for the Monday meeting."
- 2. "This one's important, pls prioritize."
- 1. "Just do it the way I said. Don't need to get into why on this one."

**Q12 link.** None asserted. A possible link to Q08 (purpose and importance of the job) is listed in `not_verified.md` as unconfirmed.

### D4. How-to information when the task is new or complex

**Definition.** When a task is new to the reader or complex, the message gives information about how to approach it, or points to where that information is. [S1 p.707; S1 p.708; S2 p.126]

**Basis.** S1 reports that people given a goal for a task that is new to them engage in deliberate planning to develop strategies [S1 p.707]. S1 notes that leaders can raise subordinates' self-efficacy by persuasive communication, which may include information about strategies for reaching the goal [S1 p.708]. S1 also lists not conveying task knowledge among the errors behind failed goal-setting results [S1 p.714]. S2 lists how as part of what direction-giving messages explain [S2 p.126].

**Applicability rule (Team judgment).** Score D4 when the message or its context signals that the task is new to the reader or complex. Mark it not assessable when the message signals a routine task, or when the judge cannot tell.

**Boundary (Team judgment).** D4 is about method. The result itself belongs to D1.

**Scale descriptors (Team judgment, paraphrasing S1 p.707 to 708 and S2 p.126).**
- **5.** The message gives the first steps or a method, plus a pointer to a guide, template, or person who can help.
- **4.** The message gives the steps or method, or a specific pointer, but not both.
- **3.** The message gives a partial hint ("use last year's file") without enough to start.
- **2.** The message offers vague help with no specific source ("ask around").
- **1.** The task is signaled as new or complex, and no method or source of help is offered.

**Anchors (Illustrative).**
- 5. "First time doing a cycle count? Start w/ the A-items list in the shared drive, scan each bin, and flag anything more than 2 units off. Dana can walk you thru the scanner."
- 4. "First time doing a cycle count? Start w/ the A-items list in the shared drive, scan each bin, and flag anything more than 2 units off."
- 3. "First time doing a cycle count? Use the A-items list in the shared drive."
- 2. "First time doing a cycle count? Ask around if u get stuck."
- 1. "Cycle count for zone C today. You'll figure it out."

**Q12 link.** None asserted.

### D5. Progress check

**Definition.** The message says when or how progress will be reviewed before or at completion. [S1 p.708]

**Basis.** S1 states that for goals to be effective, people need summary feedback that shows progress toward them [S1 p.708]. S1 also lists not providing feedback among the errors behind failed goal-setting results [S1 p.714].

**Caution.** S1 concerns the presence of progress feedback. The idea that an instruction message should set up that feedback is **Team judgment**.

**Boundary (Team judgment).** The final deadline belongs to D2.

**Scale descriptors (Team judgment, paraphrasing S1 p.708).**
- **5.** A specific check-in point is set (a time, a meeting, or a partial deliverable), plus what will be reviewed.
- **4.** A specific check-in point is set, with no statement of what will be reviewed.
- **3.** A loose check-in time is given ("sometime midweek").
- **2.** A general invitation to update is given with no time ("keep me posted").
- **1.** No mention of progress or review.

**Anchors (Illustrative).**
- 5. "Send me where you are by noon Wed and we'll check the totals together."
- 4. "Send me where you are by noon Wed."
- 3. "Send me where you are sometime midweek."
- 2. "Keep me posted on how it's going."
- 1. "Ok so that's the gist of it, I'm out most of the week at the offsite and won't really be checking messages much but I'm sure it'll be fine, just get it done."

**Q12 link.** Q11, someone at work talking about progress. The basis is overlap in wording between S1 p.708 (feedback showing progress) and the Q11 item [G1]. No source names Q12, so the mapping is **Team judgment**.

## Elements considered and left out

The reasons are in `not_verified.md`. In brief, goal difficulty cannot be judged from the text, because difficulty depends on the reader's ability and S1 treats it separately from specificity [S1 p.706]. Expressions of confidence [S1 p.708] and empathetic language [S2 p.126] have some source basis, but I left them out to keep the draft small (team judgment). They are candidates for the team.

## Rule for the label

**Team judgment, untested.** No source supplies cutoffs. The rule is a starting point for the pilot.

1. Score D1, D2, D3, and D5 on every in-scope message. Score D4 only when it applies.
2. **Good** requires D1 of 4 or more, D2 of 3 or more, no applicable dimension at 1, and a mean of 3.5 or more across applicable dimensions.
3. **Needs work** applies when D1 is 2 or less, or when two or more applicable dimensions are 2 or less.
4. **Borderline** covers every other case. It also applies when the judge's confidence is low, whatever the scores.
5. D1 and D2 are gated because S1 and S2 most directly support them [S1 p.706; S2 p.126]. The choice to gate them is still team judgment.
6. **Pending** applies when any dimension is pending. Once the writer fills in every placeholder, the message is scored again and the normal label rule applies. **Team judgment.**

## Abstention

**Team judgment.** The judge abstains and gives a reason in any of these cases.
- The message is not a task instruction (for example it is feedback, thanks, or an announcement).
- The message has fewer than about 8 words and no identifiable request.
- Both D1 and D2 are not assessable, for example because the message only refers to an earlier conversation ("do what we discussed").

## Judge instructions

**Team judgment.**
- For each dimension, quote the evidence first, then write the note, then give the score. If there is no evidence, say so before scoring.
- Quote evidence as exact substrings of the message, each 15 words or fewer.
- Typos, informal tone, emoji, and length do not raise or lower any score. This guards against the length and style bias the project must test for.
- Score only what is in the message. Do not assume context the message does not contain.
- When a dimension is not assessable, return null with a one-line reason.
- If a dimension's only evidence is a marked placeholder in square brackets ending in a question mark, such as "[due date?]", quote the placeholder, set the status to pending, and give no score.

## Judge output format

**Team judgment.** Each dimension carries a `status` of "scored", "not_assessable", or "pending". A pending dimension has a null score and quotes its placeholder as evidence. The `label` is one of "good", "borderline", "needs_work", or "pending".

```json
{
  "rubric_id": "task_instruction_v1.1",
  "in_scope": true,
  "abstain": {"value": false, "reason": null},
  "scores": {
    "D1_outcome_specificity": {"status": "scored", "evidence": ["take a look at the vendor stuff"], "note": "object named, no output wanted", "score": 2},
    "D2_time_frame": {"status": "scored", "evidence": ["whenever you get a chance"], "note": "no actionable time", "score": 1},
    "D3_rationale": {"status": "scored", "evidence": [], "note": "no evidence; no reason given", "score": 1},
    "D4_how_to": {"status": "not_assessable", "evidence": [], "note": "cannot tell if task is new", "score": null},
    "D5_progress_check": {"status": "scored", "evidence": [], "note": "no evidence; no review point", "score": 1}
  },
  "label": "needs_work",
  "confidence": {"level": "medium", "note": "short message; D4 not assessable"}
}
```

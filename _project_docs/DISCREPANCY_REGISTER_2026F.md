# Discrepancy Register — Fall 2026 (QM 47400)

Every known contradiction across the course's artifacts, consolidated in one place as of
**2026-08-20**. Sources reconciled: the live Brightspace export (2026-08-18), the official syllabus
docx, `syllabus.qmd`, `schedule.qmd`, `_project_docs/`, `_final_project/2026F/`, `_quizzes/`, the
announcement drafts, and the private task tracker.

**Severity:** 🔴 high (students see it, or it corrupts a source of truth) · 🟡 medium · ⚪ low ·
✅ resolved.

**Precedence when two artifacts disagree:** the official syllabus docx wins on *policy*; Brightspace
wins on *what students actually see and submit*; `schedule.qmd` wins on *session-by-session dates*.
Where those three conflict with each other, the conflict is listed below rather than silently
resolved.

---

## A. Brightspace vs. the repo

From `_project_docs/BRIGHTSPACE_INVENTORY_2026F.md`. 62 live items reconciled.

| ID | Where | The conflict | Sev | Task |
|---|---|---|:--:|---|
| A1 | `final_project_milestone_reference.md` vs Brightspace | **M00 is a different deliverable.** Repo: *Group Contact Confirmation*, due Sun Sep 6. Brightspace: *Instructor and TA Meetings – Round 01 Schedule*, due Sep 20. Different task, two weeks apart. | 🔴 | #29 |
| A2 | same | **M04, M07, M13 are live.** The reference file says they are "not used this term" and "Do not renumber". All three are built, dated, and pointed at 26 groups. | 🔴 | #29 |
| A3 | same vs `SYLLABUS_OF_RECORD` + website | **The project grade split has no peer-review line.** Reference file: 40/20/40. Website + syllabus of record: 30/20/10/20/20. Brightspace has a live *Peer Review Submission* (Nov 15), which settles it against the reference file. | 🔴 | #29 |
| A4 | same | **M12 title.** Repo: *LinkedIn Post Invitation* (and the filename encodes the channel). Brightspace: *Post Invitation for Poster Presentation*. | ⚪ | #29 |
| A5 | `_final_project/2026F/` | **Five live items have no instruction file:** M04, M07, M13, *Peer Review Submission* (Nov 15), *Conference Poster Presentation* (Nov 17). Repo documents 13 items; Brightspace has 16. | 🔴 | #29 |
| A6 | `_quizzes/` | **Unknown which bank version is loaded.** Banks live only in `_quizzes/2026Summer/` with versioned CSVs (v1–v4); there is no `_quizzes/2026F/`. All 16 quizzes went live to students Aug 24. Every bank was rewritten in Aug 2026 for the CV doctrine, so a stale import would teach the retired CI-overlap rule and contradict the midterm. | 🔴 | #30 |
| A7 | repo | **Three participation-type quizzes have no repo content:** Group Check-in (Aug 28), Syllabus Quiz (Aug 30), Team Setup (Sep 20). | 🟡 | #31 |
| A8 | repo | **Three participation surveys have no repo content:** Profile Survey (Aug 30), Midterm Feedback (Sep 30), Reflection Survey (Dec 11). The Reflection Survey exists only inside retired `nb20`, unreachable by students. | 🟡 | #32 |
| A9 | `syllabus.qmd` vs Brightspace | **Extra-credit rules are not published.** Four live items (Mid-term Eval Oct 2, DataCamp Dec 4, Issues in Materials Dec 4, Final Eval Dec 11). `syllabus.qmd` carries only a stub pointer to Brightspace. DataCamp is worth **up to 5% of the course grade** and its "no two completions within two days" rule plus a Dec 4 deadline makes late awareness unrecoverable. | 🔴 | #33 |
| A10 | repo | **No peer-evaluation instrument exists.** Peer evaluation is 20% of the Final Project, 20% of the Competition, and 20% of Poster-to-Product. No rubric or rating form in the repo. | 🟡 | #34 |
| A11 | `_course_case_competition/2026F/` | **Unconfirmed coverage.** Brightspace has *Rank Code Submission* (Nov 29). Not verified that the instructions describe this deliverable rather than only the Kaggle leaderboard submission. | 🟡 | #35 |
| A12 | Brightspace | **Poster-to-Product has zero Brightspace items** despite being 5% of the grade: no deliverable dropbox, no showcase item, no peer evaluation. Either deliberate or never built. | 🟡 | #35 |

## B. Published site vs. sources of record

| ID | Where | The conflict | Sev | Task |
|---|---|---|:--:|---|
| B1 | `schedule.qmd:63` → published `docs/schedule.html` | The midterm coverage line still reads **"cross-validation with 95% CIs"**. That is retired claim W1 in `CV_INFERENCE_DOCTRINE.md`; the interval is descriptive, not a confidence interval. It is **live on the public website** and contradicts nb08, the rebuilt midterm banks, and nb00. | 🔴 | none |
| B2 | `schedule.qmd` vs `_announcements/2026F/upcoming_deadlines_and_key_dates.md` | **Thanksgiving span.** Schedule says Nov 25–28; the announcement says Nov 25–27. | ⚪ | none |

## C. Task tracker vs. reality

| ID | Where | The conflict | Sev | Task |
|---|---|---|:--:|---|
| C1 | tracker issue #10 | **Midterm date and coverage both stale.** Issue says "~Sep 23" covering "nb00–nb10". Reality: **Fri Sep 25**, covering **nb00–nb09**; nb10 is retired. | 🟡 | #10 |
| C2 | tracker issue #19 | **Milestone list built on the stale reference.** Lists M00 as Sep 6, states "skips M04/M07/M13", and enumerates 11 items where Brightspace has 16. | 🟡 | commented; blocked by #29 |
| C3 | tracker issue #3 | **Appears already complete.** "Build Brightspace course shell" (due Aug 21) — the export shows 62 items built, dated, and windowed. | ⚪ | close? |

## D. Repo-internal drift and tooling

| ID | Where | The conflict | Sev | Task |
|---|---|---|:--:|---|
| D1 | `CLAUDE.md` (6 references) | **Documented path does not exist.** CLAUDE.md points the instructor-page scripts and sync command at `_adm_stuff/_instructor_page/`; the real location is `_adm/_instructor_page/`. `_adm_stuff/` is gone. The documented sync command fails as written. The `p2p-research-program` memory carries the same stale prefix. | 🟡 | none |
| D2 | `scripts/sync_instructor_md.sh` | **Silently skips.** No `.venv` with `nbconvert`, so it exits without regenerating anything and `_notebook_lm/` has no nb00 markdown for NotebookLM. Failure is invisible unless the output is read. | ⚪ | none |
| D3 | `notebooks/` vs `CLAUDE.md` | **Narrative polish is incomplete.** CLAUDE.md states the nb08 Q&A pattern is "applied consistently across all 18 notebooks". Actual counts: nb00–nb07 have **zero**; nb08+ have 7–17 each. | ⚪ | none |

## E. Inside the official syllabus docx

Carried forward from `SYLLABUS_OF_RECORD_2026F.md`. These are contradictions *within* the document
of record, or between it and the site.

| ID | The conflict | Sev | Task |
|---|---|:--:|---|
| E1 | **The embedded schedule is the wrong offering.** The docx's "TENTATIVE COURSE SCHEDULE" is the Summer 2026 4-week intensive: "May 18 – June 12, 2026", Day 0–20, Colab links pointing at the `2026Summer_..._MGMT474` repo. Students reading the official syllabus get a May–June calendar and dead notebook links. | 🔴 | none |
| E2 | ~~Two contradictory Final Project sections~~ — **resolved.** The live *Peer Review Submission* in Brightspace confirms the later 30/20/10/20/20 version is operative (see A3). The docx should be cut down to that version. | ✅ | #29 |
| E3 | **Kaggle open date.** Docx says the competition opens **Aug 28**; the site and planning docs said **Aug 24**. nb00 now defers to Brightspace rather than printing either, but the docx/site contradiction itself is unresolved. | 🟡 | none |
| E4 | **Typo: "after August 248, 2026"** in the DataCamp extra-credit rule. It is the eligibility start date, so it should read Aug 24 or Aug 28 to match E3. | ⚪ | none |
| E5 | **Typo: "within 1 calendar days"** in the grade-challenge rule. | ⚪ | none |
| E6 | Office hours (Mon 2:30–3:30 EST) are in the docx; the site defers to Brightspace. **Intentional**, no action. | ✅ | — |
| E7 | The docx keeps the Poster-to-Product 80/20 and competition 20/60/20 breakdowns that the site dropped in the 2026-08-17 trim. **Intentional**, no action. | ✅ | — |
| E8 | Prerequisite (MGMT 305), section numbers, room (WTHR 114), the Kaggle invitation link, the poster-examples link, and the whole extra-credit section appear **only** in the docx. Noted so they are not lost. | ⚪ | A9 covers extra credit |

## F. Resolved during the 2026-08-18 to 2026-08-20 sessions

| ID | The conflict | How it was resolved |
|---|---|---|
| F1 | nb00 stated the midterm as **14** multiple-choice questions; the syllabus of record and `_midterm_exam/2026F/README.md` both say **15**, five alternatives each. | The paragraph was deleted from nb00 in the trim; Brightspace and the schedule already said 15. |
| F2 | nb00's Course Map advertised nb08 as "95% CI; **the CI-overlap rule**" and Module 2 as "k-fold CV with 95% confidence intervals" — retired claims W1 and W2. | Rewritten to descriptive fold intervals and paired per-fold comparison. **B1 is the same defect still live on the website.** |
| F3 | nb00's key-dates list was out of chronological order, and its schedule table carried a vestigial "Track" column that `schedule.qmd` had already dropped. | Resolved by deleting the calendar section. |
| F4 | nb00's arc table tagged nb05/nb09 as "Project Milestone 1/2" with no milestone list left to define them. | Tags dropped. |
| F5 | The nb00 video guide described the retired Summer 4-week/20-day format, `nb20` as the final notebook, and nb00 as a "Day 0 pre-course activity"; its cell index predated the calendar section. | Re-paced to Fall MWF and re-synced to the 18-cell notebook. |

---

## Priority order for the open items

1. **A6** (quiz bank version) — quizzes went live Aug 24; a stale bank teaches a retired rule.
2. **A9** (extra-credit rules unpublished) — DataCamp's 5% becomes unearnable the longer it waits.
3. **A1–A3, A5** (milestone track) — corrupts the file every other document is told to follow; M01 opens Sep 9.
4. **B1** (95% CIs on the live site) — one line, one render, removes a public contradiction.
5. **E1** (wrong schedule inside the official syllabus) — students are reading a May–June calendar.

---

**Last updated:** 2026-08-20.
**Maintained by:** Professor Davi Moreira + AI Assistants.

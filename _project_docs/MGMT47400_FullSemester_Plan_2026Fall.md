# QM47400 — Predictive Analytics (3 credits)
## Full-Semester Course Plan — Fall 2026 (Daniels School of Business)

**Term:** Fall 2026, Purdue University (Mitch Daniels School of Business)
**Class meetings:** **Monday / Wednesday / Friday**, in person, during scheduled class time
**Instructor:** Professor Davi Moreira
**Format:** In-person MWF lectures + hands-on Jupyter notebooks in **Google Colab**, with the course's short **micro-videos (≤ 12 min each)** retained as async review/supplement.
**AI support:** students use **Gemini inside Colab** for guided "vibe coding" (draft → verify → document).
**Course center of gravity:** supervised predictive modeling in Python (ISLP-with-Python style), delivered through an applied team project that culminates in a **research poster** and a **Poster-to-Product** build sprint.

> **Re-pacing note.** This plan re-paces **20 notebooks** (nb00–nb09 and nb11–nb20) from the 4-week intensive offering across a **full ~15-week Fall semester**. **nb10 (the midterm casebook) retires from the arc together with the midterm exam**, which Fall 2026 does not administer. The notebook *content is unchanged* — only the calendar anchoring and the surrounding studio/milestone/project structure are new. **Mondays and Wednesdays carry the course content; every Friday is a studio session for the poster and/or the Course Case Competition** — the one exception is Fri Aug 28, which carries nb02. Everything the 4-week plan expressed as "Day N / 112.5 min/day / 20 business days" is replaced by Fall MWF sessions.

---

## Anchoring dates (Fall 2026)

**Official Purdue Fall 2026 academic calendar:**
- Classes begin: **Mon Aug 24, 2026**
- Labor Day (no class): **Mon Sep 7**
- Fall Break (no class): **Mon–Tue Oct 12–13**
- Thanksgiving vacation (no class): **Wed–Sat Nov 25–28**
- Classes end: **Sat Dec 12**; Final exams: **Dec 14–19**

**Course-specific anchors:**
- **Fall Undergraduate Research Conference (URC) poster presentation: Tue Nov 17, 2026** — **all students required to present.**
- **Poster submission deadline: Tue Nov 10, 2026** (7 days before URC).
- **Lecture content completes Mon Oct 26** (nb17); the last notebook, **nb20**, lands in the **Fri Nov 6** studio — leaving Oct 28 – Nov 16 for poster build, finalization, and dry-runs.
- **Poster-to-Product (P2P) build sprint runs after URC:** Nov 20 – Dec 9, culminating in a showcase (Wed Dec 9); course wrap Fri Dec 11.
- **Kaggle Case Competition** runs Aug 24 → **online work session Mon Nov 23**, final submission **Sun Nov 29** (concluded over the Thanksgiving-week online session, so December is a clean P2P runway — mirrors Fall 2025, which closed the competition Nov 30).

**Session modality.** Every session meets **in person** (MWF), with one exception: the Thanksgiving-week competition block. **Mon Nov 23** runs **online** as a work session to finalize and conclude the Kaggle competition, and the competition stays open online across the **Nov 25–28** break days through the Sun Nov 29 deadline. Per the design: **nb05 (Ridge/Lasso) is an in-person lecture**, **nb14's test-set ceremony stays in person**, and **nb15 (M3 walkthrough) and nb20 (course wrap) need no standalone lecture** — both are folded into Friday studios.

---

## Pedagogical pattern (unchanged from the notebook design)

Each notebook follows the course loop: **Concept + demo → PAUSE-AND-DO practice → Solution + common mistakes + extensions → next concept**. In the full-semester format, each Monday/Wednesday session anchors one notebook, and every Friday is a studio session for milestones, poster work, the Kaggle competition, and the P2P sprint.

---

## Grading (aligned to the student syllabus)

| Assessment | Weight |
|---|---:|
| Participation | 5% |
| Quizzes | 20% |
| Course Case Competition (Kaggle) | 30% |
| Final Project (Poster → Poster-to-Product) | 45% |

**There is no midterm and no final exam in Fall 2026.** The 20% the midterm carried in earlier offerings is redistributed to the two applied assessments — **+10 points to the Course Case Competition** and **+10 points to the Final Project** — so the semester is evaluated on work students actually build. Participation and Quizzes are unchanged.

**Course Case Competition (30%)** — the semester-long Kaggle competition (details below), worked in the Friday studios and concluded over the Thanksgiving-week online block.

**Final Project (45%)** now spans **two integrated stages of one project**:
1. **Research Poster** — the applied predictive-analytics project (milestones M1–M4), presented at the **URC on Nov 17**.
2. **Poster-to-Product** — the post-poster, two-week in-class build sprint that converts the validated model into a **stakeholder-ready dashboard/app + executive brief**, with corporate-partner feedback and a final showcase. (P2P is the post-poster phase of the Final Project, not a separate top-level grade.)

Final-project grade composition (see Brightspace syllabus for exact splits): milestone deliverables, poster + P2P deliverables (deployed app + executive brief + showcase), intra-group peer evaluation, and instructor/TA evaluation. P2P is assessed on the **NACE competencies** — Technology, Teamwork, Communication, Critical Thinking — via rubric.

---

## Kaggle Case Competition (individual or pairs / small teams)

- **Competition:** Fall 2026 QM47400 Case Competition: Bank Churn
- **Task:** Predict the probability that a bank customer churns (`Exited` = 1)
- **Metric:** AUC-ROC; **Platform:** Kaggle (private class competition, max 5 submissions/day)
- **Opens:** Aug 24, 2026 · **Online work session:** Mon Nov 23 · **Final submission:** Sun Nov 29, 2026, 11:59 PM (Kaggle + Brightspace code)
- **Brightspace deliverable:** complete, fully replicable code for the best model (preprocessing → feature engineering → training → evaluation → submission file). Kaggle team name `Group NN`; notebook `NN_kaggle_code.ipynb`.

---

## Project milestones (Fall 2026)

Canonical reference: [`_final_project/2026F/final_project_milestone_reference.md`](../_final_project/2026F/final_project_milestone_reference.md) (individual `milestone_NN_*.md` files sit beside it). **Milestone numbering is taken exactly from the 2026F reference documents** — it intentionally skips M04 / M07 / M13 (retired meeting-scheduling milestones). Due dates follow the Fall 2025 cadence; deliverables are due **Sundays 11:59 PM** except the final poster (pinned to **Tue Nov 10**, 7 days before the conference).

> **Notebook vs. milestone numbering:** the notebooks use a simplified "M1–M4" project track internally (nb05 proposal, nb09 baseline, nb15 "M3" complex-model walkthrough). The **official deliverables are M00–M12** below; map by topic (complex model → M08, draft abstract → M03). Notebook content is unchanged this term.

| # | Milestone | Due (Fall 2026) | 2025F ref. |
|---|-----------|-----------------|------------|
| **M00** | Group Contact Confirmation | **Sun Sep 6** | ~Sep 9 |
| **M01** | Initial Project Proposal | **Sun Sep 20** | Sep 21 |
| **M02** | Expanded Project Outline | **Sun Sep 27** | Sep 28 |
| **M03** | Project Draft Abstract (~250 words) | **Sun Oct 4** | Oct 5 |
| **M05** | Applying to the Conference | **Sun Oct 11** | Oct 15 |
| **M06** | Simple Model & Performance Evaluation (baseline + k-fold CV) | **Sun Oct 18** | Oct 19 |
| **M08** | More Complex Models & Performance Evaluation (tuning + CV) | **Sun Oct 25** | Oct 26 |
| **M09** | Poster First Draft | **Sun Nov 1** | Nov 2 |
| **M10** | Final Poster Submission (`NN.pdf`) | **Tue Nov 10** | Nov 9 |
| **M11** | Poster Presentation Planning (elevator pitches) | **Sun Nov 15** | Nov 16 |
| **M12** | LinkedIn Post Invitation | **Sun Nov 15** | Nov 16 |
| — | **URC Poster Presentation (required, all students)** | **Tue Nov 17** | Nov 18 |
| — | Intra-group Peer Evaluation | **Fri Dec 11** | — |
| **P2P** | Poster-to-Product: deployed dashboard/app + executive brief + showcase | **Showcase ~Wed Dec 9** | — |

---

## Notebook Sequence Rationale

The 20-notebook progression is **identical to the established arc** — each notebook builds one conceptual layer, assumes only prior notebooks, and prepares the next. The four-unit organization below replaces the four "weekly arcs" of the intensive format; the dependency chain is unchanged.

```
Orientation
  00 Launchpad / Setup  (platform fluency, AI policy, Kaggle launch, P2P preview)

Unit 1 — REGRESSION
  01 EDA/Splits → 02 Pipelines → 03 Metrics/Baselines → 04 Features/Diagnostics → 05 Regularization
  (M1 Proposal at nb05)

Unit 2 — CLASSIFICATION
  06 LogReg → 07 Clf Metrics → 08 Cross-Validation → 09 Tuning+FE+Leakage
  (M2 Baseline in this unit; nb10 retired with the midterm exam)

Unit 3 — ENSEMBLES + SELECTION
  11 Trees → 12 Random Forests → 13 Gradient Boosting → 14 Selection + Test-Set Ceremony → 15 M03 Walkthrough
  (nb15 walks the complex-model + abstract milestone retrospectively on Fri Oct 30 — after M03 and M08 have been submitted — inside the studio whose structured peer review of poster drafts feeds M09)

Unit 4 — DELIVERY
  16 Time Series → 17 Communication/Poster Design → 18 Competition Workflow → 19 Deep Learning → 20 Course Wrap
```

**Delivery is sequenced out of diagram order to serve the calendar.** The *conceptual* dependency chain above is unchanged, but the delivery notebooks move: **nb18 (Competition Workflow) is pulled forward to Fri Sep 25**, right after nb09, so the Kaggle competition has a real submission pipeline from week 5 — then **revisited Fri Oct 23**, once random forests, gradient boosting, and the nb14 selection protocol are taught and the champion model can be pushed through that pipeline. **nb17 (Communication & Poster Design) lands in week 10 (Mon Oct 26)**, immediately before poster production begins, and **nb15 (M03 walkthrough, Fri Oct 30) and nb20 (course wrap, Fri Nov 6)** are folded into Friday studios. **nb14 keeps its in-person Wed Oct 7 slot** — the test-set ceremony is a live event.

The CV-first / test-set-lock discipline is preserved exactly: cross-validation is the evaluation spine from nb08 onward, the test set stays locked until nb14's one-shot ceremony, and nb18's Kaggle-submission demo is the only other authorized use of a locked test file. *(See `CLAUDE.md` for the full CV-first rule and `scripts/audit_cv_first.py`.)*

---

## Session-by-session calendar (MWF, Fall 2026)

Legend: **nbNN** = notebook anchored that session · Mode = *In person* / *Studio* (poster / competition / project working session) / *Build sprint* (P2P) / *Online* (Thanksgiving-week competition block only) · ⛔ = no class. **Monday and Wednesday carry the content; every Friday is a poster and/or competition studio** — the single exception is Fri Aug 28, which carries nb02.

### Week 1 — Aug 24–28 · Orientation + start of Regression
| Date | Mode | Session |
|---|---|---|
| Mon Aug 24 | In person | Course launch + **nb00** Launchpad (syllabus, grading, Colab, Gemini, AI policy, **P2P preview**, **Kaggle launch**) |
| Wed Aug 26 | In person | **nb01** EDA & Splits |
| Fri Aug 28 | In person | **nb02** Preprocessing Pipelines |

### Week 2 — Aug 31–Sep 4 · Regression + competition launch
| Date | Mode | Session |
|---|---|---|
| Mon Aug 31 | In person | **nb03** Regression Metrics & Baselines |
| Wed Sep 2 | In person | **nb04** Linear Features & Diagnostics |
| Fri Sep 4 | Studio | Kaggle kickoff studio — join the competition, form teams, download the data, first submission · group formation · **M00 Group Contact due Sun Sep 6** |

### Week 3 — Sep 7–11 · Regularization + project launch
| Date | Mode | Session |
|---|---|---|
| Mon Sep 7 | ⛔ | Labor Day |
| Wed Sep 9 | In person | **nb05** Regularization (Ridge/Lasso) — live lecture |
| Fri Sep 11 | Studio | Project studio — topic and data lock-in, M01 drafting · competition EDA |

### Week 4 — Sep 14–18 · Classification
| Date | Mode | Session |
|---|---|---|
| Mon Sep 14 | In person | **nb06** Logistic Regression & Pipelines |
| Wed Sep 16 | In person | **nb07** Classification Metrics & Thresholding |
| Fri Sep 18 | Studio | Project studio — M01 finalize + M02 outline kickoff · competition baseline push · **M01 Proposal due Sun Sep 20** |

### Week 5 — Sep 21–25 · Evaluation spine + competition workflow
| Date | Mode | Session |
|---|---|---|
| Mon Sep 21 | In person | **nb08** Cross-Validation & Model Comparison |
| Wed Sep 23 | In person | **nb09** Tuning + Feature Engineering + Leakage Detection |
| Fri Sep 25 | Studio | **nb18** Competition Workflow & Kaggle Submission — competition studio · **M02 Outline due Sun Sep 27** |

### Week 6 — Sep 28–Oct 2 · Ensembles I
| Date | Mode | Session |
|---|---|---|
| Mon Sep 28 | In person | **nb11** Decision Trees (paired clf + reg) |
| Wed Sep 30 | In person | **nb12** Random Forests & Importance |
| Fri Oct 2 | Studio | Competition studio — tuned-pipeline leaderboard push · draft abstract · **M03 Draft Abstract due Sun Oct 4** |

### Week 7 — Oct 5–9 · Ensembles II + model selection
| Date | Mode | Session |
|---|---|---|
| Mon Oct 5 | In person | **nb13** Gradient Boosting |
| Wed Oct 7 | In person | **nb14** Model Selection + Test-Set Ceremony + Monitoring (live ceremony) |
| Fri Oct 9 | Studio | Poster studio — URC application workshop + abstract polish · **M05 Conference Application due Sun Oct 11** |

### Week 8 — Oct 12–16 · Time series + poster start
| Date | Mode | Session |
|---|---|---|
| Mon Oct 12 | ⛔ | Fall Break (Oct 12–13) |
| Wed Oct 14 | In person | **nb16** Time-Series Forecasting |
| Fri Oct 16 | Studio | Poster studio — turn M06 results into tables and draft figures · **M06 Simple Model due Sun Oct 18** |

### Week 9 — Oct 19–23 · Deep learning + results lock-in
| Date | Mode | Session |
|---|---|---|
| Mon Oct 19 | In person | **nb19** Deep Learning |
| Wed Oct 21 | Studio | Results lock-in clinic — champion model, CV intervals, model card for the poster |
| Fri Oct 23 | Studio | Competition studio — **nb18 revisit**: random forest / gradient boosting / champion model into the submission pipeline · **M08 Complex Models due Sun Oct 25** |

### Week 10 — Oct 26–30 · Communication + poster production
| Date | Mode | Session |
|---|---|---|
| Mon Oct 26 | In person | **nb17** Data Communication & Poster Design — **lecture content complete** |
| Wed Oct 28 | Studio | Poster production — figures built to the nb17 standard |
| Fri Oct 30 | Studio | **nb15** M03 milestone walkthrough + structured peer review of poster drafts · **M09 Poster First Draft due Sun Nov 1** |

### Week 11 — Nov 2–6 · Poster polish + Kaggle push
| Date | Mode | Session |
|---|---|---|
| Mon Nov 2 | Studio | Poster production — figure revision from peer feedback |
| Wed Nov 4 | Studio | Poster production — narrative and assembly |
| Fri Nov 6 | Studio | **nb20** course closeout brief + final poster QA + Kaggle leaderboard push — **all 20 notebooks covered** |

### Week 12 — Nov 9–13 · Poster submission + presentation prep
| Date | Mode | Session |
|---|---|---|
| Mon Nov 9 | Studio | Final poster QA → submission · **M10 Final Poster due Tue Nov 10** |
| Wed Nov 11 | Studio | Dry-run presentations |
| Fri Nov 13 | Studio | Presentation coaching + logistics |

### Week 13 — Nov 16–20 · URC + P2P kickoff
| Date | Mode | Session |
|---|---|---|
| Mon Nov 16 | Studio | Final presentation prep · **M11 Planning + M12 LinkedIn due Sun Nov 15** |
| **Tue Nov 17** | **Conference** | **URC Poster Presentation — all students present** |
| Wed Nov 18 | ⛔ | No class — rest and catch up on other coursework |
| Fri Nov 20 | Build sprint | **P2P kickoff** — scoping, partner problem framing, AI-assistant assignment, product spec · Kaggle leaderboard push |

### Week 14 — Nov 23–27 · Kaggle close + Thanksgiving
| Date | Mode | Session |
|---|---|---|
| Mon Nov 23 | **Online** | **Course Case Competition — finalize & conclude** (online work session: final push, notebook cleanup, Run-All reproducibility check) |
| Wed Nov 25 | ⛔ | Thanksgiving break (Nov 25–28) — competition stays open online |
| Fri Nov 27 | ⛔ | Thanksgiving break — final submission window, online · **Kaggle final submission due Sun Nov 29, 11:59 PM** |

### Week 15 — Nov 30–Dec 4 · P2P build
| Date | Mode | Session |
|---|---|---|
| Mon Nov 30 | Build sprint | **P2P** — data engineering + model validation |
| Wed Dec 2 | Build sprint | **P2P** — deployment + partner checkpoint |
| Fri Dec 4 | Build sprint | **P2P** — usability testing + iteration |

### Week 16 — Dec 7–11 · Showcase + closeout
| Date | Mode | Session |
|---|---|---|
| Mon Dec 7 | Build sprint | **P2P** — executive brief drafting + showcase preparation |
| Wed Dec 9 | Showcase | **P2P SHOWCASE** — partners + feedback |
| Fri Dec 11 | In person | Course wrap — peer evaluation + reflection survey (Kaggle already concluded Nov 29) |

**Finals week (Dec 14–19):** no final exam and no midterm in Fall 2026; the week is a buffer for late deliverables and grading.

### Comparison with Fall 2025 pacing (what changed and why)

The Fall 2025 offering (`_syllabus/2025F/mgmt474_fall2025_schedule.md`) spread ~9 topics across the semester with twice-weekly in-class sessions + weekly homework, and **taught deep learning in December, *after* the conference**; its case-competition rank submission closed **Nov 30**. Fall 2026 keeps the proven beats but re-orders for the Nov 17 URC requirement:

- **All content finishes before the conference** — lecture content completes **Mon Oct 26** (nb17) and the last notebook, **nb20**, lands in the **Fri Nov 6** studio, instead of running into December. The poster needs the full toolkit (incl. nb19 deep learning) in hand by early November.
- **Kaggle concludes Nov 29** (≈ 2025F's Nov 30) via an **online work session on Mon Nov 23** before Thanksgiving, so December is a clean Poster-to-Product runway.
- **No midterm.** Fall 2026 drops the midterm exam and retires **nb10 (the midterm casebook)** with it, leaving a **20-notebook arc**. The exam's 20% moves to the applied work: **Course Case Competition 30%**, **Final Project 45%**.
- **Every Friday is a studio.** Mondays and Wednesdays carry the content; Fridays are dedicated poster and/or competition working sessions (the one exception is Fri Aug 28, which carries nb02). That guarantees the project and the competition weekly class time instead of leaving them to homework — and it is what the dropped midterm slots paid for.
- **Modality is simple:** every session meets **in person** except the Thanksgiving-week competition block (**Mon Nov 23** online, competition open online across the Nov 25–28 break). **nb05 stays a live lecture** (Ridge/Lasso benefits from real-time explanation) and **nb14 stays in person** (the test-set ceremony is a live event).
- **No-lecture notebooks reclaimed for pacing:** **nb15** (M03 walkthrough) and **nb20** (course wrap) need no standalone lecture and ride inside Friday studios (Oct 30 and Nov 6), while **nb18** is pulled forward to **Fri Sep 25** and revisited **Fri Oct 23** — so the competition has a working submission pipeline early and a champion-model push late, and the heaviest notebooks breathe instead of one-per-session cramming.
- **Milestone track follows the 2026F reference numbering (M00–M12)** with Fall-2025-style Sunday due dates, replacing the notebooks' internal "M1–M4" shorthand.

---

## Poster-to-Product (P2P) — experiential capstone

Funded by a **$5,000 Daniels Experiential Learning Grant** (Curriculum Innovation Grant), P2P is the post-poster phase of the Final Project. Over a two-week in-class build sprint, teams convert their validated model into a **stakeholder-ready dashboard/app plus an executive brief**, following an industry product workflow: scope → data engineering → model validation → UX → deployment → usability test → showcase.

**Key design elements (from the grant proposal):**
- Each team is randomly assigned an **AI assistant** (a generic assistant or a course-tuned one) to scaffold planning, code review, documentation, and ethical guardrails — with **human-in-the-loop sign-offs**.
- **Industry/nonprofit partners** provide problem context and usability feedback at checkpoints and at the showcase.
- Deliverables: a **deployed prototype** + **executive brief** + showcase presentation.
- Assessed via **NACE-aligned rubrics** (Technology, Teamwork, Communication, Critical Thinking).
- Outcomes feed a reusable departmental "Poster-to-Product Instructor Kit" (rubrics, AI persona/prompt library, deployment templates) and a SoTL brief.

*Source materials:* `_adm_stuff/_qm474_poster_product/` (grant approval, application answers, budget).

---

## Course-wide core references (unchanged)
- James, Witten, Hastie, Tibshirani. *An Introduction to Statistical Learning* (ISLP) + Python labs.
- Hastie, Tibshirani, Friedman. *The Elements of Statistical Learning* (ESL).
- Provost, Fawcett. *Data Science for Business*.
- Pedregosa et al. "Scikit-learn: Machine Learning in Python." *JMLR*.
- scikit-learn User Guide (pipelines, preprocessing, model selection, metrics, inspection).
- Chip Huyen. *Designing Machine Learning Systems* (deployment thinking, monitoring).

---

**Supersedes:** `MGMT47400_Online4Week_Plan_2026Summer.md` (4-week intensive; archived).
**Last updated:** 2026-08-14 · **Maintained by:** Professor Davi Moreira + AI assistants.

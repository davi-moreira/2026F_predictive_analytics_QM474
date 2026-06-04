# QM47400 — Predictive Analytics (3 credits)
## Full-Semester Course Plan — Fall 2026 (Daniels School of Business)

**Term:** Fall 2026, Purdue University (Mitch Daniels School of Business)
**Class meetings:** **Monday / Wednesday / Friday**, in person, during scheduled class time
**Instructor:** Professor Davi Moreira
**Format:** In-person MWF lectures + hands-on Jupyter notebooks in **Google Colab**, with the course's short **micro-videos (≤ 12 min each)** retained as async review/supplement.
**AI support:** students use **Gemini inside Colab** for guided "vibe coding" (draft → verify → document).
**Course center of gravity:** supervised predictive modeling in Python (ISLP-with-Python style), delivered through an applied team project that culminates in a **research poster** and a **Poster-to-Product** build sprint.

> **Re-pacing note.** This plan re-paces the **same 21 notebooks** (nb00–nb20) used in the 4-week intensive offering across a **full ~15-week Fall semester**. The notebook *content is unchanged* — only the calendar anchoring and the surrounding studio/milestone/project structure are new. Everything the 4-week plan expressed as "Day N / 112.5 min/day / 20 business days" is replaced by Fall MWF sessions.

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
- **Course content (nb00–nb20) completes by Oct 21**, leaving Oct 23 – Nov 16 for poster build, finalization, and dry-runs.
- **Poster-to-Product (P2P) build sprint runs after URC:** Nov 18 – Dec 11, culminating in a showcase (~Dec 9).
- **Kaggle Case Competition** runs Aug 24 → final submission **Mon Nov 23** (concluded before Thanksgiving, so December is a clean P2P runway — mirrors Fall 2025, which closed the competition Nov 30).

**Session modality.** Most sessions are **in-person** (MWF). A handful are deliberately **online/async** (watch the recorded micro-videos + work the notebook): **Oct 2** (instructor travel to Chicago), **Oct 9 & Oct 14** (bracketing Fall Break Oct 12–13), and **Mon Nov 23** (before Thanksgiving — used to finalize and conclude the Kaggle competition). Per the design: **nb05 (Ridge/Lasso) is an in-person lecture**; **nb10 (midterm casebook), nb15 (M3 walkthrough), and nb20 (course wrap) need no lecture** (self-guided / studio).

---

## Pedagogical pattern (unchanged from the notebook design)

Each notebook follows the course loop: **Concept + demo → PAUSE-AND-DO practice → Solution + common mistakes + extensions → next concept**. In the full-semester format, each MWF session anchors one notebook (a few studio/buffer sessions are interleaved for milestones, the midterm, poster work, and the P2P sprint).

---

## Grading (aligned to the student syllabus)

| Assessment | Weight |
|---|---:|
| Participation | 5% |
| Quizzes | 20% |
| Online — In-Person Midterm Exam | 20% |
| Course Case Competition (Kaggle) | 20% |
| Final Project (Poster → Poster-to-Product) | 35% |

**Midterm (20%)** — administered **in person, during class time** (~late September), after the classification + cross-validation arc. Comprehensive multiple-choice / short business-case practicum on the foundational toolkit (nb00–nb10).

**Final Project (35%)** now spans **two integrated stages of one project**:
1. **Research Poster** — the applied predictive-analytics project (milestones M1–M4), presented at the **URC on Nov 17**.
2. **Poster-to-Product** — the post-poster, two-week in-class build sprint that converts the validated model into a **stakeholder-ready dashboard/app + executive brief**, with corporate-partner feedback and a final showcase. (P2P is the post-poster phase of the Final Project, not a separate top-level grade.)

Final-project grade composition (see Brightspace syllabus for exact splits): milestone deliverables, poster + P2P deliverables (deployed app + executive brief + showcase), intra-group peer evaluation, and instructor/TA evaluation. P2P is assessed on the **NACE competencies** — Technology, Teamwork, Communication, Critical Thinking — via rubric.

---

## Kaggle Case Competition (individual or pairs / small teams)

- **Competition:** Fall 2026 QM47400 Case Competition: Bank Churn
- **Task:** Predict the probability that a bank customer churns (`Exited` = 1)
- **Metric:** AUC-ROC; **Platform:** Kaggle (private class competition, max 5 submissions/day)
- **Opens:** Aug 24, 2026 · **Final submission:** Mon Nov 23, 2026, 11:59 PM (Kaggle + Brightspace code) — concluded on the online pre-Thanksgiving session
- **Brightspace deliverable:** complete, fully replicable code for the best model (preprocessing → feature engineering → training → evaluation → submission file). Kaggle team name `Group NN`; notebook `NN_kaggle_code.ipynb`.

---

## Project milestones (re-paced to Fall)

Canonical reference: [`_final_project/2026Summer/final_project_milestone_reference.md`](../_final_project/2026Summer/final_project_milestone_reference.md) *(milestone content unchanged; dates re-anchored below).*

| Milestone | Deliverable | Due (Fall 2026) |
|---|---|---|
| **M1** | Initial Project Proposal (goal + motivation + data + preliminary methods, 1–2 pp) | **Fri Sep 4** |
| **M2** | Simple Model + Performance Evaluation (EDA + FE + baseline pipeline w/ k-fold CV) | **Fri Sep 18** |
| **M3** | Complex Model + Hyperparameter Tuning + Draft Abstract (~250 words) + saved `champion_pipeline.joblib` | **Fri Oct 9** |
| **M4** | Final Research Poster (`<group-number>.pdf`) + intra-group Peer Evaluation | **Poster due Tue Nov 10**; present **Tue Nov 17** |
| **P2P** | Poster-to-Product: deployed dashboard/app + executive brief + showcase | **Showcase ~Wed Dec 9** |

---

## Notebook Sequence Rationale

The 21-notebook progression is **identical to the established arc** — each notebook builds one conceptual layer, assumes only prior notebooks, and prepares the next. The four-unit organization below replaces the four "weekly arcs" of the intensive format; the dependency chain is unchanged.

```
Orientation
  00 Launchpad / Setup  (platform fluency, AI policy, Kaggle launch, P2P preview)

Unit 1 — REGRESSION
  01 EDA/Splits → 02 Pipelines → 03 Metrics/Baselines → 04 Features/Diagnostics → 05 Regularization
  (M1 Proposal at nb05)

Unit 2 — CLASSIFICATION + MIDTERM
  06 LogReg → 07 Clf Metrics → 08 Cross-Validation → 09 Tuning+FE+Leakage → 10 Midterm Casebook
  (M2 Baseline in this unit; in-person Midterm exam)

Unit 3 — ENSEMBLES + SELECTION
  11 Trees → 12 Random Forests → 13 Gradient Boosting → 14 Selection + Test-Set Ceremony → 15 Interpretation
  (M3 Complex Model + Abstract at nb15)

Unit 4 — DELIVERY
  16 Time Series → 17 Communication/Poster Design → 18 Competition Workflow → 19 Deep Learning → 20 Course Wrap
```

The CV-first / test-set-lock discipline is preserved exactly: cross-validation is the evaluation spine from nb08 onward, the test set stays locked until nb14's one-shot ceremony, and nb18's Kaggle-submission demo is the only other authorized use of a locked test file. *(See `CLAUDE.md` for the full CV-first rule and `scripts/audit_cv_first.py`.)*

---

## Session-by-session calendar (MWF, Fall 2026)

Legend: **nbNN** = notebook anchored that session · Mode = *In person* / *Online (async)* (watch recorded videos + work the notebook) / *Studio* (project/poster/P2P working session) · ⛔ = no class.

### Week 1 — Aug 24–28 · Orientation + start of Regression
| Date | Mode | Session |
|---|---|---|
| Mon Aug 24 | In person | Course launch + **nb00** Launchpad (syllabus, grading, Colab, Gemini, AI policy, **P2P preview**, **Kaggle launch**) |
| Wed Aug 26 | In person | **nb01** EDA & Splits |
| Fri Aug 28 | In person | **nb02** Preprocessing Pipelines |

### Week 2 — Aug 31–Sep 4 · Regression
| Date | Mode | Session |
|---|---|---|
| Mon Aug 31 | In person | **nb03** Regression Metrics & Baselines |
| Wed Sep 2 | In person | **nb04** Linear Features & Diagnostics |
| Fri Sep 4 | **Lecture** | **nb05** Regularization (Ridge/Lasso) — live lecture · **M1 Proposal due** |

### Week 3 — Sep 7–11 · Classification I
| Date | Mode | Session |
|---|---|---|
| Mon Sep 7 | ⛔ | Labor Day |
| Wed Sep 9 | In person | **nb06** Logistic Regression & Pipelines |
| Fri Sep 11 | In person | **nb07** Classification Metrics & Thresholding |

### Week 4 — Sep 14–18 · Evaluation spine
| Date | Mode | Session |
|---|---|---|
| Mon Sep 14 | In person | **nb08** Cross-Validation & Model Comparison |
| Wed Sep 16 | In person | **nb09** Tuning + Feature Engineering + Leakage Detection |
| Fri Sep 18 | Studio | Project work + midterm review · **M2 Baseline due** |

### Week 5 — Sep 21–25 · Midterm
| Date | Mode | Session |
|---|---|---|
| Mon Sep 21 | Online (async) | **nb10** Midterm Casebook — self-guided review (no lecture) |
| Wed Sep 23 | **Exam (in person)** | **MIDTERM EXAM** — in person, in class |
| Fri Sep 25 | In person | **nb11** Decision Trees (paired clf + reg) |

### Week 6 — Sep 28–Oct 2 · Ensembles
| Date | Mode | Session |
|---|---|---|
| Mon Sep 28 | In person | **nb12** Random Forests & Importance |
| Wed Sep 30 | In person | **nb13** Gradient Boosting |
| Fri Oct 2 | **Online (async)** | Project studio + watch-ahead — *instructor travel (Chicago)* |

### Week 7 — Oct 5–9 · Selection + Time Series
| Date | Mode | Session |
|---|---|---|
| Mon Oct 5 | In person | **nb14** Model Selection + Test-Set Ceremony + Monitoring (live ceremony) |
| Wed Oct 7 | Studio | **nb15** M3 Walkthrough — project studio (no lecture) |
| Fri Oct 9 | **Online (async)** | **nb16** Time-Series Forecasting (recorded videos + notebook) · **M3 due** |

### Week 8 — Oct 12–16 · Delivery I
| Date | Mode | Session |
|---|---|---|
| Mon Oct 12 | ⛔ | Fall Break |
| Wed Oct 14 | **Online (async)** | **nb17** Data Communication & Poster Design (recorded videos + notebook) |
| Fri Oct 16 | In person | **nb18** Competition Workflow & Kaggle Submission |

### Week 9 — Oct 19–23 · Delivery II + poster start
| Date | Mode | Session |
|---|---|---|
| Mon Oct 19 | In person | **nb19** Deep Learning |
| Wed Oct 21 | Online (async) | **nb20** Course Wrap / Reflection bridge (no lecture) — **content complete** |
| Fri Oct 23 | Studio | Poster studio — build poster from M3 results |

### Week 10 — Oct 26–30 · Poster build
| Date | Mode | Session |
|---|---|---|
| Mon Oct 26 | Studio | Poster studio — figures, narrative, abstract |
| Wed Oct 28 | Studio | Poster studio — structured peer review |
| Fri Oct 30 | Studio | Poster studio — finalization |

### Week 11 — Nov 2–6 · Poster polish + Kaggle push
| Date | Mode | Session |
|---|---|---|
| Mon Nov 2 | Studio | Poster polish + Kaggle leaderboard push |
| Wed Nov 4 | Studio | Dry-run presentations |
| Fri Nov 6 | Studio | Final poster QA |

### Week 12 — Nov 9–13 · Poster submission + presentation prep
| Date | Mode | Session |
|---|---|---|
| Mon Nov 9 | Studio | Final poster QA → **Poster due Tue Nov 10** |
| Wed Nov 11 | Studio | Presentation practice |
| Fri Nov 13 | Studio | Logistics + presentation coaching |

### Week 13 — Nov 16–20 · URC + P2P kickoff
| Date | Mode | Session |
|---|---|---|
| Mon Nov 16 | Studio | Final presentation prep |
| **Tue Nov 17** | **Conference** | **URC Poster Presentation — all students present** |
| Wed Nov 18 | Build sprint | **P2P kickoff** — scoping, partner problem framing, AI-assistant assignment, product spec |
| Fri Nov 20 | Build sprint | **P2P** — data engineering + model validation for the product |

### Week 14 — Nov 23–27 · Kaggle close + Thanksgiving
| Date | Mode | Session |
|---|---|---|
| Mon Nov 23 | **Online (async)** | **Course Case Competition — finalize & conclude** (Kaggle final submission, 11:59 PM) |
| Wed Nov 25 | ⛔ | Thanksgiving |
| Fri Nov 27 | ⛔ | Thanksgiving |

### Week 15 — Nov 30–Dec 4 · P2P build
| Date | Mode | Session |
|---|---|---|
| Mon Nov 30 | Build sprint | **P2P** — deployment + partner checkpoint |
| Wed Dec 2 | Build sprint | **P2P** — usability testing + iteration |
| Fri Dec 4 | Build sprint | **P2P** — executive brief drafting |

### Week 16 — Dec 7–11 · Showcase + closeout
| Date | Mode | Session |
|---|---|---|
| Mon Dec 7 | Build sprint | **P2P** — showcase preparation |
| Wed Dec 9 | Showcase | **P2P SHOWCASE** — partners + feedback |
| Fri Dec 11 | In person | Course wrap — peer evaluation + reflection survey (Kaggle already concluded Nov 23) |

**Finals week (Dec 14–19):** no final exam (the midterm is the only exam); buffer for late deliverables and grading.

### Comparison with Fall 2025 pacing (what changed and why)

The Fall 2025 offering (`_syllabus/2025F/mgmt474_fall2025_schedule.md`) spread ~9 topics across the semester with twice-weekly in-class sessions + weekly homework, and **taught deep learning in December, *after* the conference**; its case-competition rank submission closed **Nov 30**. Fall 2026 keeps the proven beats but re-orders for the Nov 17 URC requirement:

- **All content finishes before the conference** (by Oct 21) instead of running into December — the poster needs the full toolkit (incl. nb19 deep learning) in hand by early November.
- **Kaggle concludes Nov 23** (was Nov 30 in 2025F) so December is a clean Poster-to-Product runway, and the conclusion lands on the online pre-Thanksgiving session.
- **Modality is explicit and travel-aware:** async on Oct 2 (Chicago), Oct 9 & 14 (around Fall Break), and Nov 23 (before Thanksgiving) — all delivered via the existing recorded micro-videos + notebooks, so no live session is lost.
- **No-lecture sessions** (nb10 casebook, nb15 walkthrough, nb20 wrap) free instructor time for milestone/poster support; **nb05 stays a live lecture** because Ridge/Lasso benefits from real-time explanation.

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
**Last updated:** 2026-06-04 · **Maintained by:** Professor Davi Moreira + AI assistants.

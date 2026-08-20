# Syllabus of Record — Fall 2026 (QM 47400)

**The official syllabus is `_syllabus/2026F/2026F_predictive_analytics_purdue_QM474.docx`** (updated 2026-08-17, PDF exported alongside it). `_syllabus/` is gitignored, so the file itself is local-only — this page is the tracked record of what it says.

When the docx and any other artifact disagree — `syllabus.qmd`, `schedule.qmd`, `_project_docs/`, Brightspace copy — **the docx wins** and the other artifact is the thing to fix.

---

## Facts of record

| Field | Value |
|---|---|
| Course | QM 47400 — Predictive Analytics, Fall 2026 |
| Sections | **001 and 002**, both Monday / Wednesday / Friday, **WTHR 114** |
| Term | Aug 24 – Dec 11, 2026 |
| Instructor | Professor Davi Moreira · Young Hall 1019 · dcordeir@purdue.edu |
| **Office hours** | **Mondays 2:30–3:30 p.m. EST**, Zoom `https://purdue-edu.zoom.us/j/9397534582` |
| Appointments | Outlook "Book time with me" link (Virtual — General Office Hours) |
| **Prerequisite** | **MGMT 305 Business Analytics** or a similar statistical foundations course |
| Brightspace | Official source of record for material and announcements |
| Course website | https://davi-moreira.github.io/2026F_predictive_analytics_QM474/ — explicitly **non-official**, supplementary |

### Assessment weights

Attendance 1% · Participation 4% · Quizzes 15% · Midterm Exam 20% · Course Case Competition 20% · Final Project 35% · Poster-to-Product 5%. **No final exam.** Matches `CLAUDE.md` and `DECISIONS.md` Decision 13 — unchanged by the 2026-08-17 update.

### Midterm exam

In person, on paper, during class time; covers material through `nb09`. **The docx states no date** (the schedule pins it to Fri Sep 25). 15 multiple-choice questions, five alternatives each, 45 minutes. Closed book: *no notes, no textbooks, no calculators, no phones, no laptops, no AI tools*. Make-up requests by email with documentation no later than 7 days before the exam.

### Course Case Competition (20%)

Kaggle **Case Competition: Bank Churn**, adapted from the 2024 Kaggle Playground Series (AI-generated synthetic data). Groups of **up to four**; **five submissions per day**.

- **Opens August 28, 2026** — note this is *not* Aug 24; see the discrepancy register below.
- **Final submission deadline November 29, 2026.**
- **Invitation link:** `https://www.kaggle.com/t/e32195d923ae45edbebe05fa5ce57fdd`
- Breakdown: Team Participation 20% · Leaderboard Performance 60% (rank-scaled, AUC = 0.5 earns zero) · Peer Evaluation 20%.

### Final Project (35%)

Group project culminating in a research poster. **The docx currently carries two contradictory Final Project sections** — see the discrepancy register. The later of the two, which matches the course website, is:

Milestone Deliverables 30% · Peer Evaluation 20% · Peer Review 10% · Poster Presentation at the URC 20% · Instructor/TA Evaluation 20%.

Award-winning poster examples: `https://davi-moreira.github.io/applied_projects.html`. Conference info: `https://www.purdue.edu/undergrad-research/conferences/index.php`.

### Poster-to-Product (5%)

Two-week in-class build sprint after the conference: validated model → stakeholder-ready dashboard/app + executive brief, following scope → data engineering → model validation → UX → deployment → usability testing → showcase. Assigned AI assistant per team under human-in-the-loop sign-offs. **Showcase Wednesday, December 9, 2026.** Funded by a **Mitch Daniels School of Business Experiential Learning Grant**. Breakdown: Deliverables and Showcase 80% (NACE competencies — Technology, Teamwork, Communication, Critical Thinking) · Peer Evaluation 20%.

### Extra credit (not published on the course website)

1. **Course evaluations** — screenshot of the midterm and/or final evaluation confirmation earns **+0.5%** on the final Participation grade.
2. **Issues in course materials** — **+0.25%** toward final Participation per confirmed issue, reported by email by **Fri Dec 4, 11:59 pm**; upload a PDF of the email thread with the instructor's confirmations in the last week of class.
3. **DataCamp — up to 5% of the overall course grade.** Every enrolled student gets a six-month subscription. Each fully completed course = **1%**, maximum five. Submit the Statement of Accomplishment PDFs on Brightspace by **Fri Dec 4, 2026, 11:59 pm**. Only courses completed during this term count; partial completions earn nothing; courses must be completed independently, and **no two may share a completion date or fall within two days of each other**.

### Grade challenges

Within **3 calendar days** of release; **1 calendar day** during the last week of class. Grades are never discussed in the classroom.

### AI policy

Encouraged for learning; **not allowed during exams**. Refine prompts, ask for explanations rather than solutions, verify output (errors are the student's responsibility), and **always cite AI use** in a short note at the end of any document.

---

## Discrepancy register — open items for Davi

These are contradictions *inside* the official docx or between it and other artifacts. None are fixed automatically; each needs Davi's decision.

| # | Issue | Where | Impact |
|---|---|---|---|
| 1 | ✅ **RESOLVED 2026-08-20** (verified: no "May 18", "June 12", "Day 0", or Summer-repo links remain in the docx). ~~The embedded "TENTATIVE COURSE SCHEDULE" was the Summer 2026 4-week intensive table~~ — "May 18 – June 12, 2026", Day 0–20, Colab links pointing at the `2026Summer_predictive_analytics_purdue_MGMT474` repo. Entirely the wrong offering. | syllabus docx, final section | **High.** Students would read a May–June calendar with dead notebook links. Replace with the Fall table now in `2026F_predictive_analytics_QM474_schedule.docx`. |
| 2 | ✅ **RESOLVED 2026-08-20** by Brightspace: the live *Peer Review Submission* proves the 30/20/10/20/20 version is operative. ~~Two contradictory "Final Project" sections.~~ The first says conference presentation is **required**, poster due Tue Nov 10, breakdown 40/20/40. The second says presenting is **"not required"** but encouraged, and uses the 30/20/10/20/20 breakdown. | syllabus docx | **High.** The two disagree on both the requirement and the grade split. The website publishes the 30/20/10/20/20 version and treats presentation as required. |
| 3 | ✅ **RESOLVED 2026-08-20** (docx now reads Aug 24). ~~Kaggle opens "August 28, 2026" in the docx;~~ the course website and prior planning docs said the competition opens **Aug 24** (first day of class). | docx vs. site/plan | Medium. Pick one; Aug 28 is a Friday (first Group Work session), Aug 24 is day one. |
| 4 | ✅ **RESOLVED 2026-08-20.** ~~Typo: "after August 248, 2026"~~ in the DataCamp extra-credit rule. | docx, extra credit §3 | Low — but it is the eligibility start date, so it should read Aug 24 or Aug 28 to match #3. |
| 5 | Typo: "within **1 calendar days**". | docx, grade challenges | Low. |
| 6 | Office hours are **Mon 2:30–3:30 EST** in the docx; the website now says only "details on the course Brightspace" (changed 2026-08-17 at Davi's request). | docx vs. site | None — intentional. The docx and Brightspace carry the time; the site defers to them. |
| 7 | The docx keeps the **Poster-to-Product 80/20 breakdown** and the **competition 20/60/20 breakdown**; the website dropped both in the 2026-08-17 trim. | docx vs. site | None — intentional. The docx is the fuller document. |
| 8 | Prerequisite (**MGMT 305**), section numbers, room (**WTHR 114**), the **Kaggle invitation link**, the **poster examples link**, and the whole **extra-credit section** appear only in the docx. | docx | Low. The site links to Brightspace for these; noted here so they are not lost. |

| 9 | **The docx still says the midterm covers "cross-validation with 95% confidence intervals".** That is retired claim W1 in `CV_INFERENCE_DOCTRINE.md`; the fold interval is descriptive, not a confidence interval for true performance. `schedule.qmd`, `syllabus.qmd`, the midterm README, and the published site were corrected on 2026-08-20, so the docx is now the **only** artifact still carrying it. | docx, Midterm Exam section | Medium. Suggested replacement: "cross-validation and paired model comparison". Not edited automatically because the file was open in Word. |

---

**Last updated:** 2026-08-20 (register reconciled against Brightspace); facts of record last read 2026-08-17 from `2026F_predictive_analytics_purdue_QM474.docx` (modified 2026-08-17 16:54).

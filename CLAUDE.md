# 2026 Fall Predictive Analytics — AI Assistant Guide

This file documents the rules and workflows that change Claude's behavior in this repository. Reference material lives in linked files — read those when relevant, not by default.

## Project Mission

**QM47400 — Predictive Analytics**, a full-semester course for Purdue's Daniels School of Business, **Fall 2026** (Aug 24 – Dec 11, 2026). In-person **Monday / Wednesday / Friday** class meetings, with the course's micro-videos (≤12 min) and Google Colab notebooks as the hands-on spine. Pedagogy: Concept → Demo → PAUSE-AND-DO Practice → Solution → Repeat.

The same **21-notebook arc (nb00–nb20)** from the 4-week intensive offering is **re-paced across ~15 weeks** — notebook content is unchanged; only the calendar and surrounding project/studio structure differ. Two dates dominate the calendar: course content completes by **~Oct 30**, the **Fall Undergraduate Research Conference poster presentation is Tue Nov 17** (all students present; poster due Nov 10), and the post-poster **Poster-to-Product** build sprint (deployed dashboard/app + executive brief, funded by a Daniels Experiential Learning Grant) runs Nov 18 – Dec 11.

- **Instructor:** Professor Davi Moreira
- **Repository:** https://github.com/davi-moreira/2026F_predictive_analytics_QM474
- **Website:** https://davi-moreira.github.io/2026F_predictive_analytics_QM474/
- **Deployment:** Quarto → `docs/` → GitHub Pages
- **Master plan:** `_project_docs/MGMT47400_FullSemester_Plan_2026Fall.md`

## See Also (Reference Files)

| File | When to read |
|---|---|
| `_project_docs/COURSE_MATERIAL_WORKFLOW.md` | Producing a notebook's full material set end-to-end — notebook → videos → Brightspace page → NotebookLM splits → quizzes (the per-notebook production pipeline + dependency order) |
| `_project_docs/NOTEBOOK_TEMPLATE.md` | Creating or restructuring a notebook — full 8-section templates |
| `_project_docs/DECISIONS.md` | Before proposing changes to conventions (seeds, splits, format) |
| `_project_docs/TROUBLESHOOTING.md` | Render fails, GitHub Pages stale, Colab errors, leaked solutions |
| `CONVERSATION_LOG.md` | Project history and prior decisions |
| `_project_docs/MGMT47400_FullSemester_Plan_2026Fall.md` | The master course plan (source of truth for sequencing, Fall 2026 calendar, milestones, Poster-to-Product) |
| `_project_docs/claude_course_plan.md` | Implementation plan with notebook-content justification |
| `scripts/audit_cv_first.py` | Run before every commit in nb09–nb20 |
| `scripts/voice_check_guides.py` | Run before every video-guide edit |
| `scripts/audit_answer_length.py` | Run before importing ANY quiz/exam CSV to Brightspace (MC answer-length cue gate) |
| `scripts/_distractor_rewrite_instructions.md` | Authoring/rewriting MC distractors — the full length-parity spec |

**Canonical notebook reference:** `notebooks/nb01_eda_splits_student.ipynb`. Match its formatting exactly.

---

## 🚨 CRITICAL RULE — Voice and Audience in Student-Facing Content

**The student notebook is read BY students, not BY instructors who then teach it.** Every sentence in a student notebook — including Gemini prompts and "After running, verify" checklists — must be written **TO the student**, never ABOUT the student and never TO the instructor.

**Hard rules:**

1. **Never write "students" as a third-party noun inside a student-facing cell.** If the text says "so students see X", "help students understand Y", "when students run this", or "as students work through", it is wrong. Rewrite in second person (`you`), neutral imperative (`print X to see Y`), or first person (`I want to see X`).
2. **Gemini prompts are scripts the student copies into Gemini.** They must sound like something a student would actually type. *Wrong:* `"... print classification_report so students see the per-class breakdown."` *Right:* `"... print classification_report to show the per-class breakdown."`
3. **No instructor-voice, video-guide, or camera language in student cells.** Forbidden phrases in student notebooks: `"on camera"`, `"the instructor should"`, `"speaking prompt"`, `"you (the instructor)"`. Those belong only in `video_guides/NN_video_lecture_guide.md` (gitignored, instructor-facing).
4. **The video guide can reference students in the third person** — wrapper prose is read silently by the instructor, so "Students often ask…" is fine there. But **inside blockquote read-aloud scripts** (`> *"..."*`), the listener IS a student, so the student-notebook rule applies.

**Before shipping any edit to a student notebook**, grep for failure modes:

```bash
# Should return zero hits in any notebooks/*_student.ipynb (Student's t is the only OK match)
grep -iE '\bstudents?\b|\bthe instructor\b|on camera|speaking prompt' notebooks/nbNN_*_student.ipynb
```

**Before shipping any video-guide edit**, run the blockquote-only voice check:

```bash
python scripts/voice_check_guides.py video_guides/NN_video_lecture_guide.md
```

Hits in wrapper prose (lines not starting with `>`) are fine — only blockquote violations are flagged.

**The most common regression:** trailing `"so students see"` / `"so students understand"` in Gemini prompts. If you feel the urge to explain *why* Gemini should print something, say `"... to show the per-class breakdown"` — the justification is part of the prompt, not a side-note about the audience.

---

## 🚨 CRITICAL RULE — Narrative Polish Pattern (nb08 Style)

Every student-notebook markdown cell follows the nb08 narrative style. This is the course's voice — applied consistently across all 21 notebooks.

**Five structural elements every student notebook has:**

1. **Business-case "Why This Matters" cell** with a named stakeholder (HomeValue CFO, MedScreen chief medical officer, TechCorp People Analytics lead). The stakeholder's concern is phrased as a direct quote. This cell opens the analytical work and motivates every section below.
2. **Narrative prose over bullet lists** — "Reading the output" cells are paragraphs, not terse enumerations. A bullet list is a fallback when the structure is genuinely list-like (a rubric, a checklist); flowing prose is the default.
3. **Inline Q&A blocks** with the exact phrase **"A question that often comes up here"** (or "A question that often comes up at this point"). Placement: after each dense explanation, anticipate one specific student confusion and answer it in one paragraph. The phrase is grep-findable for tooling. **Format (nb09 convention — load-bearing, do not deviate):**

   ```markdown
   > **A question that often comes up here:** *"<student question in double quotes>"* <single paragraph of flowing prose — concrete examples, decision rules, named stakeholders where relevant; no bullets, no nested lists, no headers>.
   ```

   Four required elements: (1) `>` blockquote prefix; (2) `**A question that often comes up here:**` (or `at this point:`) as a bolded opener ending in a colon; (3) italicized question in double quotes: `*"..."*`; (4) answer body as one flowing paragraph in the same blockquote. If the answer needs to enumerate options, fold them inline as `(1) ..., (2) ..., or (3) ...` rather than breaking out a numbered list — the single-paragraph shape is part of the convention. To retrofit older inline-paragraph Q&As to this format, run `python scripts/qa_format_to_nb09.py <notebook>` — it is idempotent.
4. **Section bridges** that explicitly name the transition: *"Section 2 landed the regression estimate with a tight CI. Now apply the identical four steps to the classification problem."* Never jump between sections without a one-sentence bridge.
5. **Warm wrap-ups with next-notebook bridges** — the "Wrap-Up" cell ends with a paragraph naming the next notebook and what it builds on today's work. Often carries one closing Q&A.

**When polishing is warranted:**
- Any new markdown cell longer than ~150 words in a student notebook.
- Any "Reading the output" cell currently a bullet list.
- Any abrupt section transition.
- Any "Why This Matters" cell lacking a named stakeholder.

**Idempotent polish helper** (the pattern used across every NB polish batch):

```python
def append_qa_if_missing(nb, signature_prefix, qa_block):
    for c in nb['cells']:
        if c['cell_type'] != 'markdown':
            continue
        src = ''.join(c['source'])
        if not src.lstrip().startswith(signature_prefix):
            continue
        if 'A question that often comes up' in src:
            return False  # already has Q&A — idempotent
        stripped = src.rstrip()
        if stripped.endswith('---'):
            stripped = stripped[:-3].rstrip()
        c['source'] = [stripped + '\n\n' + qa_block + '\n\n---\n']
        return True
    return False
```

The idempotent check (`if 'A question that often comes up' in src`) is critical — it prevents duplicating Q&As on re-runs.

**Batching rule:** polish in groups of 2–3 notebooks per commit. Polish + voice-check + render + commit per batch. Keeps commit messages meaningful and docs rendering in sync.

---

## 🚨 CRITICAL RULE — CV-First Evaluation + Test-Set Lock

**From nb09 onward, all model-performance claims come from cross-validation.** Before nb14, the test set (`X_test`, `y_test`) is *locked* — no model evaluation touches it. nb14's "Opening the Locked Test Set" ceremony is the one and only authorized test-set opening in the entire course.

| Where | What to use |
|---|---|
| nb01–nb07 | Single train/val/test split is introduced; `X_val` for mid-course evaluation |
| nb08 | k-fold CV + Student's *t* 95% CI becomes the course's evaluation spine |
| nb09–nb13, nb15, nb16, nb17 | `cross_val_score`, `cross_val_predict`, `GridSearchCV`, `RandomizedSearchCV` on `X_train`; held-out evaluation uses `X_val`, never `X_test` |
| **nb14 cell 33 ONLY** | `X_test` / `y_test` opened for the one-shot ceremony (INSIDE/ABOVE/BELOW verdict) |
| nb18 | `X_test` may appear in the Kaggle-submission demo (production-pipeline pattern, not model evaluation) |
| nb20 | No model evaluation — peer review + postmortem |

**The CV-first principle is not a style preference; it is the course's pedagogical spine.** nb14's ceremony loses its meaning if the test set has been touched 30 times before students get there.

**Before shipping any evaluation code in nb09–nb20**, run the audit:

```bash
python scripts/audit_cv_first.py
```

The only acceptable output is hits in `nb14` cell 33 plus `nb18`'s Kaggle-submission demo. Anything else is a regression and must be fixed before commit.

**Common CV-first patterns to reach for:**

- Classifier comparison: `cross_val_score(model, X_train, y_train, cv=StratifiedKFold(5, ...), scoring='roc_auc')`, then report `mean ± (t_crit * sd / sqrt(k))` as a 95% CI.
- `classification_report` on held-out predictions: `y_pred = cross_val_predict(model, X_train, y_train, cv=cv_strat)` — every prediction comes from a fold that never saw it during fitting.
- Permutation importance that would otherwise touch `X_test`: split `X_train` further (e.g., 75/25 inside the cell), fit on the 75% slice, measure permutation importance on the 25% slice. Test set stays locked.
- Calibration that needs a held-out sample: use `CalibratedClassifierCV(base, cv=5)` fit on `X_train` (internal CV handles the calibrator fit), evaluate Brier on `X_val`.

---

## 🚨 CRITICAL RULE — MC Option-Length Parity (Quizzes and Exams)

**The correct answer must not be identifiable by its length or elaboration.** This actually happened in the 2026Summer offering: correct options were authored as full decisions-with-rationale while distractors stayed terse one-liners. Students discovered that "always pick the longest option" scored \~100% (correct-is-longest in 96% of quiz questions and 99.5% of midterm questions vs. 25% chance — hypothesis-tested at p < 10⁻¹²³; see `_project_docs/DECISIONS.md` Decision 11). All inherited banks were rewritten on 2026-06-12; this rule keeps it fixed.

**Hard rules for every multiple-choice question (quizzes, midterm, any future exam):**

1. **Every option ≥ 60% of the length of that question's longest option.** Distractors carry their own flawed-but-specific rationale at the same elaboration and connector-word density as the correct option — wrongness comes from a real misconception, never from brevity, vagueness, or "always/never" tells.
2. **Per bank, the correct option is strictly longest in ≤ 40% of questions** (target \~25%, chance). Vary the correct option's length rank — it must land at longest, middle, and shortest across the bank, and the longest option's position must vary.
3. **Full authoring spec:** `scripts/_distractor_rewrite_instructions.md` (also embedded in the quiz and midterm generation plans, §4.5 and §5.6).

**Before importing ANY quiz or exam CSV to Brightspace**, run the gate — PASS is mandatory:

```bash
python scripts/audit_answer_length.py --file <path-to-csv>   # per-bank gate (PASS/FAIL)
python scripts/audit_answer_length.py                        # corpus-wide statistics
```

---

## 🚨 CRITICAL WORKFLOW — Instructor-First Notebook Editing

**ALWAYS edit `notebooks/nbNN_*_instructor.ipynb` FIRST, then generate the student file.**

- The **instructor notebook** is the source of truth (gitignored, local only).
- The **student notebook** (`nbNN_*_student.ipynb`) is generated from the instructor notebook by deleting solution cells. Only the student file is committed.

**Generating the student notebook:**

1. Copy the instructor file: `cp notebooks/nbNN_*_instructor.ipynb notebooks/nbNN_*_student.ipynb`.
2. Delete all cells containing `INSTRUCTOR SOLUTION` in the student copy (markdown or code).
3. Update the Colab badge URL to match the student filename.
4. Update the video guide (`video_guides/NN_video_lecture_guide.md`).
5. Commit only the student notebook (instructor notebooks are gitignored).

**Marker conventions in the instructor notebook:**

- Markdown solution headings: `### INSTRUCTOR SOLUTION — Exercise N`.
- Code solution cells: `# INSTRUCTOR SOLUTION` as the first comment line.
- Hidden markdown solutions: `<!-- INSTRUCTOR SOLUTION -->` as the first line.
- Student placeholder cells (e.g., `### YOUR FINDINGS HERE:`) MUST NOT contain `INSTRUCTOR SOLUTION`.

**Code-exercise block structure** (in the instructor notebook — the student copy strips cells 4–6):

1. `## 📝 PAUSE-AND-DO Exercise X` (exercise prompt markdown)
2. `> 💡 Gemini Prompt:` (Gemini suggestion with "After running, verify:" checklist)
3. Student code cell: `# YOUR SOLUTION CODE HERE` (must NOT contain `INSTRUCTOR SOLUTION`)
4. `### INSTRUCTOR SOLUTION — Exercise X` (heading; removed from student)
5. `# INSTRUCTOR SOLUTION` code cell (solution; removed from student)
6. `<!-- INSTRUCTOR SOLUTION -->` "Reading the output" markdown (removed from student)

See `_project_docs/NOTEBOOK_TEMPLATE.md` for the full notebook structure and `_project_docs/TROUBLESHOOTING.md` if a solution leaks into the student version.

**NotebookLM markdown sync (auto):** A `PostToolUse` hook in `.claude/settings.json` runs `scripts/sync_instructor_md.sh` after any `Edit`/`Write`/`NotebookEdit` whose path ends in `_instructor.ipynb`, regenerating `_notebook_lm/<basename>.md` for NotebookLM podcast ingestion. The directory is gitignored. For direct Jupyter edits (outside Claude), run `bash scripts/sync_instructor_md.sh` manually, or watch with `fswatch -o notebooks/*_instructor.ipynb | xargs -n1 -I{} bash scripts/sync_instructor_md.sh`.

---

## 🚨 CRITICAL WORKFLOW — Sync Video Guides and Planning Docs

> Producing a **new** notebook's full material set (notebook → videos → Brightspace page → NotebookLM splits → quizzes)? Follow the end-to-end pipeline and dependency order in `_project_docs/COURSE_MATERIAL_WORKFLOW.md`. The rules below are the per-update sync gate within it.

**Every time a notebook (`notebooks/nbNN_*_student.ipynb`) is updated, you MUST:**

1. **Update its video guide** (`video_guides/NN_video_lecture_guide.md`).
   Guides are gitignored — no commit needed, but cell references, speaking prompts, and timestamps go stale fast. Guide structure: At a Glance, Purpose, 9 sections (Why exists, Why after N-1, Why before N+1, Libraries/Tools, Key Concepts, Student Takeaways, Common Questions, Course Arc, Suggested Video Structure with Options A & B). Template: `video_guides/02_video_lecture_guide.md`.
2. **Update planning docs** if the change is significant (added/removed sections, new tools/libraries, reordered content, or shifted dependencies):
   - `_project_docs/MGMT47400_Online4Week_Plan_2026Summer.md` — section "Notebook Sequence Rationale" and dependency diagram.
   - `_project_docs/claude_course_plan.md` — section "Notebook Sequence and Content Justification".

   Minor fixes (typos, wording) do not require planning-doc updates.

---

## 🚨 CRITICAL WORKFLOW — Commit AND Render Webpage

**Every content change MUST be followed by render + commit + push.** GitHub Pages serves `docs/`; without rendering, the website is stale even after `git push`.

```bash
# 1. Commit content changes
git add notebooks/nbNN_topic_student.ipynb  # or schedule.qmd, syllabus.qmd, etc.
git commit -m "feat: Update notebook NN

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# 2. Render Quarto site
/Applications/RStudio.app/Contents/Resources/app/quarto/bin/quarto render

# 3. Commit rendered docs/
git add docs/
git commit -m "build: Render Quarto site

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# 4. Push everything
git push origin main
```

**The most common project-wide mistake** is forgetting step 2/3 — content change is pushed but `docs/` isn't rendered, so the website doesn't update. Always render and commit `docs/` after ANY content change to `.qmd` files, notebooks, images, syllabus, or schedule.

---

## Style Guidelines (Load-Bearing Values)

These values are referenced by tooling and student expectations — do not change casually. See `_project_docs/DECISIONS.md` for rationale.

| Setting | Value |
|---|---|
| Random seed | `RANDOM_SEED = 474` (course number) |
| Train/Val/Test split | 60 / 20 / 20 |
| Figure size | `plt.rcParams['figure.figsize'] = (10, 6)` |
| Display precision | `pd.set_option('display.precision', 3)` |
| Money in markdown cells | Always escape: `\$50,000` (unescaped `$` triggers LaTeX in Colab) |
| Tildes in markdown cells | Always escape: `\~341 patients`, `(\~0.52)` (unescaped `~` is interpreted as strikethrough or as a non-breaking space by Pandoc/Quarto and rots the rendered output) |
| Emoji vocabulary | `✓` success, `⚠️` warning, `📝` exercise, `💡` insight |

## Naming and Commit Conventions

- **Student notebooks (committed):** `nbNN_topic_student.ipynb`
- **Instructor notebooks (gitignored):** `nbNN_topic_instructor.ipynb`
- **Variables:** `lowercase_with_underscores`. **Constants:** `UPPERCASE`.
- **Commit messages:** `<type>: <subject>` where type is `feat`, `fix`, `docs`, `chore`, `build`, `refactor`. Always include `Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>`.
- **Stage specific files** (`git add notebooks/nb09_*.ipynb`) — avoid `git add .` to prevent committing temp files, large CSVs, or secrets.

---

## Anti-Patterns (Do Not Do)

These are the failures that have actually happened in this project. The positive form of most other rules is stated above; what follows is what gets caught in review.

- **Don't commit large files.** No `.zip`, `.mp4`, `.mp3`, `.mov`. No datasets >10 MB — link to external storage.
- **Don't use `git add .`** indiscriminately. Stage by name. Review `git status` first.
- **Don't change the random seed.** Always `RANDOM_SEED = 474`. Different seeds → students get different output → questions on the forum.
- **Don't skip Colab testing.** Click "Open in Colab" → "Runtime → Run all" before committing a notebook.
- **Don't push content without `quarto render` + commit `docs/`.** Website goes stale.
- **Don't leave instructor-solution cells unmarked.** Every excluded cell needs `INSTRUCTOR SOLUTION` somewhere in its source. Unmarked cells leak to students.
- **Don't mix student placeholder and instructor solution in one cell.** Student cell = `# YOUR SOLUTION CODE HERE` only. Solution = SEPARATE cell with `# INSTRUCTOR SOLUTION`.
- **Don't use unescaped `$` for money in markdown cells.** Use `\$50,000`. Colab's MathJax breaks the cell otherwise.
- **Don't use unescaped `~` for "approximately" in markdown cells.** Always escape: `\~341 patients`, `(\~0.52)`. Pandoc/Quarto interpret `~` as a strikethrough delimiter or non-breaking space depending on context, which silently mangles the rendered output. Same rule applies to all markdown content the course renders — student notebooks (markdown cells in `.ipynb`), instructor notebooks, video guides (`video_guides/*.md`), and `.qmd` pages.
- **Don't write fully-justified correct options against terse distractors.** Elaboration leaks correctness: students scored \~100% by always picking the longest option (caught by student reports, 2026Summer). Every option in a question must sit in the same length band, and `scripts/audit_answer_length.py --file <csv>` must PASS before Brightspace import.
- **Don't add complexity that wasn't requested.** No extra features, refactoring, or "improvements" unless asked. Over-engineering confuses students and adds maintenance burden.
- **Don't append to `CONVERSATION_LOG.md` by overwriting** — always append, never replace. Lose history once and you lose it forever.

---

## Quarto Quick Commands

```bash
# Render entire site
/Applications/RStudio.app/Contents/Resources/app/quarto/bin/quarto render

# Preview locally
/Applications/RStudio.app/Contents/Resources/app/quarto/bin/quarto preview

# Render one file
/Applications/RStudio.app/Contents/Resources/app/quarto/bin/quarto render index.qmd
```

---

## ✅ Session End Checklist

Before ending any session that touched course content:

- [ ] All changes committed with clear `<type>: <subject>` messages and `Co-Authored-By:` line.
- [ ] **Voice-check grep run** on any modified student notebook (`grep -iE '\bstudents?\b|\bthe instructor\b|on camera|speaking prompt' notebooks/nbNN_*_student.ipynb` returns zero non-`Student's t` hits). If video guides changed: `python scripts/voice_check_guides.py` is clean.
- [ ] **CV-first audit run** if any nb09–nb20 evaluation code changed: `python scripts/audit_cv_first.py` returns only the nb14 cell 33 + nb18 Kaggle-submission exceptions.
- [ ] **Answer-length audit run** if any quiz/exam CSV was created or edited: `python scripts/audit_answer_length.py --file <csv>` returns PASS for every touched bank.
- [ ] **Narrative polish applied** if any new or rewritten student markdown cells landed: named stakeholder in Why-This-Matters, narrative prose over bullet lists in Reading-the-output, at least one `"A question that often comes up here"` Q&A, warm wrap-up with bridge to the next notebook.
- [ ] **`quarto render` run** if ANY content changed (`.qmd`, notebooks, images), AND `docs/` committed.
- [ ] `CONVERSATION_LOG.md` updated with session summary (appended, not overwritten).
- [ ] If notebooks changed: tested in Colab.
- [ ] `git push origin main` (includes BOTH content AND `docs/`).
- [ ] Clear summary delivered to the user; remaining work listed for next session.

**The two most common end-of-session misses:** forgetting to render Quarto and commit `docs/` (website goes stale), and committing a student-notebook polish without running the voice-check grep (hits get caught in review — cheaper to catch pre-commit).

---

**Last Updated:** 2026-04-28
**Version:** 2.0 — slimmed from 977 lines by extracting reference material into `NOTEBOOK_TEMPLATE.md`, `DECISIONS.md`, `TROUBLESHOOTING.md`, and `scripts/`. Behavior-changing rules and workflows preserved verbatim.
**Maintained by:** Professor Davi Moreira + AI Assistants

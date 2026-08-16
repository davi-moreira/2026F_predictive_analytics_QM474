# The corrected CV-comparison doctrine (2026-08-15)

An independent review found that the course's evaluation spine taught three
statements that are not true. They originate in `nb08` and propagate through
every notebook that compares models. This file is the single source of truth for
what replaces them. Apply it verbatim in spirit — the wording per notebook is
authored to fit that notebook's voice, but the *claims* below are fixed.

## What was wrong

**W1 — "Student's *t* is the conservative choice because the folds are correlated."**
(`nb08` §1, and echoed wherever the CI formula is introduced.)
Student's *t* widens an interval to account for estimating the standard deviation
from few observations. It does nothing about dependence. Because the training
sets of adjacent folds overlap in `k-2` of their `k-1` parts, the fold scores are
positively correlated, and the usual `s/sqrt(k)` **understates** the true
variability. The naive interval is therefore optimistic — too narrow — and *t*
does not repair that. Bengio and Grandvalet (JMLR 2004) show there is no unbiased
estimator of the variance of k-fold CV.

**W2 — "If the two 95% CIs overlap, the models are statistically indistinguishable."**
(`nb08` §Exercise 1, and the decision rule repeated in nb09, nb11-nb14, nb16, nb18.)
Comparing two *marginal* intervals is not a test of the difference between them.
Non-overlap does imply a difference at the stated level, but overlap does **not**
imply the absence of one — two intervals can overlap substantially while the
paired difference is consistently one-signed. Schenker and Gentleman (*The
American Statistician*, 2001) is the standard reference.

**W3 — "A test score INSIDE the CV interval confirms the model generalises."**
(`nb14` ceremony, and the INSIDE/ABOVE/BELOW verdict wherever it appears.)
An interval around a *mean of fold scores* is not a prediction interval for a
*different* statistic computed on a *different* sample. A single test score
landing inside it is weak evidence at best, and the interval was already too
narrow by W1.

## What we teach instead

**C1 — Report the fold spread honestly, and name it descriptively.**
Keep `mean ± t_crit * s / sqrt(k)`. Keep calling the arithmetic what it is. But
label it a **descriptive interval** or **approximate 95% interval**, and state
once per notebook that it is optimistic because folds share training data. The
number is still the right thing to report; the certainty claim is what changes.
Never call it "the 95% confidence interval for the model's true performance".

**C2 — Compare models on paired per-fold differences, not on two marginal intervals.**
Score both candidates on the **identical** folds (same splitter, same seed).
For each fold compute `d_i = score_A(i) - score_B(i)`. Then:

- If every `d_i` has the same sign and the mean difference is larger than the
  margin in C3, the winner is consistent across folds — call it a real difference.
- If the `d_i` change sign across folds, the two models trade places depending on
  which rows they saw, and the comparison does not support a winner.

This is a small mechanical change — subtract per fold before summarising — but it
removes the fold-to-fold variation shared by both models, which is exactly the
noise that made the marginal intervals look wide. Report the paired mean
difference with its own descriptive interval, carrying the same W1 caveat.

**C3 — Predeclare a practical-equivalence margin, and the parsimony tiebreak survives.**
Before comparing, write down the smallest difference that would change the
business decision — 0.01 ROC-AUC, $2,000 of MAE, whatever the stakeholder's
problem implies. If the paired difference does not clear that margin, the models
are **practically equivalent**, and the simpler, cheaper, more interpretable one
wins. That is the same parsimony rule the course has always applied; only the
statistical justification underneath it changes, and it is now the honest one:
"the difference is too small to matter here", not "the intervals overlapped so
there is no difference".

**C4 — The test-set ceremony compares against the predeclared tolerance, not the CV interval.**
Open the locked test set once, report the score, and judge it against the
business tolerance agreed in C3 — plus the CV mean as a rough expectation, stated
as such. Keep the INSIDE / ABOVE / BELOW vocabulary if it is useful as a shorthand
for "close to what CV suggested / better / worse", but it is a **sanity check and
a description**, never a statistical proof of generalisation and never a
deployment gate on its own.

## Where this must be applied

`nb02` (14, 48) · `nb06` (25, 58) · `nb08` (6, 9, 10, 13, 14, 15, 23) ·
`nb09` (10, 11, 13, 17) · `nb11` (11, 28, 29) · `nb12` (19, 35, 38, 45) ·
`nb13` (19, 37) · `nb14` (20, 21, 24, 37) · `nb16` (52, 54, 60, 61) ·
`nb18` (34, 38, 56, 59)

Cell indices are from the **student** notebooks as of 2026-08-15 and are a
starting map, not a guarantee — locate the claim by its wording, not its index.
Also carried in: `CLAUDE.md` (the CV-first rule), `_project_docs/DECISIONS.md`
(Decision 9), the video guides, and the Brightspace pages.

## References

- Bengio, Y., & Grandvalet, Y. (2004). No unbiased estimator of the variance of
  k-fold cross-validation. *JMLR* 5. https://www.jmlr.org/papers/v5/grandvalet04a.html
- Nadeau, C., & Bengio, Y. (2003). Inference for the generalization error.
  *Machine Learning* 52.
- Schenker, N., & Gentleman, J. F. (2001). On judging the significance of
  differences by examining the overlap between confidence intervals.
  *The American Statistician* 55(3). https://doi.org/10.1198/000313001317097960

---

## Authoring rules for anyone applying this correction

A first pass at rewriting the notebooks produced 294 edits, and verification — which *executed* the
notebooks rather than only reading them — rejected a large fraction. Every rejection fell into one of
five patterns. Do not repeat them.

**A1 — Never assert a number you have not computed.** The failed pass wrote sentences like "the
paired fold differences never favour the forest" and "the random forest gives back about 0.007
ROC-AUC". Both were false against the notebook's own output. If a replacement needs a specific
figure, run the cell and read it; if you cannot run it, write the sentence so it does not depend on
the figure ("whether the differences all point the same way is the thing to check in the output
below"). Qualitative and correct beats quantitative and wrong.

**A2 — Keep the three outcomes distinct.** C2/C3 have three, not two:
*same sign and the gap clears the margin* = a real difference;
*signs disagree across folds* = the comparison does not support a winner (inconclusive);
*signs agree but the gap is under the margin* = practically equivalent, simpler model wins.
Collapsing the middle case into "practically equivalent" rebuilds W2 in new words.

**A3 — Declare the margin before the results, once, in one form.** The failed pass routed decisions
through a "business tolerance" that appeared nowhere in the notebook, and stated the rule in three
incompatible ways across cells. Pick one wording, introduce the margin *before* the first comparison
that uses it, and use that same wording everywhere.

**A4 — Prose and code must move together.** The notebooks keep only means and CI half-widths; the
per-fold arrays are discarded. A rule the student cannot execute from any cell's output is not a
rule, it is a slogan. Any notebook whose prose adopts the paired comparison must also expose the
fold arrays and compute the differences — that is a code edit, not only a markdown edit.

**A5 — Sweep the whole notebook, not the mapped cells.** W2 survived in Gemini verify checklists,
wrap-up bullets, and monitoring cards the map did not list, one cell away from an edited paragraph.
Search for the *wording* — overlap, statistically tied, indistinguishable, INSIDE, CI lower bound as
a gate — and fix every instance or none.

**A6 — Instructor copy first.** Per `CLAUDE.md`, the instructor notebook is the source of truth. Use
`scripts/apply_instructor_first.py`, which applies each edit to `*_instructor.ipynb` and refuses the
edit outright if the text is not found there. Instructor solution cells also *print* verdicts
("CIs OVERLAP — not statistically significant"); those need the same correction as the prose.

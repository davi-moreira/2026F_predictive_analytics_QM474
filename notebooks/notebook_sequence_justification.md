## Notebook Sequence and Content Justification

### Design Philosophy

The 21 notebooks (NB00–NB20) follow a **single-layer-at-a-time** principle: each notebook introduces exactly one new concept, assumes only what prior notebooks taught, and prepares exactly what the next one needs. No notebook can be skipped without breaking its successor's assumptions.

The course is organized into a **pre-course orientation** and **four weekly arcs**, each ending with a project milestone that forces students to integrate that week's skills.

---

### Pre-Course — Orientation (NB 00)

**Goal:** Eliminate all setup friction so Day 1 can focus entirely on analytics content.

| NB | What It Teaches | Why Here |
|----|----------------|----------|
| **00** Launchpad: Course Setup | Colab navigation, Gemini Ask→Verify→Document, course structure, environment verification | Day 0 pre-course activity. Students can't engage with any technical content until they understand the platform and AI assistant policy. Separating logistics from analytics prevents NB01 from being overloaded. |

**Arc logic:** Platform fluency → ready for content.

---

### Week 1 — The Regression Arc (NB 01–05)

**Goal:** Build the complete supervised learning workflow from scratch, using regression as the vehicle.

| NB | What It Teaches | Why Here |
|----|----------------|----------|
| **01** EDA & Splits | Statistical learning framework (Y = f(X) + ε), EDA checklist, 60/20/20 splits, leakage vocabulary, bias-variance trade-off | The conceptual foundation. Students can't preprocess, model, or evaluate until they understand predictive analytics concepts, data exploration, and why splitting matters. NB00 handled platform setup; NB01 handles content. |
| **02** Preprocessing Pipelines | Pipeline + ColumnTransformer (impute, encode, scale) | NB01 taught *why* you must fit only on training data; NB02 teaches the *tool* that enforces it. Separating these avoids cognitive overload. |
| **03** Regression Metrics & Baselines | MAE, RMSE, R², DummyRegressor baseline | You must know how to *measure* quality before trying to *improve* it. NB04's feature engineering would be blind without metrics. |
| **04** Linear Features & Diagnostics | PolynomialFeatures, interactions, residual analysis | Now that students can measure improvement, they learn to engineer features — and discover the overfitting problem when 8 features explode to 44. |
| **05** Regularization (Ridge/Lasso) | RidgeCV, LassoCV, coefficient shrinkage/sparsity | The direct solution to NB04's overfitting. These two notebooks form a deliberate **problem → solution pair**. Also hosts the project proposal milestone, closing the regression arc. |

**Arc logic:** Concepts & data workflow → Safe preprocessing → Measurement → Improvement → Control. Each step is prerequisite to the next.

---

### Week 2 — The Classification Arc (NB 06–10)

**Goal:** Pivot to classification, build a richer evaluation toolkit, and learn systematic model comparison.

| NB | What It Teaches | Why Here |
|----|----------------|----------|
| **06** Logistic Regression & Pipelines | Predicted probabilities, threshold sensitivity, regularization via C | The regression-to-classification pivot. Reuses the same Pipeline pattern from Week 1, making the transition seamless. Students need probability foundations before NB07's metrics. |
| **07** Classification Metrics & Thresholding | Precision, recall, F1, ROC/PR curves, cost-based threshold selection | NB06 introduces probabilities informally; NB07 formalizes them into a complete metrics framework. NB08 needs this vocabulary to choose a `scoring` parameter for CV. |
| **08** Cross-Validation | StratifiedKFold, cross_val_score, cross_validate | Replaces the fragile single train/val split with reliable, low-variance estimates. Students must understand standalone CV before NB09 embeds it inside grid search. |
| **09** Tuning & Feature Engineering | GridSearchCV, RandomizedSearchCV, project baseline scaffold | Integration notebook — brings together pipelines, metrics, CV, and tuning into a single workflow. Provides the baseline report template needed for the midterm. |
| **10** Midterm Casebook | Business-case strategy (no new libraries) | Tests *strategic reasoning*, not mechanics: "Given this business problem, what's the target? metric? split? leakage risk?" Creates a natural consolidation pause before Week 3's new algorithms. Project baseline due. |

**Arc logic:** New task type → New metrics → Reliable comparison → Integration → Strategic assessment.

---

### Week 3 — The Ensembles Arc (NB 11–15)

**Goal:** Introduce non-linear models, ensembles, formal model selection, and interpretation.

| NB | What It Teaches | Why Here |
|----|----------------|----------|
| **11** Decision Trees | CART, depth sweep, overfitting demo, tree visualization | The first non-linear model. Students see the bias-variance tradeoff concretely: training accuracy hits 100% while test accuracy degrades. This instability motivates NB12. |
| **12** Random Forests | Bagging, random feature subsets, permutation importance, OOB | Solves the single tree's variance problem by averaging many decorrelated trees. The "parallel ensemble" concept only lands after students experience NB11's instability firsthand. |
| **13** Gradient Boosting | Sequential error correction, learning rate, constrained tuning | Completes the ensemble trilogy. The contrast — bagging reduces variance (NB12) vs. boosting reduces bias (NB13) — is the deepest conceptual point in the course. Also provides the likely champion model. |
| **14** Model Selection Protocol | Formal comparison harness, identical CV folds, test set opened once | Now that the full candidate roster exists (logistic, tree, RF, GBM), a formal protocol replaces the informal "pick the highest number" approach. Premature without all candidates. |
| **15** Interpretation & Error Analysis | Permutation importance, PDP/ICE, segment-level error analysis | Answers "what is the champion learning and where does it fail?" Interpretation only makes sense after committing to one model (NB14). Project improved model due. |

**Arc logic:** Non-linear model → Parallel ensemble → Sequential ensemble → Fair selection → Explain the winner.

---

### Week 4 — The Production Arc (NB 16–20)

**Goal:** Bridge from "model works in a notebook" to "model deployed responsibly and communicated clearly."

| NB | What It Teaches | Why Here |
|----|----------------|----------|
| **16** Decision Thresholds & Calibration | Cost matrices, threshold sweeps, calibration curves, sensitivity analysis | NB15's error analysis reveals *where* the model fails; NB16 teaches how to set thresholds that minimize the *business cost* of those failures. Threshold mechanics are prerequisite for NB17's fairness analysis. |
| **17** Fairness & Model Cards | Slice-based evaluation, group fairness diagnostics, model card documentation | A model with excellent aggregate metrics can still harm specific groups. Threshold choices from NB16 directly affect group-level outcomes — students need to understand thresholds before analyzing their fairness implications. |
| **18** Reproducibility & Monitoring | Function refactoring, joblib serialization, monitoring plan (drift signals, owners) | NB17 adds the ethical layer; NB18 adds the operational layer. Together they form the pre-deployment checklist. Artifacts created here become evidence in NB19's narrative. |
| **19** Executive Narrative & Video Studio | Five-Act Framework (Problem → Approach → Results → Recommendation → Risks), slide storyboard, video script | Translates 18 notebooks of technical work into a compelling non-technical story. Without NB18's artifacts and monitoring vocabulary, the narrative would lack operational credibility. |
| **20** Final Submission & Peer Review | Self-audit checklist, artifact manifest, peer review rubric, postmortem | The capstone: audit your own work, submit the complete package, evaluate a peer's project, and reflect. Closes the course arc from NB00's first Colab session and NB01's first data split to a fully reviewed deliverable. |

**Arc logic:** Better decisions → Ethical audit → Operational readiness → Communication → Delivery and reflection.

---

### Cross-Cutting Design Choices

- **Every week ends with a project milestone** (Proposal → Baseline → Improved Model → Final), ensuring students apply each arc's skills to their own data immediately.
- **The dependency arrows within each week are strict** — each notebook assumes the previous one is mastered. Between weeks, the dependency is softer (consolidation happens at milestone boundaries).
- **Tools are introduced once and reused** — Pipeline appears in NB02 and is used in every subsequent modeling notebook. CV appears in NB08 and is embedded inside grid search in NB09+. This "teach once, reuse always" pattern reduces cognitive load.
- **The course alternates between building and evaluating** — NB02 builds pipelines, NB03 evaluates them. NB04 builds features, NB05 controls them. NB13 builds the final model, NB14 selects it. This rhythm teaches students that construction without evaluation is reckless.

# Milestone 10 — Final Poster Submission

## About the Final Project

The Final Project is a **group capstone** (groups of four, randomly assigned) culminating in a **research poster** and a post-conference **Poster-to-Product** build sprint. Across the term your group completes milestones **M00 through M13** (no gaps in the numbering); each member also submits a confidential intra-group peer evaluation at the end. The project is worth **35%** of the course grade — Milestone Deliverables 30%, Peer Evaluation 20%, Peer Review 10%, Poster Presentation at the conference 20%, Instructor/TA Evaluation 20%. The post-conference **Poster-to-Product** sprint is graded separately as its own **5%** of the course grade. **Presentation at the Purdue Undergraduate Research Conference is required for all students**; the final poster is due nine days before the conference.

---

## What to Submit on Brightspace

| # | File | Description |
|---|------|-------------|
| 1 | **`NN.pdf`** *(e.g., group 03 → `03.pdf`)* | One single PDF — your final poster. There is no need to inform your section number. |

---

## Instructions

1. Review the attached **rubric**, the **Data Communication & Poster Design** material (**nb17**), and the **feedback you received on your first draft (M09)**.
2. **Submission** — submit one single PDF named with your group number (group 01 → `01.pdf`, group 17 → `17.pdf`).

By following these instructions, **the instructor will print your poster for free** in time for the conference.

> **Deadline rationale.** The final poster is due exactly **9 days before** the Undergraduate Research Conference, to leave time for printing and final presentation prep (M11/M12).

---

**Course alignment.** Incorporate the M09 feedback; ensure every claim is backed by the **cross-validated** results from M06/M08; keep the test set out of model selection; and make sure both the **Acknowledgments** and the **AI Use Disclosure** sections are present. Make your stakeholder's decision and your recommended model easy to find. All students present this poster at the conference (required).

**Model comparison (rubric criterion 6).** State the primary metric, the margin δ (the smallest gain that would change your stakeholder's decision, and what it means in their terms), and the order in which you compared models (simplest first). Report each model's fold scores with their mean and SD. Compare models on the same folds and report the mean paired difference. The recommended rule reads the interval corrected for fold overlap, **mean ± t × SD(differences) × √(1/k + 1/(k−1))**; positive differences favor the challenger. Name which of the four outcomes it shows: **worthwhile gain** (the whole interval above δ), **worthwhile loss** (below −δ), **practically equivalent** (inside ±δ), or **unresolved** (anything else). Under this rule, fold wins, overlapping intervals, and a model's own interval or lower bound do not pick the champion. The course announcement has the code.

**Champion (rubric criterion 6).** Name one champion (the baseline can win) and justify it in a short statement that covers four points: what you recommend and for which decision; the evidence (outcome, mean gain, interval, δ); the checks (secondary metrics, cost, interpretability); and what would change your mind. Adopt the more complex model only on a worthwhile gain. If the result is practically equivalent or unresolved, keep the simpler model and say which it was; with the corrected interval, never call an unresolved result "equivalent". With more than two candidates, show the sequence of comparisons that led to the champion.

**Fall 2026 transition.** This note controls criterion 6. The notebooks still teach notebook 08's three-outcome rule; a comparison that applies it correctly earns full credit, as does a champion chosen as notebook 14 teaches and explained for your stakeholder. If you set δ or your criteria after seeing your M06/M08 results, say so: honest disclosure is not penalized. The corrected interval is recommended, not required. A baseline champion or an honest "unresolved" verdict can earn full credit. No new model search or test-set opening is required.

---

Please feel free to let me know if you have any questions.

All the best,

Prof. Moreira

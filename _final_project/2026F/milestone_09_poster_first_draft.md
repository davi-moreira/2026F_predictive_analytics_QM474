# Milestone 09 — Poster First Draft

## About the Final Project

The Final Project is a **group capstone** (groups of four, randomly assigned) culminating in a **research poster** and a post-conference **Poster-to-Product** build sprint. Across the term your group completes milestones **M00 through M13** (no gaps in the numbering); each member also submits a confidential intra-group peer evaluation at the end. The project is worth **35%** of the course grade — Milestone Deliverables 30%, Peer Evaluation 20%, Peer Review 10%, Poster Presentation at the conference 20%, Instructor/TA Evaluation 20%. The post-conference **Poster-to-Product** sprint is graded separately as its own **5%** of the course grade. **Presentation at the Purdue Undergraduate Research Conference is required for all students**; the final poster is due one week before the conference.

---

## What to Submit on Brightspace

| # | File | Description |
|---|------|-------------|
| 1 | **`NN.pdf`** *(e.g., group 03 → `03.pdf`)* | A single-PDF first draft of your poster. No need to inform your section number. |

Use the attached **template** and **rubric**, plus the **Data Communication & Poster Design** material (**nb17**).

---

## 1. Prepare Your Core Content

**a) Title and Authors** — clear, concise title reflecting your research question; all team members' names (plus advisor/mentor acknowledgments).

**b) Abstract / Introduction** — state the research question/problem; provide context and importance; briefly summarize methods (baseline + advanced), data, and main findings.

**c) Methods and Data** — describe your **baseline model** (Linear/Logistic) and **advanced model** (e.g., Random Forest, SVM, Gradient Boosting); summarize the dataset, key variables, preprocessing (feature engineering, missing data); summarize the **hyperparameter-tuning** approach; justify each method against your question. Name your **stakeholder** and the **decision** your model supports, and state your **selection criteria**: the primary metric, the **margin δ** (the smallest gain that would change that decision, and what it means in your stakeholder's terms, e.g., dollars, missed cases, customers), and the order in which you compared models (simplest first). Say when you wrote these down.

**d) Results and Analysis** — report each model's primary metric as its **fold scores, their mean, and their SD**. Compare models on the **same folds**: show the per-fold differences and the interval corrected for fold overlap, read it against ±δ, and name the outcome (worthwhile gain, worthwhile loss, practically equivalent, or unresolved). A chart of the per-fold gains with the ±δ band shaded works well (nb17). Interpret accurately, noting limitations or anomalies.

**e) Conclusions and Future Directions** — **declare your champion** (the baseline can win) in four sentences: what you recommend and for which decision; the evidence (outcome, mean gain, interval, δ); the checks (secondary metrics, cost, interpretability); and what would change your mind. If the comparison is unresolved, say so and explain why you keep the simpler model. Then give implications, possible improvements, and next steps, tied back to your research question.

## 2. Organize Effectively
Logical flow (Introduction → EDA → Methods → Results → Conclusion); tie conclusions to data/analysis; highlight implications for future work. Use headings, bullets, and numbered sections; place visuals where they belong and reference them in text.

## 3. Document Sources & Acknowledge Collaborators
Proper citations for references/data/code; credit sources; acknowledge partners and advisors (TAs, domain experts).

## 4. Design an Effective Visual Presentation
Clean, attractive layout with readable fonts (≥18 pt for main text); high-contrast color scheme; clearly labeled charts/tables (titles, axes, legends); effective white space. Keep text concise; highlight significant results; keep formatting consistent.

## 5. Data Privacy & NDA Compliance
Your poster must **not** contain personally identifiable or sensitive data. In line with any NDA, all detailed data must be permanently deleted upon completion of your project. Any such data on the poster scores 0 on rubric criterion 8 and must be removed before the poster is printed.

## 6. Acknowledgments Section (include on the poster)
As applicable: **Mitch Daniels School of Business** (if it funded your participation); **Professor Davi Moreira** (mentor); **Teaching Assistants**; any other contributing individuals or institutions.
> *Example:* "We thank Professor Davi Moreira for his mentorship throughout the project. We are also grateful to our TAs, [Name] and [Name], for their guidance. This work was supported by the Mitch Daniels School of Business. We also acknowledge the Undergraduate Research Center and Purdue University for this valuable opportunity."

## 7. AI Use Disclosure (include on the poster)
Per the syllabus **AI Policy**, every poster discloses AI use in the template's **AI USE DISCLOSURE** section: name each AI tool you used (e.g., Gemini in Colab), say what it did (code, debugging, text editing, figure design), and state that your group reviewed and verified the output. If you used no AI tools, write *"No AI tools were used."* A poster without this section cannot earn more than 2 of the 5 points in rubric criterion 8.
> *Example:* "We used Gemini in Google Colab to debug our cross-validation code and ChatGPT to tighten the abstract's wording. We reviewed and verified every AI-assisted output and take full responsibility for this poster."

## 8. Submission
Submit one PDF named with your group number — group 01 → `01.pdf`, group 17 → `17.pdf`.

---

**Course alignment.** Your headline numbers come from M06 (baseline) and M08 (tuned model), all **cross-validated** (course rule). Compare the two on **identical folds** with **per-fold paired differences** and the corrected interval against the margin δ, and **name a champion** with a rationale tied to your stakeholder's decision (rubric criterion 6). On this draft criterion 6 gets feedback only; it is scored on the final poster (M10). Keep the test set out of model selection. Apply the six principles + eleven-section poster architecture from **nb17**. This draft gets feedback you incorporate into the final poster (M10).

**Fall 2026 transition.** The notebooks still teach notebook 08's three-outcome rule; a comparison that applies it correctly earns full credit, as does a champion chosen as notebook 14 teaches and explained for your stakeholder. If you set δ or your criteria after seeing your M06/M08 results, say so on the poster: honest disclosure is not penalized. A baseline champion or an honest "unresolved" verdict can earn full credit.

---

Please feel free to let me know if you have any questions.

All the best,

Prof. Moreira

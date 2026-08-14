# QM47400: Predictive Analytics

[![Course Website](https://img.shields.io/badge/Website-Course%20Page-blue)](https://davi-moreira.github.io/2026F_predictive_analytics_QM474/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/davi-moreira/2026F_predictive_analytics_QM474/)

## Course Information

**Instructor:** [Professor Davi Moreira](https://davi-moreira.github.io)
**Email:** dcordeir@purdue.edu
**Office:** Young Hall 1019
**Institution:** Mitch Daniels School of Business, Purdue University

**Course Format:** Full-semester, in-person — **Monday / Wednesday / Friday**
**Term:** Fall 2026 (Aug 24 – Dec 11, 2026)
**Credits:** 3 credit hours

## Course Description

This full-semester course enables students to navigate the entire predictive analytics pipeline skillfully—from data preparation and exploration to modeling, assessment, and interpretation. The hands-on spine is a set of **20 Google Colab notebooks** paired with short **micro-videos (≤12 minutes each)**, exercises, quizzes, and progressive team-project work, all designed to run in **Google Colab with Google Gemini AI assistance** through a "vibe coding" approach: **draft → verify → document**.

Topics include exploratory data analysis, train/validation/test splits, linear and logistic regression, classification metrics, cross-validation and model comparison, regularization, tree-based methods, random forests, gradient boosting, model selection with a locked test-set ceremony, interpretation, time-series forecasting, data communication, competition workflow, and a hands-on introduction to deep learning and large language models.

The course centers on **one comprehensive capstone project** completed in **groups of four randomly assigned members**, plus a **Kaggle case competition** predicting bank customer churn. The project unfolds in two integrated stages:

1. **Research Poster** — milestones M00–M12, culminating in a **required presentation at the Fall 2026 Purdue Undergraduate Research Conference on Tuesday, November 17, 2026** (poster due one week prior, Nov 10).
2. **Poster-to-Product** — a post-conference, two-week in-class build sprint that converts the validated model into a **stakeholder-ready dashboard/app + executive brief**, with corporate-partner feedback and a final showcase (**Wed Dec 9**). *(Supported by a Daniels School Experiential Learning Grant.)*

Master plan and single source of truth for sequencing: [`_project_docs/MGMT47400_FullSemester_Plan_2026Fall.md`](_project_docs/MGMT47400_FullSemester_Plan_2026Fall.md). Milestone reference: [`_final_project/2026F/final_project_milestone_reference.md`](_final_project/2026F/final_project_milestone_reference.md).

## Course Structure

The 20-notebook arc (nb00–nb09 and nb11–nb20; nb10, the midterm casebook, is retired) is paced across ~15 weeks, organized into four units. **Mondays and Wednesdays carry the course content; every Friday is a studio session dedicated to the final-project poster and/or the Course Case Competition** — the single exception is Fri Aug 28, which carries nb02. Lecture content completes on **Mon Oct 26**, and the last two notebooks (nb15 and nb20) are delivered inside the Friday poster studios on Oct 30 and Nov 6, so groups can finalize and present their posters in November.

- **Unit 1 — Regression (nb00–nb05):** Colab/AI workflow, EDA, preprocessing pipelines, regression metrics, linear regression, Ridge/Lasso. *Supports M01 Initial Project Proposal (nb05).*
- **Unit 2 — Classification (nb06–nb09):** Logistic regression, classification metrics, cross-validation, hyperparameter tuning + leakage detection. *Supports M06 Simple Model & Performance Evaluation.*
- **Unit 3 — Ensembles + Selection (nb11–nb15):** Decision trees, random forests, gradient boosting, model selection + test-set ceremony, interpretation. *Supports M08 More Complex Models and the M03 Draft Abstract (nb15).*
- **Unit 4 — Delivery (nb16–nb20):** Time-series forecasting, data communication & poster design, competition workflow, deep learning, course wrap.
- **Poster → URC (Nov):** poster studios, dry-runs, submission (Nov 10), conference presentation (Nov 17).
- **Poster-to-Product (Nov 20 – Dec 9):** build sprint → showcase.

## Learning Approach

The course follows a consistent pedagogical pattern for each topic:

1. **Concept + demo in notebook** (with micro-video)
2. **Guided practice** with a "pause-and-do" exercise
3. **Solution** covering common mistakes + extensions
4. **Next concept + demo** ... and repeat

The course's evaluation backbone is **CV-first**: cross-validation drives all performance claims from nb08 onward, the test set stays locked until nb14's one-shot ceremony, and nb18's Kaggle-submission demo is the only other authorized use of a locked test file.

## Technology Stack

- **Platform:** Google Colab (cloud-based Jupyter notebooks)
- **AI Assistance:** Google Gemini in Colab for guided "vibe coding"
- **Primary Libraries:** `scikit-learn`, `pandas`, `numpy`, `matplotlib` / `seaborn`, `statsmodels`; `PyTorch` and Hugging Face `transformers` in the deep-learning notebook
- **Additional Tools:** Microsoft Copilot (optional productivity enhancement)

All course materials are designed to run directly in Google Colab with no local installation required.

## Course Notebooks

All notebooks run in Google Colab with one-click access and follow a standardized format (logo + instructor header, learning objectives, setup, content sections, PAUSE-AND-DO exercises, wrap-up, bibliography). The canonical reference for notebook structure is `nb01_eda_splits_student.ipynb`. All notebooks use `RANDOM_SEED = 474` for reproducibility. See [`schedule.qmd`](schedule.qmd) for the full session-by-session Fall 2026 calendar.

| NB | Topic | Notebook |
|----|-------|----------|
| 00 | Launchpad: course setup, Colab, Gemini, AI policy | [nb00_launchpad_course_setup_student.ipynb](notebooks/nb00_launchpad_course_setup_student.ipynb) |
| 01 | Predictive analytics fundamentals, EDA, and data splitting | [nb01_eda_splits_student.ipynb](notebooks/nb01_eda_splits_student.ipynb) |
| 02 | Data setup and preprocessing pipelines | [nb02_preprocessing_pipelines_student.ipynb](notebooks/nb02_preprocessing_pipelines_student.ipynb) |
| 03 | Regression metrics and baseline modeling | [nb03_regression_metrics_baselines_student.ipynb](notebooks/nb03_regression_metrics_baselines_student.ipynb) |
| 04 | Linear regression: features, interactions, diagnostics | [nb04_linear_features_diagnostics_student.ipynb](notebooks/nb04_linear_features_diagnostics_student.ipynb) |
| 05 | Regularization (Ridge/Lasso) + Project proposal | [nb05_regularization_project_proposal_student.ipynb](notebooks/nb05_regularization_project_proposal_student.ipynb) |
| 06 | Logistic regression: probabilities, boundaries, pipelines | [nb06_logistic_pipelines_student.ipynb](notebooks/nb06_logistic_pipelines_student.ipynb) |
| 07 | Classification metrics: confusion matrix, ROC/PR, business costs | [nb07_classification_metrics_thresholding_student.ipynb](notebooks/nb07_classification_metrics_thresholding_student.ipynb) |
| 08 | Resampling and cross-validation: comparing models honestly | [nb08_cross_validation_model_comparison_student.ipynb](notebooks/nb08_cross_validation_model_comparison_student.ipynb) |
| 09 | Hyperparameter tuning + feature engineering + leakage detection | [nb09_tuning_feature_engineering_project_baseline_student.ipynb](notebooks/nb09_tuning_feature_engineering_project_baseline_student.ipynb) |
| 11 | Decision trees: interpretable models with sharp edges | [nb11_decision_trees_student.ipynb](notebooks/nb11_decision_trees_student.ipynb) |
| 12 | Random forests: bagging, OOB, feature importance | [nb12_random_forests_importance_student.ipynb](notebooks/nb12_random_forests_importance_student.ipynb) |
| 13 | Gradient boosting: performance with discipline | [nb13_gradient_boosting_student.ipynb](notebooks/nb13_gradient_boosting_student.ipynb) |
| 14 | Model selection + test-set ceremony + monitoring | [nb14_model_selection_protocol_student.ipynb](notebooks/nb14_model_selection_protocol_student.ipynb) |
| 15 | Milestone 03 walkthrough: complex model + tuning + draft abstract | [nb15_milestone_03_walkthrough_student.ipynb](notebooks/nb15_milestone_03_walkthrough_student.ipynb) |
| 16 | Time-series forecasting: walk-forward CV, lag features | [nb16_time_series_forecasting_student.ipynb](notebooks/nb16_time_series_forecasting_student.ipynb) |
| 17 | Data communication and poster design | [nb17_data_communication_poster_student.ipynb](notebooks/nb17_data_communication_poster_student.ipynb) |
| 18 | Competition workflow: notebook to Kaggle submission | [nb18_competition_workflow_student.ipynb](notebooks/nb18_competition_workflow_student.ipynb) |
| 19 | Deep learning + hands-on PyTorch + LLM lab | [nb19_deep_learning_student.ipynb](notebooks/nb19_deep_learning_student.ipynb) |
| 20 | Course end: final submission, peer review, reflection | [nb20_final_submission_peer_review_student.ipynb](notebooks/nb20_final_submission_peer_review_student.ipynb) |

## Textbooks and References

### Primary Textbook
- **James, G., Witten, D., Hastie, T., & Tibshirani, R.** (2023). *An Introduction to Statistical Learning with Applications in Python (ISLP)*. Springer. [Download Here](https://www.statlearning.com/)

### Supporting References
- **Hastie, T., Tibshirani, R., & Friedman, J.** *The Elements of Statistical Learning (ESL)*
- **Provost, F., & Fawcett, T.** *Data Science for Business*
- **Pedregosa et al.** "Scikit-learn: Machine Learning in Python." *Journal of Machine Learning Research*
- **Chip Huyen.** *Designing Machine Learning Systems*
- **scikit-learn User Guide** — pipelines, preprocessing, model selection, metrics, inspection
- **Breiman, L.** "Random Forests"; **Friedman, J.H.** "Greedy Function Approximation: A Gradient Boosting Machine"; **Fawcett, T.** "An introduction to ROC analysis"
- **Hyndman, R.J., & Athanasopoulos, G.** *Forecasting: Principles and Practice* (FPP3)
- **Cole Nussbaumer Knaflic.** *Storytelling with Data*; **Edward Tufte.** *The Visual Display of Quantitative Information*

## Assessment and Grading

| Assessment Component | Weight |
|---------------------|--------|
| Participation | 5% |
| Quizzes | 20% |
| Kaggle Case Competition | 30% |
| Final Project (Poster → Poster-to-Product) | 45% |

### Project Milestones (groups of four randomly assigned members)

Milestone deliverables are due **Sundays, 11:59 PM**, except the final poster, which is pinned to **Tue Nov 10** — exactly 7 days before the conference. The gaps at **M04 / M07 / M13** are intentional (retired meeting-scheduling milestones); do not renumber.

| # | Milestone | Due (Fall 2026) |
|---|-----------|-----------------|
| **M00** | Group Contact Confirmation | Sun Sep 6 |
| **M01** | Initial Project Proposal | Sun Sep 20 |
| **M02** | Expanded Project Outline | Sun Sep 27 |
| **M03** | Project Draft Abstract | Sun Oct 4 |
| **M05** | Applying to the Conference | Sun Oct 11 |
| **M06** | Simple Model & Performance Evaluation | Sun Oct 18 |
| **M08** | More Complex Models & Performance Evaluation | Sun Oct 25 |
| **M09** | Poster First Draft | Sun Nov 1 |
| **M10** | Final Poster Submission (`NN.pdf`) | Tue Nov 10 |
| **M11** | Poster Presentation Planning | Sun Nov 15 |
| **M12** | LinkedIn Post Invitation | Sun Nov 15 |
| — | **URC Poster Presentation — required of every student** | Tue Nov 17 |
| — | Intra-group Peer Evaluation | Fri Dec 11 |

**Poster-to-Product (Fri Nov 20 – Wed Dec 9):** deployed dashboard/app + executive brief, showcase Wed Dec 9. Full instructions and rubrics: [`_final_project/2026F/`](_final_project/2026F/) and [`_adm_stuff/_qm474_poster_product/`](_adm_stuff/_qm474_poster_product/).

### Kaggle Case Competition
- **Competition:** Fall 2026 QM47400 Case Competition: Bank Churn
- **Task:** Predict bank customer churn probability (AUC-ROC)
- **Opens:** Aug 24, 2026 · **Online work session:** Mon Nov 23 · **Deadline:** Sun Nov 29, 2026 at 11:59 PM (Kaggle + Brightspace code submission)

## Getting Started

### For Students

1. **Access the Course Website:** Visit [https://davi-moreira.github.io/2026F_predictive_analytics_QM474/](https://davi-moreira.github.io/2026F_predictive_analytics_QM474/)
2. **Set Up Google Colab:** Ensure you have a Google account and can access [Google Colab](https://colab.research.google.com/)
3. **Start with nb00:** Click the "Open in Colab" button for the Launchpad notebook and follow the setup instructions
4. **Enable Gemini in Colab:** Follow in-notebook instructions to activate Google Gemini AI assistance
5. **Each session:** review the day's micro-videos (Brightspace), open the notebook in Colab, complete the "pause-and-do" exercises, and submit the notebook + concept quiz on Brightspace

### For Instructors

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/davi-moreira/2026F_predictive_analytics_QM474.git
   ```
2. **Quarto Website (optional local preview):**
   ```bash
   quarto preview
   ```
3. **Customize Materials:** All notebooks and Quarto files can be edited to adapt to your context. Sequencing and pacing live in `_project_docs/MGMT47400_FullSemester_Plan_2026Fall.md`.

## Contact Information

**Professor Davi Moreira**
Email: dcordeir@purdue.edu
Office: Young Hall 1019
Course Website: [https://davi-moreira.github.io/2026F_predictive_analytics_QM474/](https://davi-moreira.github.io/2026F_predictive_analytics_QM474/)
Personal Website: [https://davi-moreira.github.io](https://davi-moreira.github.io)

**Brightspace:** Course announcements, video content, quizzes, and assignment submissions are managed through Purdue Brightspace at [https://purdue.brightspace.com/](https://purdue.brightspace.com/)

## License

This course material is licensed under the terms specified in the [LICENSE](LICENSE) file.

---

**Built with [Quarto](https://quarto.org/) | Hosted on [GitHub Pages](https://pages.github.com/)**

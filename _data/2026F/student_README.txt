QM 47400 — Predictive Analytics — Fall 2026
Course data bundle
===========================================

Everything in this archive is also reachable without downloading anything, so
treat this bundle as a convenience: an offline copy, a backup if a download
fails in class, and a way to work outside Google Colab.

WHAT IS IN HERE
---------------

case_competition/
  train.csv              15,000 labelled rows. `Exited` is the target
                         (1 = the customer closed the account, 0 = retained).
  test.csv               10,000 rows, same columns EXCEPT `Exited`. These are
                         the rows you predict.
  sample_submission.csv  The exact format the leaderboard accepts: two columns,
                         `id` and `Exited`, one row per test record.

  Used by: the Fall 2026 QM47400 Case Competition (Bank Churn), which runs the
  whole semester, and by Notebook 18 (Competition Workflow).

  NOTE: These are the same files the Kaggle competition page serves under its
  Data tab. Downloading them from Kaggle yourself is part of the exercise, and
  the competition page is the authoritative source — if the two ever disagree,
  Kaggle wins.

notebook_datasets/
  us_employment.csv      Monthly US employment series (columns: ds, unique_id,
                         y). Used by Notebook 16 (Time-Series Forecasting).
                         The notebook reads this straight from a web address,
                         so you do not need this file unless you are working
                         offline.
  california_housing.csv The California Housing data used across Notebooks
                         01-05, 08, 09, 11-14 and 19 for the HomeValue
                         Analytics business case. Those notebooks load it
                         through scikit-learn (`fetch_california_housing`), so
                         again you only need this file if you are offline.

WHAT IS *NOT* IN HERE, AND WHY
------------------------------

The MedScreen business case (breast-cancer screening) is built into
scikit-learn and downloads itself when the notebook runs
(`load_breast_cancer`). There is no file to distribute.

HOW TO USE IT IN GOOGLE COLAB
-----------------------------

Most notebooks need no upload at all — they fetch their own data. The one
exception is Notebook 18 and your competition work, which expect the
competition files to be present:

  1. Open the notebook in Colab.
  2. Click the folder icon in the left sidebar to open the Files panel.
  3. Click the upload button and add train.csv and test.csv.
  4. Run the notebook from the top.

Uploaded files disappear when the Colab runtime restarts, so you will re-upload
them each session. That is normal.

QUESTIONS
---------
Ask on the course Brightspace page. The syllabus and schedule at
https://davi-moreira.github.io/2026F_predictive_analytics_QM474/
are the source of truth for dates and deadlines.

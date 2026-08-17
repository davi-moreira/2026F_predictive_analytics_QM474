#!/usr/bin/env bash
# Rebuild the Fall 2026 student data bundle from the tracked sources.
# Output: _data/2026F/QM47400_Fall2026_course_data.zip  (gitignored; post to Brightspace)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
COMP="$ROOT/_course_case_competition/2026F/fall-2026-qm-47400-case-competition-bank-churn"
OUT="$ROOT/_data/2026F/QM47400_Fall2026_course_data.zip"
NAME="QM47400_Fall2026_course_data"

for f in train.csv test.csv sample_submission.csv; do
  [ -f "$COMP/$f" ] || { echo "missing competition file: $COMP/$f" >&2; exit 1; }
done
for f in "$ROOT/notebooks/us_employment.csv" "$ROOT/notebooks/california_housing.csv"; do
  [ -f "$f" ] || { echo "missing dataset: $f" >&2; exit 1; }
done

STAGE="$(mktemp -d)/$NAME"
mkdir -p "$STAGE/case_competition" "$STAGE/notebook_datasets"
cp "$COMP"/train.csv "$COMP"/test.csv "$COMP"/sample_submission.csv "$STAGE/case_competition/"
cp "$ROOT/notebooks/us_employment.csv" "$ROOT/notebooks/california_housing.csv" "$STAGE/notebook_datasets/"
cp "$ROOT/_data/2026F/student_README.txt" "$STAGE/README.txt"

rm -f "$OUT"
( cd "$(dirname "$STAGE")" && zip -q -r "$OUT" "$NAME" -x '*.DS_Store' )
echo "built $OUT"
unzip -l "$OUT" | tail -n +2

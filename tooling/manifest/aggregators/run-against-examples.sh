#!/usr/bin/env bash
# run-against-examples.sh — exercise every aggregator against the
# example manifests under ../examples/ and print their output.
#
# Exit 0 if all aggregators succeed (including schema validation).
# Exit non-zero on the first failure.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXAMPLES="$(cd "$HERE/../examples" && pwd)"
PY=${PYTHON:-python3}

run() {
    local title="$1"
    shift
    echo
    echo "============================================================"
    echo "  $title"
    echo "============================================================"
    "$@"
}

run "validate.py" \
    "$PY" "$HERE/validate.py" --root "$EXAMPLES"

run "capability-index.py" \
    "$PY" "$HERE/capability-index.py" --root "$EXAMPLES"

run "bp-traceability.py" \
    "$PY" "$HERE/bp-traceability.py" --root "$EXAMPLES"

run "agent-composition.py" \
    "$PY" "$HERE/agent-composition.py" --root "$EXAMPLES"

run "contract-matrix.py" \
    "$PY" "$HERE/contract-matrix.py" --root "$EXAMPLES"

run "api-catalogue.py" \
    "$PY" "$HERE/api-catalogue.py" --root "$EXAMPLES"

echo
echo "all aggregators succeeded."

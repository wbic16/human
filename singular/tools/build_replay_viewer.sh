#!/bin/bash
# Recreate the static replay viewer bundle from the viewer sources.
# The target bundle directory is the only argument (given by coworld build).
set -euo pipefail
TARGET=$1
ROOT=$(cd "$(dirname "$0")/.." && pwd)
rm -rf "$TARGET"
mkdir -p "$TARGET"
cp "$ROOT/viewer/index.html" "$TARGET/index.html"
echo "replay viewer bundle built at $TARGET"

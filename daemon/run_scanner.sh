#!/usr/bin/env bash
# NetDiscovery Quick Runner Script
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================================="
echo "  NetDiscovery: Local Network Scanner & Metadata Collector"
echo "  Maintainer: Vedant Singh (https://www.sshconnect.space/)"
echo "=========================================================="

# Check Python 3
if ! command -v python3 &>/dev/null; then
    echo "[!] Error: python3 is required."
    exit 1
fi

# Run scanner in continuous loop (pass args through)
python3 scanner.py "$@"

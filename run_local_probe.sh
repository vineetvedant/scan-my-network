#!/usr/bin/env bash
# NetDiscovery Quick Runner for macOS & Linux
# Runs a local discovery scan on your active Wi-Fi / LAN subnet
# and starts the telemetry bridge server so the dashboard can display your devices.
set -e

echo "=========================================================="
echo "  NetDiscovery: Local Network Scanner & Web Bridge        "
echo "  Maintainer: Vedant Singh (https://www.sshconnect.space/)"
echo "=========================================================="

if ! command -v python3 &>/dev/null; then
    echo "[!] Python 3 is required. Please install python3."
    exit 1
fi

echo "[*] Executing subnet discovery scan on your network..."
python3 daemon/scanner.py --once

if [ -f "devices.json" ]; then
    echo "[+] Discovery complete! Starting local telemetry bridge on http://127.0.0.1:8000..."
    echo "[*] Open your dashboard and click 'Connect My Network' to inspect your live network devices."
    python3 -m http.server 8000
else
    echo "[!] Error: devices.json was not generated."
    exit 1
fi

# NetDiscovery Quick Runner for Windows
# Runs a local discovery scan on your active Wi-Fi / LAN subnet
# and starts the telemetry bridge server so the dashboard can display your devices.

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  NetDiscovery: Local Network Scanner & Web Bridge        " -ForegroundColor Green
Write-Host "  Maintainer: Vedant Singh (https://www.sshconnect.space/)" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Cyan

$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "[!] Python is not installed. Please install Python 3." -ForegroundColor Red
    Exit 1
}

Write-Host "[*] Executing subnet discovery scan on your network..." -ForegroundColor Cyan
python daemon/scanner.py --once

if (Test-Path "devices.json") {
    $count = (Get-Content "devices.json" -Raw | ConvertFrom-Json).devices.Count
    Write-Host "[+] Discovery complete! Discovered $count devices on your network." -ForegroundColor Green
    Write-Host "[*] Starting local telemetry bridge on http://127.0.0.1:8000..." -ForegroundColor Cyan
    Write-Host "[*] Open your dashboard and click 'Connect My Network' -> 'Detect Local Probe' to view all your devices." -ForegroundColor Yellow
    python -m http.server 8000
} else {
    Write-Host "[!] Error: devices.json was not generated." -ForegroundColor Red
}

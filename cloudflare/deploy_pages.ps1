# NetDiscovery 1-Click Deployment to Cloudflare Pages (100% Free)
# Requirements: Node.js (npx) installed

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  NetDiscovery: Deploy to Cloudflare Pages (100% Free)    " -ForegroundColor Green
Write-Host "  Maintainer: Vedant Singh (https://www.sshconnect.space/)" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Cyan

$project = Read-Host "Enter your Cloudflare Pages Project Name [default: netdiscovery-live]"
if (-not $project) { $project = "netdiscovery-live" }

Write-Host "[*] Packaging and deploying to Cloudflare Pages Edge..." -ForegroundColor Cyan
npx wrangler pages deploy . --project-name=$project

Write-Host "[+] Deployment successful!" -ForegroundColor Green
Write-Host "[*] Your live dashboard is available at: https://$project.pages.dev" -ForegroundColor Yellow

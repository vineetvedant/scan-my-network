#!/usr/bin/env bash
# NetDiscovery 1-Click Deployment to Cloudflare Pages (100% Free)
set -e

echo "=========================================================="
echo "  NetDiscovery: Deploy to Cloudflare Pages (100% Free)    "
echo "  Maintainer: Vedant Singh (https://www.sshconnect.space/)"
echo "=========================================================="

read -p "Enter your Cloudflare Pages Project Name [default: netdiscovery-live]: " project
project=${project:-netdiscovery-live}

echo "[*] Packaging and deploying to Cloudflare Pages Edge..."
npx wrangler pages deploy . --project-name="$project"

echo "[+] Deployment successful!"
echo "[*] Your live dashboard is available at: https://$project.pages.dev"

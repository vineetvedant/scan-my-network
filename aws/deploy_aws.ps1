param (
    [string]$BucketName = "netdiscovery-telemetry-$((Get-Date).Ticks)",
    [string]$Region = "us-east-1"
)

$ErrorActionPreference = "Stop"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  Deploying NetDiscovery to AWS S3 & CloudFront" -ForegroundColor Cyan
Write-Host "  Bucket: $BucketName | Region: $Region" -ForegroundColor Cyan
Write-Host "=========================================================="

# 1. Create Private S3 Bucket
Write-Host "[*] Creating private S3 bucket: $BucketName..." -ForegroundColor Yellow
if ($Region -eq "us-east-1") {
    aws s3api create-bucket --bucket $BucketName --region $Region
} else {
    aws s3api create-bucket --bucket $BucketName --region $Region --create-bucket-configuration LocationConstraint=$Region
}

# Block Public Access
aws s3api put-public-access-block --bucket $BucketName --public-access-block-configuration `
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

# 2. Upload Web GUI
Write-Host "[*] Uploading index.html and devices.json..." -ForegroundColor Yellow
aws s3 cp index.html "s3://$BucketName/index.html" --content-type "text/html" --cache-control "max-age=3600"
aws s3 cp devices.json "s3://$BucketName/devices.json" --content-type "application/json" --cache-control "no-cache, no-store, must-revalidate, max-age=0"

Write-Host "[+] Successfully provisioned s3://$BucketName/" -ForegroundColor Green
Write-Host "Run the local daemon to sync:" -ForegroundColor Green
Write-Host "python daemon\scanner.py --interval 30 --s3-bucket $BucketName" -ForegroundColor White

#!/usr/bin/env bash
# NetDiscovery Automated AWS S3 + CloudFront Deployment Script
set -e

BUCKET_NAME=${1:-"netdiscovery-telemetry-$(date +%s)"}
REGION=${2:-"us-east-1"}

echo "=========================================================="
echo "  Deploying NetDiscovery to AWS CloudFront & S3"
echo "  Bucket: $BUCKET_NAME | Region: $REGION"
echo "=========================================================="

# 1. Create Private S3 Bucket
echo "[*] Creating private S3 bucket..."
if [ "$REGION" = "us-east-1" ]; then
    aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION"
else
    aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION" --create-bucket-configuration LocationConstraint="$REGION"
fi

# Enable Public Access Block
aws s3api put-public-access-block --bucket "$BUCKET_NAME" --public-access-block-configuration \
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

# 2. Upload Web GUI (index.html) and sample data
echo "[*] Uploading index.html and sample telemetry..."
aws s3 cp index.html "s3://$BUCKET_NAME/index.html" --content-type "text/html" --cache-control "max-age=3600"
aws s3 cp devices.json "s3://$BUCKET_NAME/devices.json" --content-type "application/json" --cache-control "no-cache, no-store, must-revalidate, max-age=0"

echo "[✓] Files uploaded to s3://$BUCKET_NAME/"
echo ""
echo "Next step: Run the local daemon to continuously sync live discovery:"
echo "  python3 daemon/scanner.py --interval 30 --s3-bucket $BUCKET_NAME"

#!/usr/bin/env python3
"""
NetDiscovery Cloud Sync Pipeline
Automates pushing scanned device telemetry to AWS S3 (behind CloudFront)
or dispatching payloads to an AWS API Gateway / Lambda backend.
Enforces strict Cache-Control headers to prevent stale network state caching.
"""

import os
import sys
import json
import argparse
import subprocess
from typing import Optional

def upload_to_s3(
    file_path: str,
    bucket_name: str,
    s3_key: str = "devices.json",
    cloudfront_distribution_id: Optional[str] = None
) -> bool:
    """
    Uploads devices.json to an S3 bucket configured behind CloudFront.
    Ensures Cache-Control headers are explicitly set to no-store/max-age=0.
    """
    if not os.path.exists(file_path):
        print(f"[!] Error: File '{file_path}' does not exist.", file=sys.stderr)
        return False

    print(f"[*] Uploading {file_path} to s3://{bucket_name}/{s3_key}...")

    # Method 1: Boto3 (Python SDK)
    try:
        import boto3
        from botocore.exceptions import ClientError

        s3_client = boto3.client("s3")
        with open(file_path, "rb") as f:
            s3_client.put_object(
                Bucket=bucket_name,
                Key=s3_key,
                Body=f,
                ContentType="application/json",
                CacheControl="no-cache, no-store, must-revalidate, max-age=0",
                Metadata={
                    "scanner": "netdiscovery-daemon",
                    "sync-pipeline": "automated"
                }
            )
        print(f"[+] Successfully synced {s3_key} to s3://{bucket_name}/ via Boto3")

        # Optional CloudFront invalidation if distribution ID provided
        if cloudfront_distribution_id:
            try:
                cf = boto3.client("cloudfront")
                import time
                cf.create_invalidation(
                    DistributionId=cloudfront_distribution_id,
                    InvalidationBatch={
                        "Paths": {
                            "Quantity": 1,
                            "Items": [f"/{s3_key}"]
                        },
                        "CallerReference": str(time.time())
                    }
                )
                print(f"[+] Triggered CloudFront invalidation for /{s3_key}")
            except Exception as e:
                print(f"[!] CloudFront invalidation failed: {e}", file=sys.stderr)

        return True

    except ImportError:
        # Method 2: Fallback to AWS CLI
        print("[*] Boto3 not installed, attempting fallback via AWS CLI...")
        cmd = [
            "aws", "s3", "cp",
            file_path,
            f"s3://{bucket_name}/{s3_key}",
            "--content-type", "application/json",
            "--cache-control", "no-cache, no-store, must-revalidate, max-age=0"
        ]
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if res.returncode == 0:
                print(f"[+] Successfully synced {s3_key} via AWS CLI.")
                return True
            else:
                print(f"[!] AWS CLI error: {res.stderr}", file=sys.stderr)
                return False
        except Exception as e:
            print(f"[!] Failed to execute AWS CLI: {e}", file=sys.stderr)
            return False


def post_to_api_gateway(
    file_path: str,
    api_url: str,
    api_key: Optional[str] = None
) -> bool:
    """
    Option B: Posts the scanned device payload directly to an AWS API Gateway endpoint.
    """
    import urllib.request
    import urllib.error

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            payload_data = f.read().encode("utf-8")

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "NetDiscovery-Daemon/1.0"
        }
        if api_key:
            headers["x-api-key"] = api_key

        req = urllib.request.Request(api_url, data=payload_data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=10) as resp:
            status = resp.status
            if 200 <= status < 300:
                print(f"[+] Payload successfully dispatched to API Gateway (HTTP {status})")
                return True
            else:
                print(f"[!] API Gateway returned HTTP {status}", file=sys.stderr)
                return False
    except urllib.error.URLError as e:
        print(f"[!] API Gateway POST failed: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="NetDiscovery Cloud Sync Utility")
    parser.add_argument("--file", default="devices.json", help="Path to devices.json")
    parser.add_argument("--s3-bucket", help="Target S3 Bucket")
    parser.add_argument("--s3-key", default="devices.json", help="S3 Destination Key")
    parser.add_argument("--cf-dist-id", help="CloudFront Distribution ID for cache invalidation")
    parser.add_argument("--api-url", help="API Gateway URL (Option B)")
    parser.add_argument("--api-key", help="API Gateway API Key (Option B)")

    args = parser.parse_args()

    if args.s3_bucket:
        upload_to_s3(args.file, args.s3_bucket, args.s3_key, args.cf_dist_id)
    elif args.api_url:
        post_to_api_gateway(args.file, args.api_url, args.api_key)
    else:
        print("Please specify either --s3-bucket or --api-url.")
        sys.exit(1)


if __name__ == "__main__":
    main()

terraform {
  required_version = ">= 1.3.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "Target AWS Region"
}

variable "project_name" {
  type        = string
  default     = "netdiscovery-console"
  description = "Project name prefix"
}

# -------------------------------------------------------------
# 1. Private S3 Bucket for Hosting & Telemetry Data
# -------------------------------------------------------------
resource "aws_s3_bucket" "telemetry_bucket" {
  bucket_prefix = "${var.project_name}-"
  force_destroy = true
}

resource "aws_s3_bucket_public_access_block" "telemetry_bucket_pab" {
  bucket = aws_s3_bucket.telemetry_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_cors_configuration" "telemetry_bucket_cors" {
  bucket = aws_s3_bucket.telemetry_bucket.id

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "HEAD"]
    allowed_origins = ["*"]
    expose_headers  = ["ETag", "Cache-Control"]
    max_age_seconds = 3000
  }
}

# -------------------------------------------------------------
# 2. CloudFront Origin Access Control (OAC)
# -------------------------------------------------------------
resource "aws_cloudfront_origin_access_control" "oac" {
  name                              = "${var.project_name}-oac"
  description                       = "OAC for NetDiscovery S3 Origin"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

# -------------------------------------------------------------
# 3. CloudFront Distribution
# -------------------------------------------------------------
resource "aws_cloudfront_distribution" "cf_dist" {
  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"
  comment             = "NetDiscovery Network Telemetry Console"

  origin {
    domain_name              = aws_s3_bucket.telemetry_bucket.bucket_regional_domain_name
    origin_id                = "S3-${aws_s3_bucket.telemetry_bucket.id}"
    origin_access_control_id = aws_cloudfront_origin_access_control.oac.id
  }

  # Default Cache Behavior: Static Web Assets
  default_cache_behavior {
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "S3-${aws_s3_bucket.telemetry_bucket.id}"
    viewer_protocol_policy = "redirect-to-https"
    compress               = true

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    min_ttl     = 0
    default_ttl = 86400
    max_ttl     = 31536000
  }

  # Ordered Cache Behavior: devices.json (Zero Caching for Real-Time Telemetry)
  ordered_cache_behavior {
    path_pattern           = "/devices.json"
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD", "OPTIONS"]
    target_origin_id       = "S3-${aws_s3_bucket.telemetry_bucket.id}"
    viewer_protocol_policy = "redirect-to-https"
    compress               = true

    forwarded_values {
      query_string = true
      headers      = ["Origin", "Access-Control-Request-Headers", "Access-Control-Request-Method"]
      cookies {
        forward = "none"
      }
    }

    min_ttl     = 0
    default_ttl = 0
    max_ttl     = 5
  }

  price_class = "PriceClass_100"

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}

# -------------------------------------------------------------
# 4. S3 Bucket Policy (Allows only CloudFront OAC to Read)
# -------------------------------------------------------------
resource "aws_s3_bucket_policy" "oac_policy" {
  bucket = aws_s3_bucket.telemetry_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "AllowCloudFrontServicePrincipalReadOnly"
        Effect    = "Allow"
        Principal = {
          Service = "cloudfront.amazonaws.com"
        }
        Action   = "s3:GetObject"
        Resource = "${aws_s3_bucket.telemetry_bucket.arn}/*"
        Condition = {
          StringEquals = {
            "AWS:SourceArn" = aws_cloudfront_distribution.cf_dist.arn
          }
        }
      }
    ]
  })
}

# -------------------------------------------------------------
# 5. Dedicated IAM User for Local Daemon with Least Privilege
# -------------------------------------------------------------
resource "aws_iam_user" "daemon_user" {
  name = "${var.project_name}-daemon"
}

resource "aws_iam_access_key" "daemon_key" {
  user = aws_iam_user.daemon_user.name
}

resource "aws_iam_user_policy" "daemon_policy" {
  name = "${var.project_name}-daemon-s3-push"
  user = aws_iam_user.daemon_user.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowPutTelemetryPayload"
        Effect = "Allow"
        Action = [
          "s3:PutObject",
          "s3:PutObjectAcl"
        ]
        Resource = "${aws_s3_bucket.telemetry_bucket.arn}/devices.json"
      }
    ]
  })
}

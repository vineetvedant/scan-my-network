output "s3_bucket_name" {
  value       = aws_s3_bucket.telemetry_bucket.id
  description = "Target S3 Bucket for scanner uploads and hosting"
}

output "cloudfront_domain_name" {
  value       = aws_cloudfront_distribution.cf_dist.domain_name
  description = "CloudFront URL for accessing the dashboard"
}

output "cloudfront_distribution_id" {
  value       = aws_cloudfront_distribution.cf_dist.id
  description = "CloudFront Distribution ID"
}

output "daemon_access_key_id" {
  value       = aws_iam_access_key.daemon_key.id
  description = "Access key for the local scanner daemon"
}

output "daemon_secret_access_key" {
  value       = aws_iam_access_key.daemon_key.secret
  sensitive   = true
  description = "Secret key for the local scanner daemon"
}

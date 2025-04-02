output "s3_bucket_name" {
  value = aws_s3_bucket.model_artifacts.id
}

output "sagemaker_role_arn" {
  value = aws_iam_role.sagemaker_execution_role.arn
}


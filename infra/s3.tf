resource "aws_s3_bucket" "model_artifacts" {
  bucket = "sagemaker-model-artifacts-${random_id.bucket_id.hex}"

  tags = {
    Name = "SageMakerModelArtifacts"
  }
}

resource "random_id" "bucket_id" {
  byte_length = 4
}


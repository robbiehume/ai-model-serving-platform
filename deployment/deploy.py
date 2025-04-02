import sagemaker
from sagemaker.pytorch import PyTorchModel
import boto3
import os

# --------------------------
# Config (adjust these if needed)
# --------------------------
bucket = 'sagemaker-model-artifacts-75a7383a'  # from terraform output
model_artifact = 'model.tar.gz'
role_arn = 'arn:aws:iam::160885254600:role/sagemaker_execution_role'  # from terraform output
region = 'us-east-2'

# --------------------------
# Session
# --------------------------
sagemaker_session = sagemaker.Session()
s3_model_path = f's3://{bucket}/{model_artifact}'

# --------------------------
# Create PyTorch Model using native SageMaker container
# --------------------------
model = PyTorchModel(
    entry_point='inference.py',  # you'll create this next
    source_dir='deployment',
    role=role_arn,
    framework_version='1.12',   # compatible with current SageMaker PyTorch versions
    py_version='py38',
    model_data=s3_model_path,
    sagemaker_session=sagemaker_session
)

# --------------------------
# Deploy Model
# --------------------------
predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.t2.medium',  # free tier eligible if you're careful
    endpoint_name='mnist-endpoint'
)

print("✅ Endpoint deployed successfully!")
print(f"Endpoint Name: {predictor.endpoint_name}")


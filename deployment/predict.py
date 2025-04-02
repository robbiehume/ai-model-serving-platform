#import boto3
#import json
#import numpy as np
#
## --------------------------
## Config
## --------------------------
#endpoint_name = 'mnist-endpoint'   # make sure it matches your deployment
#region = 'us-east-2'
#
## --------------------------
## Create SageMaker Runtime client
## --------------------------
#runtime = boto3.client('sagemaker-runtime', region_name=region)
#
## --------------------------
## Dummy Input (Random Tensor)
## --------------------------
## Normally you would send an actual MNIST image (1x28x28)
## For now, let's send a random tensor shaped correctly
#
#data = np.random.rand(1, 1, 28, 28).tolist()  # Shape: [batch_size, channels, height, width]
#
#payload = json.dumps(data)
#
## --------------------------
## Invoke Endpoint
## --------------------------
#response = runtime.invoke_endpoint(
#    EndpointName=endpoint_name,
#    ContentType='application/json',
#    Body=payload
#)
#
#result = response['Body'].read()
#print("✅ Inference result:", result.decode())

import torch
from torchvision import datasets, transforms
import json
import boto3

# --------------------------
# Config
# --------------------------
endpoint_name = 'mnist-endpoint'
region = 'us-east-2'

# --------------------------
# Load MNIST Sample
# --------------------------
transform = transforms.Compose([
    transforms.ToTensor(),
])

test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
sample_img, _ = test_dataset[0]  # Take the first image

# Prepare input for SageMaker (batch dimension + convert to list)
input_tensor = sample_img.unsqueeze(0)  # Shape: [1,1,28,28]
input_data = input_tensor.numpy().tolist()

payload = json.dumps(input_data)

# --------------------------
# Send to Endpoint
# --------------------------
runtime = boto3.client('sagemaker-runtime', region_name=region)

response = runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType='application/json',
    Body=payload
)

result = response['Body'].read()
print("✅ Inference result:", result.decode())



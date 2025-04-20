# AI Model-Serving Platform (In Progress)

An end-to-end AI model training and serving pipeline for the MNIST dataset using PyTorch and AWS SageMaker.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Tech Stack](#tech-stack)
- [Architecture Diagram](#architecture-diagram)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Infrastructure Provisioning](#infrastructure-provisioning)
- [Training & Packaging](#training--packaging)
- [Deployment](#deployment)
- [Inference](#inference)
- [Sample Output](#sample-output)
- [CI/CD (Planned)](#cicd-planned)
- [Monitoring](#monitoring)
- [Contributing](#contributing)
- [Status & Roadmap](#status--roadmap)

## Prerequisites
- Python 3.8+ (tested on 3.12)
- pip
- Terraform ≥ 1.0.0
- AWS CLI configured (`aws configure`)
- An AWS account with S3, SageMaker, and IAM permissions

## Tech Stack
- AWS SageMaker (Model Hosting)
- PyTorch (Model Training)
- Terraform (Infrastructure as Code)
- AWS CLI & boto3 (Model packaging & inference)
- SageMaker Python SDK (Deployment)
- GitHub Actions (CI/CD) – planned
- AWS CloudWatch (Monitoring)
- Docker (Optional containerization)

## Architecture Diagram
*(TODO: insert diagram illustrating data flow and components)*

## Directory Structure
```text
. 
├── data/             # MNIST data storage
├── model/            # Trained model artifacts
├── infra/            # Terraform IaC for S3 + SageMaker endpoint
├── deployment/       # Deployment & inference scripts
├── train.py          # Model training script
├── requirements.txt  # Python dependencies
└── README.md         # This document
```

## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Infrastructure Provisioning
```bash
cd infra/
terraform init
terraform apply
```
After apply, retrieve the S3 bucket name and IAM role ARN via `terraform output`.

## Training & Packaging
```bash
python train.py
# Produces model/model.pth
tar -czvf model.tar.gz -C model model.pth
aws s3 cp model.tar.gz s3://<bucket-name>/
```

## Deployment
Edit `deployment/deploy.py` to configure `bucket`, `model_artifact`, `role_arn`, and `region`, then:
```bash
python deployment/deploy.py
```
This creates a SageMaker endpoint (default name: `mnist-endpoint`).

## Inference
```bash
python deployment/predict.py
```
Sends the first MNIST test image to the live endpoint and prints the output logits.

## Sample Output
```text
✅ Inference result: [0.00, 0.01, 0.90, 0.02, 0.03, 0.00, 0.00, 0.00, 0.00, 0.04]
```

## CI/CD (Planned)
We plan to add GitHub Actions to automate training, packaging, and deployment on merge.

## Monitoring
Basic CloudWatch metrics and logs are enabled for the endpoint.

## Contributing
Please submit issues or PRs, following existing code style and practices.

## Status & Roadmap
- **Status**: In Progress
- **Roadmap**:
  - Full training pipeline integration
  - Auto-scaling SageMaker endpoints
  - Hyperparameter tuning (SageMaker Experiments)
  - A/B testing and rollout strategies

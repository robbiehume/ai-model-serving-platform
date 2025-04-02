# AI Model-Serving Platform (In Progress)

## Overview
A scalable AI model-serving platform built using AWS SageMaker, Terraform, and CI/CD automation.

## Tech Stack
- SageMaker (Model Hosting)
- PyTorch (Model Training)
- Terraform (Infrastructure)
- GitHub Actions (CI/CD)
- AWS CloudWatch (Monitoring)
- Docker (Optional API or CI/CD usage)

## Features
- Infrastructure as Code (Terraform)
- Simple CNN trained on MNIST dataset
- Automated deployment via GitHub Actions
- SageMaker endpoint deployment
- Real-time inference testing via boto3
- Basic CloudWatch monitoring

## Architecture Diagram

## How to Use
1. Train model (`train.py`)
2. Package model (`tar -czvf model.tar.gz model.pth`)
3. Upload model (`aws s3 cp`)
4. Deploy model (`deploy.py`)
5. Query endpoint (`predict.py`)
6. (Optional) CI/CD pipeline and Monitoring

## Sample Output
- Inference result: `[class probabilities or logits]`

## Status
In Progress

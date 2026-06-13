# MLOps Sentiment Analysis Pipeline

## Overview

This project demonstrates an end-to-end MLOps workflow for a Sentiment Analysis application.

The workflow covers model training, API development, containerization, infrastructure provisioning, automated image delivery and monitoring.

The application accepts text input and predicts whether the sentiment is Positive or Negative.

---

## Tech Stack

### Machine Learning

* Python
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression

### Backend

* Flask

### Containerization

* Docker
* Docker Hub

### Infrastructure

* AWS EC2
* Terraform

### CI/CD

* GitHub Actions

### Monitoring

* Prometheus
* Grafana

---

## Project Architecture

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
Docker Hub
   │
   ▼
AWS EC2
   │
   ├── Flask API (Docker Container)
   │
   ├── Prometheus
   │
   └── Grafana
```

---

## Features

* Train a sentiment analysis model using TF-IDF and Logistic Regression
* Serve predictions through a Flask REST API
* Containerize the application using Docker
* Store container images in Docker Hub
* Provision infrastructure using Terraform
* Deploy application on AWS EC2
* Automate Docker image build and push using GitHub Actions
* Monitor services using Prometheus and Grafana
* Automatically recover services after EC2 restart

---

## Project Structure

```text
project-3-mlops-pipeline/
│
├── app.py
├── train_model.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── terraform/
│   ├── main.tf
│   ├── provider.tf
│   ├── variables.tf
│   └── outputs.tf
│
└── .github/
    └── workflows/
        └── docker-build.yml
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "healthy",
  "model": "loaded"
}
```

---

### Sentiment Prediction

```http
POST /predict
```

Request:

```json
{
  "text": "I love this product"
}
```

Response:

```json
{
  "sentiment": "Positive"
}
```

---

## Terraform Deployment

Terraform is used to:

* Create AWS EC2 infrastructure
* Configure security groups
* Expose application ports
* Manage infrastructure as code

---

## CI/CD Workflow

GitHub Actions automatically:

1. Detects changes pushed to the main branch
2. Builds a Docker image
3. Pushes the image to Docker Hub

---

## Monitoring

### Prometheus

Used for metrics collection and service monitoring.

### Grafana

Used for dashboard visualization and monitoring.

Verified after EC2 restart using systemd services and Docker restart policies.

---

## Future Improvements

* Add Node Exporter for host-level monitoring
* Store Terraform state remotely
* Deploy using Kubernetes
* Add automated testing pipeline

---

## Learning Outcomes

Through this project I worked with:

* Machine Learning model deployment
* Docker image management
* AWS EC2 deployment
* Terraform infrastructure provisioning
* GitHub Actions automation
* Prometheus monitoring
* Grafana dashboards
* Service recovery and restart policies

```
```
# project-3-mlops-pipeline
End-to-end MLOps pipeline — ML model training, Docker, Kubernetes (EKS), Terraform, GitHub Actions CI/CD, Prometheus + Grafana monitoring on AWS

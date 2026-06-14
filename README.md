# MLOps Sentiment Analysis Pipeline 

## Overview

End-to-end MLOps pipeline for Sentiment Analysis — from model training to production deployment with full monitoring, CI/CD automation, and Kubernetes orchestration.

---

## Live Architecture

```text
Developer
│
▼
GitHub Repository
│
▼
GitHub Actions (Pytest → Docker Build → Docker Push)
│
▼
DockerHub (sneha24012004/mlops-sentiment-app:v1)
│
▼
AWS EC2 (t3.small, Ubuntu 22.04, 20GB)
├── Flask API (Docker, Port 5000)
├── Nginx Reverse Proxy (Port 80)
├── Prometheus (Port 9090)
├── Grafana + Alerts (Port 3000)
└── Node Exporter (Port 9100)

Kubernetes (Minikube Local)
└── 3 Pods + NodePort Service + Rolling Updates
```

---

## Tech Stack

| Layer            | Technology                                        |
| ---------------- | ------------------------------------------------- |
| ML               | Python, Scikit-learn, TF-IDF, Logistic Regression |
| API              | Flask REST API                                    |
| Containerization | Docker, DockerHub                                 |
| Orchestration    | Kubernetes (Minikube), Rolling Updates            |
| Infrastructure   | AWS EC2, Terraform (IaC)                          |
| CI/CD            | GitHub Actions (Tests + Build + Push)             |
| Monitoring       | Prometheus, Grafana, Node Exporter, CPU Alerts    |
| Web Server       | Nginx Reverse Proxy                               |

---

## Project Structure

```text
project-3-mlops-pipeline/
├── app.py                          # Flask REST API
├── train_model.py                  # ML model training + MLflow
├── Dockerfile                      # Container definition
├── docker-compose.yml              # Multi-container setup
├── requirements.txt                # Python dependencies
├── model/
│   ├── model.pkl                   # Trained model
│   └── vectorizer.pkl              # TF-IDF vectorizer
├── k8s/
│   ├── deployment.yaml             # Kubernetes deployment (3 replicas)
│   └── service.yaml                # Kubernetes NodePort service
├── terraform/
│   ├── main.tf                     # EC2 + Security Groups
│   ├── provider.tf                 # AWS provider
│   ├── variables.tf                # Variables
│   └── outputs.tf                  # Outputs
└── .github/
    └── workflows/
        └── docker-build.yml        # CI/CD pipeline
```

---

## API Endpoints

### Health Check

```http
GET /health
```

**Response**

```json
{
  "status": "healthy",
  "model": "loaded",
  "accuracy": "100%"
}
```

### Sentiment Prediction

```http
POST /predict
```

**Request**

```json
{
  "text": "I love this product"
}
```

**Response**

```json
{
  "sentiment": "Positive",
  "confidence": "83.76%",
  "model": "Logistic Regression + TF-IDF"
}
```

---

## CI/CD Pipeline

GitHub Actions automatically:

1. Runs Pytest automated tests
2. Builds Docker image
3. Pushes to DockerHub
4. Triggers on every push to main branch

---

## Kubernetes Deployment

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl rollout status deployment/mlops-app
```

* 3 Replicas
* NodePort Service
* Rolling Updates Enabled

---

## Monitoring Stack

* **Prometheus** — Metrics collection (CPU, Memory, API health)
* **Node Exporter** — System-level metrics
* **Grafana** — Dashboard visualization
* **Alerts** — High CPU alert configured (threshold: 80%)
* **Auto-restart** — All services reboot-safe via systemd

---

## Infrastructure (Terraform)

```bash
terraform init
terraform plan
terraform apply
```

Provisions:

* AWS EC2 Instance
* Security Groups
* Remote Terraform State Support

---

## Reboot Safety

All services configured with auto-restart:

* ✅ Docker Container (`restart: unless-stopped`)
* ✅ Prometheus (`systemd enabled`)
* ✅ Grafana (`systemd enabled`)
* ✅ Node Exporter (`systemd enabled`)
* ✅ Nginx (`systemd enabled`)

---

## Cost

**AWS Free Tier — ₹0 spent**

---

## Skills Demonstrated

* ML model training and deployment
* Docker containerization and registry management
* Kubernetes orchestration with rolling updates
* AWS EC2 provisioning with Terraform
* GitHub Actions CI/CD automation
* Production monitoring with Prometheus and Grafana
* Infrastructure as Code (IaC)
* Service reliability and auto-recovery

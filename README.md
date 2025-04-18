# SentinelLog: AI-Driven Cloud Log Monitoring System

## Overview
SentinelLog is an AI-powered cloud log monitoring system designed for **proactive security** and **performance monitoring** in cloud environments. It integrates **AWS CloudWatch**, **Grafana**, **Docker**, **Kubernetes**, **Ansible**, **Jenkins**, and **AI-based anomaly detection** to automate log analysis and system remediation.

## Features
- **AWS CloudWatch Integration** – Collects and streams logs for real-time monitoring.
- **AI-Based Anomaly Detection** – Uses Isolation Forest ML model to detect anomalies in logs.
- **Grafana Dashboard** – Real-time visualization of system logs and alerts.
- **Docker & Kubernetes Deployment** – Ensures scalability and fault tolerance.
- **Ansible Automation** – Automates deployment and infrastructure provisioning.
- **Jenkins CI/CD Pipeline** – Automates deployment and monitoring.
- **Auto-Remediation** – Dynamically mitigates issues before impacting services.

## Prerequisites
- **AWS Academy Account** (for CloudWatch setup)
- **Docker & Kubernetes** installed
- **Python 3.9+** with required libraries
- **Ansible & Jenkins** installed

## Installation & Setup
### 1️⃣ Set Up AWS CloudWatch Logs
```sh
aws logs create-log-group --log-group-name SentinelLog-Demo
aws logs create-log-stream --log-group-name SentinelLog-Demo --log-stream-name TestStream
aws logs put-log-events --log-group-name SentinelLog-Demo --log-stream-name TestStream --log-events timestamp=$(date +%s%N | cut -b1-13),message="Test log: CPU usage at 90%"
```

### 2️⃣ Install Dependencies
```sh
pip install pandas scikit-learn boto3
```

### 3️⃣ Run AI-Based Anomaly Detection
Create `log_anomaly_detection.py` and run:
```sh
python log_anomaly_detection.py
```

### 4️⃣ Set Up Grafana for Visualization
```sh
docker run -d --name=grafana -p 3000:3000 grafana/grafana
```
- Open **http://localhost:3000** and connect AWS CloudWatch as a data source.

### 5️⃣ Dockerize & Deploy
```sh
# Build Docker Image
docker build -t sentinel-log .

# Run the Container
docker run --rm sentinel-log
```

### 6️⃣ Automate Deployment with Ansible
Create `deploy.yml` and run:
```sh
ansible-playbook deploy.yml
```

### 7️⃣ Set Up Jenkins Pipeline
Create a `Jenkinsfile` and run in Jenkins:
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t sentinel-log .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d sentinel-log'
            }
        }
    }
}
```
```

### 8️⃣ Set Up Auto-Remediation Script
Create `auto_fix.sh`:
```sh
#!/bin/bash
LOG_FILE="/var/log/system.log"

if grep -q "error" $LOG_FILE; then
  echo "Issue detected! Restarting service..."
  systemctl restart my_service
fi
```
Run it with a cron job:
```sh
crontab -e
* * * * * /bin/bash /path/to/auto_fix.sh
```
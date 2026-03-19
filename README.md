# 🚀 DevSecOps CI/CD Pipeline with Kubernetes and GitOps

## 📌 Overview
This project demonstrates a complete DevSecOps pipeline by deploying a containerized application using modern cloud-native tools.

A simple static portfolio website (`index.html`) is used as the application.

> ⚠️ Note: This project uses a simple static website for demonstration, but the same pipeline can be applied to any application such as a Node.js app, Python app, or microservices-based system.

---

## ⚙️ Tech Stack
- Docker  
- Kubernetes  
- GitHub Actions (CI/CD)  
- Trivy (Security Scanning)  
- ArgoCD (GitOps)  

---

## 🔄 Workflow
Code Push → GitHub Actions → Docker Build → Trivy Scan → Docker Hub → Kubernetes → ArgoCD Sync

---

## 🐳 Containerization
- Application containerized using Docker  
- Served using Nginx  

---

## ⚙️ CI/CD Pipeline
- Automated build on every push  
- Vulnerability scanning using Trivy  
- Image pushed to Docker Hub  

---

## ☸️ Kubernetes Deployment
- Deployment and Service YAML files  
- Application exposed using NodePort  

---

## 🔄 GitOps with ArgoCD
- Kubernetes manifests stored in GitHub  
- ArgoCD automatically syncs changes to cluster  

---

## 🧪 How to Run Locally

### 1. Clone repository
git clone https://github.com/callmedenz/portfolio-devsecops.git
cd portfolio-devsecops

### 2. Run using Docker
docker build -t portfolio-app .
docker run -p 8080:80 portfolio-app

### 3. Run on Kubernetes
kubectl apply -f k8s/
minikube service portfolio-service

---

## 👨‍💻 Author
Dennis Pradhan

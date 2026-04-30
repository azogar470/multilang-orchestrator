# Multi-Language Orchestrator

A containerized multi-language microservices application orchestrated in Kubernetes using **Kind** (Kubernetes in Docker) for local development and testing.

## 📋 Overview

This project demonstrates how to:
- Build and containerize applications in **multiple languages** (Node.js & Python)
- Deploy them as **microservices** in a Kubernetes cluster
- Use **Kind** to run a local Kubernetes cluster without cloud infrastructure

### Services Included
- **Node.js App**: Express.js API running on port 3000
- **Python App**: Flask API running on port 5000

---

## 🏗️ Architecture

### Kubernetes Cluster (Kind)

```
┌─────────────────────────────────────────────────────────┐
│           KIND Cluster (3 Nodes)                        │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │         Control Plane Node                       │  │
│  │  ┌────────────────────────────────────────────┐  │  │
│  │  │ API Server, Scheduler, Controller Manager  │  │  │
│  │  └────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────┐  │  │
│  │  │ NodePort Services (Port 30000, 30001)     │  │  │
│  │  └────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────┐   ┌──────────────────────┐  │
│  │   Worker Node 1      │   │   Worker Node 2      │  │
│  │  ┌────────────────┐  │   │  ┌────────────────┐  │  │
│  │  │ Pods/Containers│  │   │  │ Pods/Containers│  │  │
│  │  └────────────────┘  │   │  └────────────────┘  │  │
│  └──────────────────────┘   └──────────────────────┘  │
│                                                          │
└─────────────────────────────────────────────────────────┘
         │                              │
    Host Port 8080                  Host Port 8081
    (Node App)                      (Python App)
```

- **Docker**: For running Kind and building container images
- **Kind**: Local Kubernetes cluster tool
- **kubectl**: Kubernetes command-line tool
- **Git**: Version control
## 📦 Project Structure
```
.
├── config.yml                    # Kind cluster configuration
├── k8s/
│   ├── node-deployment.yaml     # Node.js Deployment & Service
│   └── python-deployment.yaml   # Python Deployment & Service
├── nodeJS/
│   ├── Dockerfile               # Node.js container image
│   ├── index.js                 # Express.js application
│   └── package.json             # Node.js dependencies
├── python/
│   ├── Dockerfile               # Python container image
│   └── app.py                   # Flask application
└── README.md                    # This file


```
## 📚 Kubernetes Resources Used

- **Deployment**: Manages replicas of pods
- **Service**: Exposes pods with NodePort type
- **Pod**: Smallest deployable unit running containers
- **Node**: Machine (physical or virtual) in the cluster

## 📖 Additional Resources

- [Kind Documentation](https://kind.sigs.k8s.io/)
- [Kubernetes Official Docs](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)

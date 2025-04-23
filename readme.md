# 📦 Vault Infra Manifest Collection

This repository contains a curated collection of infrastructure manifests to help you quickly bootstrap various services using **Kubernetes**, **Docker Compose**, or **Terraform**. It acts as both a central hub for modular deployment templates and a future-ready foundation for CI/CD-ready environments.

> This repo is part of my ongoing initiative to open-source reusable DevOps and platform engineering knowledge. It complements other tools like my [KrakenD JSON config generator](https://github.com/anandakevin/tool-krakend-configurator) and CI/CD practices explored across projects.

## 📁 Repository Structure

```bash
.
├── [platform]/                     # Platform name. e.g., k8s/, docker-compose/, terraform/
│   ├── [group-name]/               # service group name
│       └── [deployment-name]/      # e.g., krakend/, vault/, observability/
└── README.md
```

Each folder is structured modularly for ease of reuse, and each deployment subfolder contains self-contained manifests and configurations for specific services.

## 📌 How to Use

Pick the deployment style and service you need:

```bash
cd k8s/krakend/
kubectl apply -f .

# Docker Compose

cd docker-compose/minio/
docker compose up -d

# Terraform

cd Terraform/aws-base/
terraform init && terraform apply
```

Each service folder will contain a README.md or notes on prerequisites, variables, and recommended usage.

## 📎 Related Projects

- [🔧 KrakenD Config Generator](https://github.com/anandakevin/tool-krakend-configurator)
- [🌐 Personal Site / Docs Hub](https://anandakevin.github.io/)
- ✍️ Articles on Medium and Dev.to

## 🙌 Contributions & License

This is a learning-focused and open-source-first repo. Contributions, suggestions, and forks are welcome!
📜 Licensed under [MIT](./LICENSE)

> Made with curiosity, systems thinking, and way too much tea 🍵

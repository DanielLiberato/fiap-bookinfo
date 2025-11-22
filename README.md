# 🚀 FIAP - DevOps Pipeline (Bookinfo)

![CI/CD Status](https://github.com/DanielLiberato/fiap-bookinfo/actions/workflows/pipeline.yaml/badge.svg)

Entrega do trabalho de **Intelligent CI/CD Pipelines**. Este projeto implementa um pipeline automatizado para a aplicação *Bookinfo ProductPage*.

## 🛠 Tecnologias Utilizadas
* **Aplicação:** Python (Flask)
* **Containerização:** Docker
* **CI/CD:** GitHub Actions
* **Registry:** Docker Hub
* **Segurança:** Trivy (Vulnerability Scanner)
* **IaC:** Kubernetes Manifests

## ⚙️ Pipeline Workflow
O pipeline executa automaticamente os seguintes passos a cada push na branch `main`:

1.  **Checkout:** Baixa o código fonte.
2.  **Code Quality:** Análise estática com `flake8`.
3.  **Testes Unitários:** Validação lógica da aplicação.
4.  **Build & Push:** Criação da imagem Docker e envio para o Docker Hub com tag de versionamento.
5.  **Security Scan:** Varredura de CVEs na imagem gerada.
6.  **Deploy Strategy:** Atualização dinâmica dos manifestos Kubernetes (`k8s/deployment.yaml`) com a nova versão da imagem.

## 📦 Como Rodar Localmente
```bash
docker run -p 9080:9080 234325/bookinfo-fiap:latest
```

## 🛠 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Trivy](https://img.shields.io/badge/trivy-security-orange?style=for-the-badge)
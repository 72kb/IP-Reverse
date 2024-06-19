# IP-Reverse: A Flask App with MongoDB on GKE

This project demonstrates deploying a Flask application with a MongoDB backend to Google Kubernetes Engine (GKE) using Docker, Helm, and GitHub Actions for CI/CD.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [GCP Setup](#gcp-setup)
  - [Local Setup](#local-setup)
  - [Docker](#docker)
  - [Kubernetes](#kubernetes)
  - [Helm](#helm)
  - [GitHub Actions](#github-actions)
- [Usage](#usage)
  - [Deploy Locally](#deploy-locally)
  - [Deploy to GKE](#deploy-to-gke)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Google Cloud Platform (GCP) account
- Docker Hub account
- GitHub account
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Helm](https://helm.sh/docs/intro/install/)

## Setup

### GCP Setup

1. **Create a GCP Project**
   - Go to the [GCP Console](https://console.cloud.google.com/).
   - Create a new project.

2. **Enable the Kubernetes Engine API**
   - In the GCP Console, navigate to `APIs & Services > Library`.
   - Enable the `Kubernetes Engine API`.

3. **Create a GKE Cluster**
   - In the GCP Console, navigate to `Kubernetes Engine > Clusters`.
   - Create a new cluster.

4. **Authenticate and Configure gcloud**
   - Authenticate with your GCP account:
     ```sh
     gcloud auth login
     ```
   - Set the default project:
     ```sh
     gcloud config set project YOUR_PROJECT_ID
     ```
   - Get credentials for your cluster:
     ```sh
     gcloud container clusters get-credentials YOUR_CLUSTER_NAME --zone YOUR_CLUSTER_ZONE
     ```

### Local Setup

Clone the repository to your local machine:

```sh
git clone https://github.com/your-username/flask-app.git
cd flask-app

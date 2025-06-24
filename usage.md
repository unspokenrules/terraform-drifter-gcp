# Usage Guide

## What This Is and Why It Exists

### 🧠 Purpose
This repository automates the creation of foundational GCP networking infrastructure using Terraform. It’s designed to detect, surface, and optionally reconcile **drift** between your Terraform state and actual cloud infrastructure.

### 🚨 The Problem It Solves
Cloud environments drift. Teams manually tweak resources in the GCP console, breaking IaC assumptions and introducing hidden risk. This repo gives you a Terraform-first baseline for:
- Deploying core GCP network components
- Detecting infrastructure drift using Terraform plan diffs
- Maintaining state integrity across environments

### 🧰 When to Use This
Use this repo when:
- You want a clean, auditable GCP networking setup via Terraform
- You need to validate that your infrastructure hasn’t drifted from its declared state
- You’re building pipelines that gate deployments on infrastructure consistency

### ⚡️ Why This Is Better Than Defaults
- Built-in drift detection focus
- Terraform native—works with CI/CD and remote backends
- Clean separation of concerns with potential for modular growth
- Minimal GCP assumptions; adaptable to multi-project use

---

## Prerequisites

> ✅ Required Tools:
- [Terraform CLI](https://developer.hashicorp.com/terraform/downloads)
- [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
- Python 3.10+
- A GCP project with billing enabled
- Proper IAM roles for networking and asset inventory APIs

> 🔐 Authentication:
- Run: `gcloud auth application-default login`
- Ensure your credentials have sufficient access to list and manage network resources

---

# 📘 How to Use Terraform Drifter for GCP — Step-by-Step

---

## 🧱 STEP 0: Set Up Your Environment

Make sure you have the following before running anything:
- Python 3.10+ with `venv`
- Authenticated GCP CLI
- A cloned version of this repo
- Terraform installed and initialized
- A JSON export of your Terraform state

---

## 🔧 STEP 1: Clone This Repository

```bash
git clone https://github.com/unspokenrules/terraform-drifter-gcp.git
cd terraform-drifter-gcp
```

---

## 📦 STEP 2: Install Python Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install google-cloud-asset protobuf
```

---

## 🔐 STEP 3: Authenticate to Google Cloud

```bash
gcloud auth application-default login
```

---

## 🌐 STEP 4: Export Terraform State to JSON

From your Terraform project directory:

```bash
terraform show -json > terraform.tfstate.json
```

Copy the resulting file into this repo directory.

---

## 🚀 STEP 5: Run the Drifter Tool

```bash
python cli.py \
  --project your-gcp-project-id \
  --tfstate terraform.tfstate.json \
  --md drift_report.md \
  --json drift_report.json
```

Replace `your-gcp-project-id` with your actual project ID.

---

## 📄 STEP 6: Read the Report

Open the generated `drift_report.md`:

```
=== Unmanaged Resources ===
compute.googleapis.com/Instance - rogue-vm

=== Stale Resources ===
google_compute_instance - ghost-vm

=== Managed Resources ===
compute.googleapis.com/Instance - tf-managed-vm
```

| Section | Description |
|---------|-------------|
| **Unmanaged** | GCP has it, Terraform doesn’t — possibly rogue |
| **Stale**     | Terraform has it, GCP doesn’t — probably obsolete |
| **Managed**   | Terraform and GCP match — no issues |

---

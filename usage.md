# 📘 How to Use Terraform Drifter for GCP — Step-by-Step

This is a no-fluff, operator-level guide for using the drift detection tool you just built.

---

## 🧱 STEP 0: Prerequisites

Make sure you have the following set up **before you run anything**:

- ✅ Python 3.10+
- ✅ `gcloud` CLI installed and authenticated
- ✅ A cloned copy of your GitHub repo
- ✅ Terraform installed and initialized
- ✅ Your Terraform state available as JSON

---

## 🔧 STEP 1: Clone Your Repo

```bash
git clone https://github.com/unspokenrules/terraform-drifter-gcp.git
cd terraform-drifter-gcp
```

---

## 📦 STEP 2: Install Python Dependencies

(Optional but recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

Then:
```bash
pip install google-cloud-asset protobuf
```

---

## 🔐 STEP 3: Authenticate to Google Cloud

```bash
gcloud auth application-default login
```

This gives the tool access to your GCP project.

---

## 🌐 STEP 4: Export Terraform State

From your Terraform project directory:
```bash
terraform show -json > terraform.tfstate.json
```

Then move that `.json` into your drift detection repo.

---

## 🚀 STEP 5: Run the Drifter Tool

In your drift detection repo folder:

```bash
python cli.py \
  --project your-gcp-project-id \
  --tfstate terraform.tfstate.json \
  --md drift_report.md \
  --json drift_report.json
```

Replace `your-gcp-project-id` with your actual GCP project.

---

## 📄 STEP 6: Read the Report

Open `drift_report.md` — you’ll see:

```
=== Unmanaged Resources ===
compute.googleapis.com/Instance - rogue-vm

=== Stale Resources ===
google_compute_instance - ghost-vm

=== Managed Resources ===
compute.googleapis.com/Instance - tf-managed-vm
```

| Section | What It Means |
|---------|----------------|
| **Unmanaged** | GCP has it, Terraform doesn’t — might be rogue. |
| **Stale**     | Terraform has it, GCP doesn’t — likely a ghost. |
| **Managed**   | Good. Terraform and GCP are aligned. |

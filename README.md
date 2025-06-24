# 🚨 Terraform Drifter for GCP
## 🧠 What It Is

**Terraform Drifter for GCP** compares your Terraform state to the actual resources running in Google Cloud.  
It flags what Terraform doesn't know about (unmanaged), what no longer exists (stale), and what it does manage (clean).

Built for:
- Cloud engineers
- SREs
- Security teams

---

## ✨ Features at a Glance

| Capability                          | Status    |
|-------------------------------------|-----------|
| Compare Terraform state vs GCP live | ✅ Yes     |
| Detect unmanaged resources          | ✅ Yes     |
| Detect stale state entries          | ✅ Yes     |
| Markdown & JSON reporting           | ✅ Yes     |
| Compute Engine support              | ✅ Yes     |
| Cloud Storage support               | ✅ Yes     |
| CLI interface                       | ✅ Yes     |
| CI/CD integration ready             | ✅ Yes     |
| Easy to extend                      | ✅ Yes     |

---
##  🧱Prereqs You Must Have
Before anything else:

- ✅ [ ] You have Python 3.10+ installed
- ✅ [ ] You have gcloud CLI installed and authenticated
- ✅ [ ] You’ve cloned this GitHub repo locally
- ✅ [ ] You’ve exported your Terraform state file as JSON

If any of these aren’t done, pause and fix it now. Drift detection will break otherwise.

---

## Instructions
🔧 STEP 1: Clone the Repo










## ⚡ TL;DR (One-Minute Setup)

```bash
# Install dependencies
pip install -r requirements.txt

# Auth to GCP
gcloud auth application-default login

# Run drift check
python cli.py \
  --project your-gcp-project-id \
  --tfstate terraform.tfstate.json \
  --md drift_report.md \
  --json drift_report.json
```

---

## 🧪 Output Example

```
=== Unmanaged Resources ===
compute.googleapis.com/Instance - rogue-vm
storage.googleapis.com/Bucket - drift-bucket

=== Stale Resources ===
google_compute_instance - ghost-vm

=== Managed Resources ===
compute.googleapis.com/Instance - tf-managed-vm
```

- ✅ **Unmanaged**: exists in GCP, not in Terraform
- ❌ **Stale**: exists in Terraform state, not in GCP
- 🔒 **Managed**: exists in both

---

## 🔧 Developer Notes

Want to extend this? You’ll mostly be editing:

| File                     | What it handles                          |
|--------------------------|-------------------------------------------|
| `gcp_inventory.py`       | Fetch live GCP assets                     |
| `tf_parser.py`           | Parse Terraform state                     |
| `core.py`                | Diff logic: GCP vs Terraform              |
| `reporter.py`            | Markdown + JSON report generation         |

---

## 💡 Why This Exists

Terraform is only as good as your discipline.  
Most infra teams **accumulate ghosts** — resources that are:
- Manually created
- Forgotten
- Never removed

This tool forces visibility.  
It makes Terraform the source of truth again.

---


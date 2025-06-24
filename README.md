# 🚨 Terraform Drifter for GCP
## 🧠 What It Is

**Terraform Drifter for GCP** compares your Terraform state to the actual resources running in Google Cloud.  
It flags what Terraform doesn't know about (unmanaged), what no longer exists (stale), and what it does manage (clean).

Built for:
- Cloud engineers
- SREs
- Security teams

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

## 📷 Sample Drift Report (Rendered)

![Image](https://github.com/user-attachments/assets/ffc5d3a8-dc06-4209-9af8-c08930c50e78)

---

## 📦 Supported Resource Types

| Terraform Type                     | GCP Asset Type                      |
|-----------------------------------|-------------------------------------|
| `google_compute_instance`         | `compute.googleapis.com/Instance`   |
| `google_project_iam_custom_role`  | `iam.googleapis.com/Role`           |
| `google_storage_bucket`           | `storage.googleapis.com/Bucket`     |

Extending support is as easy as adding new mappings in `tf_parser.py` and `gcp_inventory.py`.

---

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


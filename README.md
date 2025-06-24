# terraform-drifter-gcp

> 🚨 Detect unmanaged, orphaned, and drifted resources in GCP by comparing live infrastructure with your Terraform state.

---

## 🧠 What is Drifter?

**Drifter** is a CLI tool that finds real-world GCP resources that exist outside your Terraform state. It helps cloud engineers detect:

- 🧟‍♀️ **Zombie resources** — resources deployed manually or forgotten
- 🔥 **Drifted configurations** — changes in resource config that Terraform doesn't know about
- ❌ **Stale declarations** — Terraform state entries that point to deleted infrastructure

**Why it matters**:  
If Terraform doesn’t manage it, you don’t control it.  
Drifter closes the gap between what’s deployed and what’s declared.

---

## 🔧 Supported Resources (v0.1)

- `google_compute_instance`
- `google_storage_bucket`
- `google_sql_database_instance`
- `google_pubsub_topic`
- (more coming...)

---

## 🚀 Quickstart

### Install requirements:

```bash
pip install -r requirements.txt
```

### Authenticate with GCP:
```bash
gcloud auth application-default login
```

### Run Drifter:

```bash
python cli.py \
  --project=my-gcp-project \
  --tfstate=./terraform.tfstate \
  --output=drift_report.md
```

---

## 📊 Output Example

```markdown
# Drift Report — my-gcp-project

## Unmanaged Resources

- `google_compute_instance` → `dev-vm-1` (not found in TF)
- `google_storage_bucket` → `temp-logs-bucket` (not defined in TF)

## Drifted Resources

- `google_sql_database_instance` → `prod-db`
    - Terraform says tier: `db-f1-micro`
    - GCP says tier: `db-custom-2-7680`

## Missing Resources in GCP

- `google_pubsub_topic` → `tf-logs-topic` (declared in TF, not found in GCP)
```

---

## 🛠 Features

- ✅ Compare live GCP assets with Terraform state
- ✅ Identify unmanaged & drifted resources
- ✅ Markdown/JSON/HTML report output
- ✅ Config file for exclusions
- ✅ GitHub Action support (WIP)

---

## 📁 Project Structure

```
terraform-drifter-gcp/
├── drifter/
│   ├── cli.py
│   ├── core.py
│   ├── tf_parser.py
│   ├── gcp_inventory.py
│   ├── reporter.py
│   └── utils.py
├── examples/
│   └── sample_state.json
├── tests/
│   └── test_core.py
├── requirements.txt
└── README.md
```

---


## 🤝 Contributing

Contributions welcome. Open an issue or submit a PR — especially for:
- Support for more resource types
- Report enhancements
- Drift detection logic

---

## ⚠️ Disclaimer

This tool is **read-only by default**. It does **not** delete or modify any GCP resources or Terraform state. Always review drift reports manually.

---

## 👨‍💻 Author

Built by [@unspokenrules](https://github.com/unspokenrules) — because infrastructure should never be a guessing game.

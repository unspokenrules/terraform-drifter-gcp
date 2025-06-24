# cli.py
import argparse
from drifter.tf_parser import load_terraform_state
from drifter.gcp_inventory import list_gcp_resources
from drifter.core import compare_resources
from drifter.reporter import generate_markdown_report, generate_json_report

parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True)
parser.add_argument("--tfstate", required=True)
parser.add_argument("--md", required=True)
parser.add_argument("--json", required=True)
args = parser.parse_args()

print("[INFO] Loading Terraform state...")
tf_resources = load_terraform_state(args.tfstate)
print(f"[INFO] TF Resources: {tf_resources}")

print("[INFO] Fetching GCP live resources...")
gcp_resources = list_gcp_resources(args.project)
print(f"[INFO] GCP Resources: {gcp_resources}")

print("[INFO] Comparing...")
results = compare_resources(tf_resources, gcp_resources)
print(f"[INFO] Results: {results}")

print("[INFO] Generating reports...")
generate_markdown_report(results, args.md)
generate_json_report(results, args.json)
print("[INFO] Done.")

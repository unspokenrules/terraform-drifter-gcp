

from datetime import datetime
import json

def generate_markdown_report(results, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 🛰️ Terraform Drift Report\n\n")
        f.write(f"**Generated:** {datetime.utcnow().isoformat()} UTC\n\n")

        f.write("## ❌ Unmanaged Resources\n")
        for res in results["unmanaged"]:
            f.write(f"- {res[0]} - {res[1]}\n")
        if not results["unmanaged"]:
            f.write("- None\n")

        f.write("\n## ⚠️ Stale Resources\n")
        for res in results["stale"]:
            f.write(f"- {res[0]} - {res[1]}\n")
        if not results["stale"]:
            f.write("- None\n")

        f.write("\n## ✅ Managed Resources\n")
        for res in results["managed"]:
            f.write(f"- {res[0]} - {res[1]}\n")
        if not results["managed"]:
            f.write("- None\n")

def generate_json_report(results, output_file):
    def sanitize(obj):
        if isinstance(obj, (str, int, float, bool)) or obj is None:
            return obj
        elif isinstance(obj, dict):
            return {k: sanitize(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [sanitize(i) for i in obj]
        else:
            return str(obj)

    cleaned_results = {
        k: [sanitize(i) for i in v]
        for k, v in results.items()
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at": datetime.utcnow().isoformat(),
            "results": cleaned_results
        }, f, indent=2)

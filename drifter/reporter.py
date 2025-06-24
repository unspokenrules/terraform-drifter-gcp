from datetime import datetime
from collections import defaultdict

def generate_markdown_report(results, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# 🌐 Drift Report\n\n")
        f.write(f"**Generated:** `{datetime.utcnow().isoformat()}`\n\n")

        # Count summary
        f.write("## 📊 Summary\n")
        f.write("| Type | Count |\n")
        f.write("|------|-------|\n")
        f.write(f"| ✅ Managed | {len(results['managed'])} |\n")
        f.write(f"| ❌ Unmanaged | {len(results['unmanaged'])} |\n")
        f.write(f"| ⚠️ Stale | {len(results['stale'])} |\n\n")

        # Section generator
        def write_section(title, icon, data):
            grouped = defaultdict(list)
            for rtype, name in data:
                grouped[rtype].append(name)

            f.write(f"## {icon} {title}\n")
            if not grouped:
                f.write("_None._\n\n")
                return

            for rtype in sorted(grouped):
                f.write(f"### 🔹 {rtype}\n")
                for name in sorted(grouped[rtype]):
                    f.write(f"- {name}\n")
                f.write("\n")

        write_section("Managed Resources", "✅", results["managed"])
        write_section("Unmanaged Resources (Not in Terraform)", "❌", results["unmanaged"])
        write_section("Stale Resources (Only in Terraform)", "⚠️", results["stale"])


import json

def generate_json_report(results, output_path):
    def normalize(data):
        return [
            {"type": t, "name": n}
            for (t, n) in sorted(data)
        ]

    output = {
        "generated_at": datetime.utcnow().isoformat(),
        "results": {
            "managed": normalize(results["managed"]),
            "unmanaged": normalize(results["unmanaged"]),
            "stale": normalize(results["stale"])
        }
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

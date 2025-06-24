# drifter/tf_parser.py
def load_terraform_state(state_file_path):
    import json
    with open(state_file_path, "r") as f:
        data = json.load(f)

    resources = []

    def extract_resources(mod):
        for res in mod.get("resources", []):
            res_type = res.get("type")
            res_name = res.get("name")
            res_values = res.get("values", {})

            gcp_resource_type = {
                "google_compute_instance": "compute.googleapis.com/Instance",
                "google_project_iam_custom_role": "iam.googleapis.com/Role"
            }.get(res_type)

            if gcp_resource_type:
                resources.append({
                    "type": gcp_resource_type,
                    "name": res_values.get("role_id", res_name),  # role_id is key for IAM roles
                    "attributes": res_values
                })

    root = data.get("values", {}).get("root_module", {})
    extract_resources(root)
    for mod in root.get("child_modules", []):
        extract_resources(mod)

    return resources

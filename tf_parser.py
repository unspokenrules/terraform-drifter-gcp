import json

def load_terraform_state(state_file_path):
    """
    Loads and parses Terraform state JSON file.
    Returns a list of normalized resource dicts.
    """
    with open(state_file_path, "r") as f:
        data = json.load(f)

    resources = []

    for res in data.get("values", {}).get("root_module", {}).get("resources", []):
        res_type = res.get("type")
        res_name = res.get("name")
        res_values = res.get("values", {})

        resource_entry = {
            "type": res_type,
            "name": res_name,
            "id": res_values.get("id", ""),
            "attributes": res_values
        }
        resources.append(resource_entry)

    # Also scan child modules (if any)
    for mod in data.get("values", {}).get("root_module", {}).get("child_modules", []):
        for res in mod.get("resources", []):
            res_type = res.get("type")
            res_name = res.get("name")
            res_values = res.get("values", {})

            resource_entry = {
                "type": res_type,
                "name": res_name,
                "id": res_values.get("id", ""),
                "attributes": res_values
            }
            resources.append(resource_entry)

    return resources

# drifter/gcp_inventory.py
from google.cloud import asset_v1

def list_gcp_resources(project_id):
    client = asset_v1.AssetServiceClient()
    scope = f"projects/{project_id}"
    asset_types = [
        "compute.googleapis.com/Instance",
        "iam.googleapis.com/Role"
    ]

    results = []

    request = asset_v1.SearchAllResourcesRequest(
        scope=scope,
        asset_types=asset_types,
        page_size=100,
    )

    for resource in client.search_all_resources(request=request):
        name = resource.name.split("/")[-1]

        results.append({
            "type": resource.asset_type,
            "name": name
        })

    return results

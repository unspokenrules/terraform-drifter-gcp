

from google.cloud import asset_v1

def list_gcp_resources(project_id):
    """
    List active GCP resources in the given project using Cloud Asset Inventory.
    Returns a list of (type, name) dicts.
    """
    client = asset_v1.AssetServiceClient()
    scope = f"projects/{project_id}"

    asset_types = [
        "compute.googleapis.com/Instance",
        "storage.googleapis.com/Bucket",
    ]

    request = asset_v1.ListAssetsRequest(
        parent=scope,
        asset_types=asset_types,
        content_type=asset_v1.ContentType.RESOURCE,
    )

    results = []
    for response in client.list_assets(request=request):
        asset = response.asset
        resource = asset.resource.data
        results.append({
            "type": asset.asset_type,
            "name": resource.get("name", "unknown")
        })

    return results

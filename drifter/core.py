
def compare_resources(tf_resources, gcp_resources):
    """
    Compare Terraform resources and live GCP resources.
    Returns a dictionary of unmanaged, stale, and managed resources.
    """
    tf_set = set((res['type'], res['name']) for res in tf_resources)
    gcp_set = set((res['type'], res['name']) for res in gcp_resources)

    unmanaged = gcp_set - tf_set
    stale = tf_set - gcp_set
    managed = tf_set & gcp_set

    return {
        "unmanaged": sorted(unmanaged),
        "stale": sorted(stale),
        "managed": sorted(managed)
    }


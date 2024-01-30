###### METHOD 1 - Databricks SDK ######
from databricks.sdk import WorkspaceClient

workspace_client = WorkspaceClient()

new_cluster = workspace_client.clusters.create(
    cluster_name="my-cluster",
    spark_version="12.2.x-scala2.12",
    node_type_id="Standard_DS3_v2",
    num_workers=2
)

print(f"Cluster created with ID: {new_cluster.cluster_id}")


###### METHOD 2 - REST API ######
###### METHOD 1 - Databricks SDK ######
import libraries

workspace_client = WorkspaceClient()

new_cluster = workspace_client.clusters.create(
    cluster_name="my-cluster",
    spark_version="12.2.x-scala2.12",
    node_type_id="Standard_DS3_v2",
    num_workers=2
)

print(f"Cluster created with ID: {new_cluster.cluster_id}")


###### METHOD 2 - REST API ######

workspace_host = "https://<your-workspace-url>"
personal_token = "dapi<your-token>"

cluster_spec = {
    "cluster_name": "my-cluster",
    "node_type_id": "Standard_DS3_v2",
    "spark_version": "12.2.x-scala2.12",
    "num_workers": 2
}

response = requests.post(
    f"{workspace_host}/api/2.0/clusters/create",
    headers={"Authorization": f"Bearer {personal_token}"},
    json=cluster_spec
)

cluster_id = response.json()['cluster_id']
print(f"Cluster created with ID: {cluster_id}")
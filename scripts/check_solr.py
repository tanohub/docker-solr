#!/usr/bin/python3

import json
import requests

cluster_status_url = "http://localhost:8981/solr/admin/collections?action=clusterstatus&wt=json"

cluster_status_request = requests.get(cluster_status_url)

if cluster_status_request.status_code != 200:
  raise Exception(f"Failed to get Solr cluster status: {response.status_code}")

cluster_status_json = json.loads(cluster_status_request.text)

#print(json.dumps(cluster_status_json, indent = 4, sort_keys=True))

for collection in cluster_status_json["cluster"]["collections"]:
  for shard in cluster_status_json["cluster"]["collections"][collection]["shards"]:
   for replica in cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"]:
    replica_state = cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"][replica]["state"]
    print("coll: " + collection + " --- shard: " + shard + " --- replica: " + replica + " --- state: " + replica_state )
#        "state": cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"][replica]["state"],
#        "type": cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"][replica]["type"],
#        "leader": cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"][replica]["leader"]
#        )

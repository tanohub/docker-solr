#!/usr/bin/python3

import json
import requests

cluster_status_url = "http://localhost:8981/solr/admin/collections?action=clusterstatus&wt=json"

cluster_status_request = requests.get(cluster_status_url)

if cluster_status_request.status_code != 200:
  raise Exception(f"Failed to get Solr cluster status: {response.status_code}")

cluster_status_json = json.loads(cluster_status_request.text)

#print(json.dumps(cluster_status_json, indent = 4, sort_keys=True))

replica_state_down_counter = 0
for collection in cluster_status_json["cluster"]["collections"]:
  for shard in cluster_status_json["cluster"]["collections"][collection]["shards"]:
    for replica in cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"]:
      replica_state = cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"][replica]["state"]
      node_name = cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"][replica]["node_name"]
      if replica_state == 'down' :
        replica_state_down_counter += 1 
        print("coll: " + collection + " --- shard: " + shard + " --- node: " + node_name + "--- replica: " + replica + " --- state: " + replica_state )

print("Found " + str(replica_state_down_counter) + " replica in down status")

#        "state": cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"][replica]["state"],
#        "type": cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"][replica]["type"],
#        "leader": cluster_status_json["cluster"]["collections"][collection]["shards"][shard]["replicas"][replica]["leader"]
#        )

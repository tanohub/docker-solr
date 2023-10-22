#!/usr/bin/python3

import json
import requests

cluster_status_url = "http://localhost:8983/solr/admin/collections?action=clusterstatus&wt=json"

cluster_status_request = requests.get(cluster_status_url)
cluster_status_json = json.loads(cluster_status_request.text)

for collections in cluster_status_json['cluster']['collections']:
	print(collections[pullReplicas])
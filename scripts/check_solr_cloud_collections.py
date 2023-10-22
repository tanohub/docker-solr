#!/usr/bin/python3

import json
import requests

def check_collection_status(zk_hosts, collection_name):
  """Checks the status of a Solr Cloud collection.

  Args:
    zk_hosts: A list of ZooKeeper hosts.
    collection_name: The name of the Solr Cloud collection to check.

  Returns:
    A dictionary containing the status of the collection.
  """

  url = "http://{}/solr/admin/collections?action=COLSTATUS&collection={}".format(zk_hosts[0], collection_name)
  response = requests.get(url)
  if response.status_code == 200:
    return json.loads(response.content)
  else:
    raise Exception("Failed to check collection status: {}".format(response.status_code))

def main():
  zk_hosts = ["localhost:2181"]

  # Get a list of all Solr Cloud collections.
  url = "http://{}/solr/admin/collections?action=LIST"
  response = requests.get(url, zk_hosts=zk_hosts)
  if response.status_code == 200:
    collections = json.loads(response.content)["collections"]
  else:
    raise Exception("Failed to get list of collections: {}".format(response.status_code))

  # Check the status of each collection.
  collection_statuses = {}
  for collection_name in collections:
    collection_status = check_collection_status(zk_hosts, collection_name)
    collection_statuses[collection_name] = collection_status

  # Print the status of each collection.
  for collection_name, collection_status in collection_statuses.items():
    print("Collection: {}".format(collection_name))
    print("Status: {}".format(collection_status["status"]))

if __name__ == "__main__":
  main()

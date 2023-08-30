# Table of Contents
- [Introduction](#introduction)
    - [Version](#version)
- [Quickstart](#quick-start)
- [Services](#services)
- [References](#references)

# Introduction

Docker compose that runs:
- 3x solr nodes, in solrcloud configuration
- 3x zookeeper node, in ensemble configuration

## Version

Current versions:
- solr: **8.7** ( can be changed via .env file )
- zookeeper: **3.6.2**  ( can be changed via .env file )

# Quick Start

```
docker-compose start

$ docker-compose exec solr1 bash
solr@a2ccf9071cda:$ cd /opt/solr

::: Upload custom config
solr@a2ccf9071cda:$ bin/solr zk upconfig -d /tmp/solr-collections/books/config/ -n books-config

::: Create custom collections with custom configset
CLI:
solr@a2ccf9071cda:$ bin/solr create -c books -s 1 -rf 2 -V

curl:
for i in {01..05} ; do curl "http://localhost:8983/solr/admin/collections?action=CREATE&name=books_solr1-2_${i}&numShards=1&collection.configName=books-config&replicationFactor=2&createNodeSet=solr1:8983_solr,solr2:8983_solr"; done
for i in {01..05} ; do curl "http://localhost:8983/solr/admin/collections?action=CREATE&name=books_solr2-3_${i}&numShards=1&collection.configName=books-config&replicationFactor=2&createNodeSet=solr2:8983_solr,solr3:8983_solr"; done

::: Delete custom collections
curl:
for i in {01..05} ; do curl "http://localhost:8983/solr/admin/collections?action=DELETE&name=books_solr1-2${i}" ; done
for i in {01..05} ; do curl "http://localhost:8983/solr/admin/collections?action=DELETE&name=books_solr2-3${i}" ; done

::: popolate custom collections
solr@a2ccf9071cda:$ bin/post -c books_solr1-2_01 /tmp/solr-collections/books/books.json 


```

# Services
| Service   | Note |
| :---      | :--- |
| http://localhost:8981 | solr node1 |
| http://localhost:8081 | solr node1 - ui web |
| http://localhost:8982 | solr node2 |
| http://localhost:8082 | solr node2 - ui web |
| http://localhost:8983 | solr node3 |
| http://localhost:8083 | solr node3 - ui web |
| | |
| tcp://localhost:2181 \ 7001 | zookeeper node1 |
| tcp://localhost:2182 \ 7002 | zookeeper node2 |
| tcp://localhost:2183 \ 7003 | zookeeper node3 |

# References
https://solr.apache.org/guide/8_7/solr-tutorial.html
https://github.com/hectorcorrea/solr-for-newbies/blob/main/tutorial.md

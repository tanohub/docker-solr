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
```

# Services
| Service   | Note |
| :---      | :--- |
| http://localhost:8981 | solr node1 |
| http://localhost:8982 | solr node2 |
| http://localhost:8983 | solr node3 |
| | |
| tcp://localhost:2181 \ 7001 | zookeeper node1 |
| tcp://localhost:2182 \ 7002 | zookeeper node2 |
| tcp://localhost:2183 \ 7003 | zookeeper node3 |

# References
https://solr.apache.org/guide/8_7/solr-tutorial.html

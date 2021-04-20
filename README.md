# ELK-Project
- My ELK (Elasticsearch, Logstash, Kibana) work.
- Here you can find what I have worked on as Associate Software Developer Intern(Virtual) at Firewires Solutions Pvt. Ltd. during COVID-19.

# What is ElasticSearch?

- ElasticSearch is an open-source search engine built on top of Apache Lucene, as the rest of the ELK Stack, including Logstash and Kibana
- Supports full-text search i.e. completely document based instead of tables and schema
- Used for Single Page Application Projects

# Basic Concepts:

- **Index**: Collection of documents with similar characteristics and is identified by a name. This name is used to refer to the index while performing indexing, search, update, and delete-operations against the documents in it.
- **Type**: Logical category/partition of an index for partitioning the index.
- **Document**: A basic unit of information which can be indexed. It is expressed in JSON format.
- **Shards**: ElasticSearch ahs ability to subdivide the index into multiple pieces called "shards". Each shard is fully-functional and independent "index" that can be hosted on any node within the cluster.
- **Replicas**: ElasticSearch allows you to make one or more copies of your index's shards which are called replica shards or replica.

# API Conventions:

## 1. Multiple Indices:

- Most APIs support execution across multiple indices
- Different notation are used to perform operations in ultiple indices like:
  
  - Comma separated notations(demo1, demo2, demo3)
  - Wildcard notations(demo1*, + demo2, -demo3, de*o)
  - URL Query String Parameters(ignore_unavail, allow_no_indices, expand_wildcards)

## 2. Date Math Support in Index Name:

- ElasticSearch lets you to search indices according to date and time
- You need to specify date and time in a specific format like:  
  e.g. <static_name{date_math_expr{date_format | time_zone}}>
  
  Where,
    static_name: Static text part of the name
    date_math_expr: Computes the date dynamically
    date_format: Optional date format
    time_zone: Optional time zone
 
## 3. Common Options:

- **Following are the common options for all the REST APIs:**
  
  Pretty Result               -       Time Units
  
  HUman Readable Output       -       Byte Size Units
  
  Date Math                   -       Unit-less Quantities
  
  Response Filtering          -       Distance Units
  
  Flat Settings               -       Fuzziness
  
  Parameter                   -       Enabling Stack Traces
  
  No Values                   -       Request Body in Query String
  
  ## 4. URL-based Access Control:
  
  - Users can also have a proxy with URL-basedaccess control to secure access to the ElasticSearch indices
  - User has an option of apecifying an index in the URL and on each individual request body for some requests like:
    - multi-search
    - multi-get
    - bulk

# ElasticSearch APIs:

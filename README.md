# ELK-Stack-Project
- My ELK (Elasticsearch, Logstash, Kibana) work.
- Here you can find what I have worked on as an Associate Software Developer Intern(Virtual) at Firewires Solutions Pvt. Ltd. during COVID-19.

# What is ElasticSearch?

- ElasticSearch is an open-source search engine built on top of Apache Lucene, as the rest of the ELK Stack, including Logstash and Kibana
- Supports full-text search i.e. completely document-based instead of tables and schema
- Used for Single Page Application Projects

# What is Logstash?

- Tool for collecting and monitoring logs from remote machines
- Works as data pipeline for ElasticSearch

# What is Kibana?

- Data exploration and visualization tool
- Used for log and time series analysis, application monitoring, and operational intelligence
- A front-end UI to your ELK Stack

- **Role of Kibana**:
  - Enables the searching and interaction with data in ElasticSearch
  - Allows performing advanced analytics and creation of reports
  - Enables creation and sharing of dynamic dashboards that get updated in realtime


# How the ELK Work Together:

![Screenshot (182)](https://user-images.githubusercontent.com/63872951/115670909-90ba0080-a367-11eb-9da2-2a3ebbe882c9.png)


# Basic Concepts:

- **Index**: Collection of documents with similar characteristics and is identified by a name. This name is used to refer to the index while performing indexing, search, update, and delete operations against the documents in it.
- **Type**: Logical category/partition of an index for partitioning the index.
- **Document**: A basic unit of information that can be indexed. It is expressed in JSON format.
- **Shards**: ElasticSearch ahs ability to subdivide the index into multiple pieces called "shards". Each shard is a fully functional and independent "index" that can be hosted on any node within the cluster.
- **Replicas**: ElasticSearch allows you to make one or more copies of your index's shards which are called replica shards or replica.
- **Cluster**: Collection of nodes. Can contain as many nodes as you can. Provides indexing and search capability across all nodes. Unique.
- **Node**: Node stores searchable data, participates in a cluster's indxing and search capabilities, identified by a name. A node joins a cluster named "elasticsearch" by default.
 

# API Conventions:

## 1. Multiple Indices:

- Most APIs support execution across multiple indices
- Different notation are used to perform operations in ultiple indices like:
  
  - Comma separated notations(demo1, demo2, demo3)
  - Wildcard notations(demo1*, + demo2, -demo3, de*o)
  - URL Query String Parameters(ignore_unavail, allow_no_indices, expand_wildcards)

## 2. Date Math Support in Index Name:

- ElasticSearch lets you search indices according to date and time
- You need to specify the date and time in a specific format like:  
  e.g. <static_name{date_math_expr{date_format | time_zone}}>
  
  Where,
    - static_name: Static text part of the name
    - date_math_expr: Computes the date dynamically
    - date_format: Optional date format
    - time_zone: Optional time zone
 
## 3. Common Options:

- **Following are the common options for all the REST APIs:**
  
  Pretty Result               -       Time Units
  
  Human Readable Output       -       Byte Size Units
  
  Date Math                   -       Unit-less Quantities
  
  Response Filtering          -       Distance Units
  
  Flat Settings               -       Fuzziness
  
  Parameter                   -       Enabling Stack Traces
  
  No Values                   -       Request Body in Query String
  
## 4. URL-based Access Control: 
  
  - Users can also have a proxy with URL-based access control to secure access to the ElasticSearch indices
  - User has an option of specifying an index in the URL and on each individual request body for some requests like:
    - multi-search
    - multi-get
    - bulk

# ElasticSearch APIs:

**1. Document APIs:** Those APIs that perform the operation at the document level

**2. Search APIs:** Used to search across indices of all types

**3. Aggregation APIs:** Used to run aggregations across an index

**4. Index APIs:** To perform operations at the index level

**5. Cluster APIs:** Operate on a subset of the nodes which can be specified with node filters

# A. Document API

### 1. Single Document API: 
**to perform querying across a single document**
- It consists of:
  - Index API
  - Get API
  - Update API
  - Delete API

### 2. Multi-Document API:
**to perform querying across multiple documents**
- It consists of:
  - Multi Get API
  - Bulk API
  - Delete By Query API
  - Update By Query API
  - Reindex API
 
# Document API - CRUD Operations

**Step 1:** Go to Kibana >> Management >> Dev Tools >> 

**Step 2:** Write down the following query in the Console and Click 'Run'

PUT myplaylist/song/7 \
{ \
  "title" : "My holiday",\
  "Artist" : "Shubzz",\
  "Album" : "Linkin Park",\
  "Year" : "2012"\
}

- PUT method is used in making REST API calls to create index and document
- 'myplaylist' is the name of the index, 'song' is the document and '7' is the id

**Step 3:** Check the output

- If you get **"result" : "created"** in the following output, your query has created the document

{\
  "_index" : "myplaylist",\
  "_type" : "song",\
  "_id" : "7",\
  "_version" : 8,\
  "result" : "created",\
  "_shards" : {\
    "total" : 2,\
    "successful" : 1,\
    "failed" : 0\
  }
  
**Step 4:** Use GET method to read the created document, in Console, run the following query
  
GET myplaylist/song/7

  - If you get **"found" : true** then your query is successful 
 
 {\
  "_index" : "myplaylist",\
  "_type" : "song",\
  "_id" : "7",\
  "_version" : 8,\
  "_seq_no" : 11,\
  "_primary_term" : 1,\
  "found" : true,\
  "_source" : {\
    "title" : "My holiday",\
    "Artist" : "Shubzz",\
    "Album" : "Linkin Park",\
    "Year" : "2012"
  }
}

**Step 5:** Update the document by adding some other parameters

PUT myplaylist/song/7 \
{ \
  "title" : "My holiday",\
  "Artist" : "Shubzz",\
  "Album" : "Linkin Park",\
  "Year" : "2012",\
  "location" : "Delhi"\
}

  - Check the output and if you get **"successful" : 1** and **"result" : "true"**, query success.

**Step 6:** use DELETE API to delete a document

DELETE myplaylist/song/7

  - If you get **"successful" : 1** means that the document has been deleted

# B. Search API

### Using a search API, you can execute a search query and get back search hits that match the query

**1. Multi Index:** You can search for the documents present in all the indices or in some specific indices

**2. Multi-Type:** You can search all the documents in an index across all types or in some specified type

**3. URI Search:** Various parameters can be passed in a search operation using Uniform Resource Identifier:
  - e.g. q, lenient, timeout, fields, from, sort, size, terminate_after
  
  - Example: Using URI: q search
  
**Step 1:** Run this query in your Kibana Console: **GET myplaylist/song/_search?q=Year:2012*

**Step 2:** You need to get the following result:

{\
  "took" : 955,\
  "timed_out" : false,\
  "_shards" : {\
    "total" : 1,\
    "successful" : 1,\
    "skipped" : 0,\
    "failed" : 0\
  },\
  "hits" : {\
    "total" : {\
      "value" : 1,\
      "relation" : "eq"\
    },\
    "max_score" : 0.4700036,\
    "hits" : [\
      {\
        "_index" : "myplaylist",\
        "_type" : "song",\
        "_id" : "7",\
        "_score" : 0.4700036,\
        "_source" : {\
          "title" : "My holiday",\
          "Artist" : "Shubzz",\
          "Album" : "Linkin Park",\
          "Year" : "2012"\
        }\
      }\
    ]\
  }\
}

# C. Aggregation API

- Aggregation collects all the data which is selected by the search query

- This framework consists of many building blocks called aggregators, which help in building complex summaries of the data

- Below is the **syntax** of the aggregation,

 "aggregations" : {\
 "<aggregation_name>" : {\
 "<aggregation_type>" : {\
 <aggregation_body>\
 }\
 [, "meta" : { [<meta_data_body>] } ]?\
 [, "aggregations" : { [<sub_aggregation>] + } ]?\
 }\
 [, "<aggregation_name_2>" : { ... } ]*\
 }
 
- **Aggregation - Types**:

  - Bucketing
  - Metric
  - Matrix
  - Pipeline

# D. Index API

- Index APIs are responsible formanaging all the aspects ofindex like settings, aliases, mappings, index templates 

- Create Index, Get Index, Index Exits, Delete Index, Index Aliases, Analyze, Index Stats, Refresh are some keywords/operations that we can do using the index APIs

![Screenshot (183)](https://user-images.githubusercontent.com/63872951/115782998-f3e47b00-a3d9-11eb-9597-49902ca5d52e.png)


# E. Cluster API

- Cluster API is used to get the information about the cluster andits nodes andmaking changes in them

- One can get information like Cluster Health, Cluster Stats, Cluster State, Cluster Pending Task, etc

![Screenshot (185)](https://user-images.githubusercontent.com/63872951/115782777-b122a300-a3d9-11eb-84d3-0e5b88014acc.png)


Example: Cluster Health API

**Step 1:** Run this query in your Kibana Console: **GET _cluster/health**

**Step 2:** Check for following result,

{\
  "cluster_name" : "elasticsearch",\
  "status" : "yellow",\
  "timed_out" : false,\
  "number_of_nodes" : 1,\
  "number_of_data_nodes" : 1,\
  "active_primary_shards" : 313,\
  "active_shards" : 313,\
  "relocating_shards" : 0,\
  "initializing_shards" : 0,\
  "unassigned_shards" : 39,\
  "delayed_unassigned_shards" : 0,\
  "number_of_pending_tasks" : 0,\
  "number_of_in_flight_fetch" : 0,\
  "task_max_waiting_in_queue_millis" : 0,\
  "active_shards_percent_as_number" : 88.92045454545455\
}


- You can try any of above API for getting information about Cluster

# Query DSL

- Elasticsearch provides a full Query DSL(Domain-Specified Language) based onJSON to define queries
- Query DSL is an AST of queries, consisting of of two types of clause, majorly,
  
  - Leaf Query Cluse(Looks for particular value in a particular field)
  - Compound Query Clause(Combines Leaf Query Clause and other clauses to form a query)

# Mapping

- Mapping is the process of defining how a document, and the fields that it contains, are stored and indexed

- **Mapping Types**

  1. Meta-fields
  2. Fields or Properties
  
- **Field Data Types**

  1. Core Data Types
  2. Complex Data Types
  3. Geo Data Types
  4. Specialized Data Types

- **Mapping Parameters**

![Screenshot (186)](https://user-images.githubusercontent.com/63872951/115829696-e73d4280-a42c-11eb-80db-c62e52af6ee2.png)

# Analysis

- **During a search operation when a query is processed, the content in any index is analyzed by analysis module**

- **The analyzer module contains the following,**

![Screenshot (187)](https://user-images.githubusercontent.com/63872951/115969102-ee616f00-a558-11eb-9a4a-54c901108dc7.png)

- The process of converting a text into a token and terms which are added to an inverted index for search is called analysis. It is carried out using analyzer.
- Analyzer can be in-built or custom
- An analyzer converts the fields into tokens 

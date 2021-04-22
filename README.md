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

## Document API

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

# Search API

### Using a search API, you can execute a search query and get back search hits that match the query

**1. Multi Index:** You can search for the documents present in all the indices or in some specific indices

**2. Multi-Type:** You can search all the documents in an index across all types or in some specified type

**3. UIR Search:** Various parameters can be passed in a search operation using Uniform Resource Identifier:
  - e.g. q, lenient, timeout, fields, from, sort, size, terminate_after
  



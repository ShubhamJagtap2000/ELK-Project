#We need to connect to our ElasticSearch first, fo that refer to the reference link provided in the README.md for explaination

import elasticsearch
import eland as ed
from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['host_server_name'],
    http_auth=('YOUR_USERNAME', 'YOUR_PASSWORD'),
    scheme="https",
    port=443,
)

es.ping()

df = ed.DataFrame(es, es_index_pattern="NAME_OF_INDEX_PATTERN")     

df

/////////////////////////////////////////////////////////////////////////////////////////////////////


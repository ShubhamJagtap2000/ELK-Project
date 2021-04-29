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

#Get the names of all available indices on ElasticSearch as output
rec = es.indices.get_alias("*")
for Name in rec:
    print(Name)

#Choose the index whose data you are interested in
df = ed.DataFrame(es, es_index_pattern="NAME_OF_INDEX_PATTERN")     

#Print the data in chosen index in the form of eland dataframe
df


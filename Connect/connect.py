import elasticsearch
import eland as ed
from elasticsearch import Elasticsearch

# Connecting to an Elastic Cloud instance(remote)
es = Elasticsearch(
    ['host_server_name'],
    http_auth=('YOUR_USERNAME', 'YOUR_PASSWORD'),
    scheme="https",
    port=443,
)

#you can also use this one-liner
#es = Elasticsearch(['https://YOUR_USERNAME:YOUR_PASSWORD@HOST_SERVER_NAME:PORT'])

#Invoke and import index data into eland dataframe
df = ed.DataFrame(es, es_index_pattern="NAME_OF_INDEX_PATTERN")     

#Check whether the Elasticsearch respond
es.ping()

df


# For connecting Elastic cloud on your localhost
df = ed.DataFrame("localhost:9200", es_index_pattern="NAME_OF_INDEX_PATTERN")
df

#Refer to README.md file for a detailed code and execution steps
import elasticsearch
import eland as ed
from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['host_server_name'],
    http_auth=('YOUR_USERNAME', 'YOUR_PASSWORD'),
    scheme="https",
    port=443)

#Following syntax is used to create an index into your Elasticsearch
es.indices.create(index = "My_First_Index", ignore = 400)

#Check or Fetch the created index
df = ed.DataFrame(es, es_index_pattern="mydata")  
df

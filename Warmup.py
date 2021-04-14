import elasticsearch
import pandas as pd

from elasticsearch import Elasticsearch


es = Elasticsearch(
    ['host_server_name'],
    http_auth=('YOUR_USERNAME', 'YOUR_PASSWORD'),
    scheme="https",
    port=443,
)

#you can also use this one-liner
#es = Elasticsearch(['https://Shubham:9V6yx+RbBw29@elastic.firewires.in:443'])

es.ping()          #Check whether the Elasticsearch responds

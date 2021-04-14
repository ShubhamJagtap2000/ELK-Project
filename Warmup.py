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
#es = Elasticsearch(['https://YOUR_USERNAME:YOUR_PASSWORD@HOST_SERVER_NAME:PORT'])

es.ping()          #Check whether the Elasticsearch responds

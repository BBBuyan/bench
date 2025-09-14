import os
from elasticsearch import Elasticsearch

ip = os.getenv("ELASTIC_IP")
port = os.getenv("ELASTIC_PORT")
url = f"http://{ip}:{port}/"

client = Elasticsearch(url, request_timeout=60)
 
if __name__ =="__main__":
    print(client.info())

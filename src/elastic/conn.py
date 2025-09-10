import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()
ip = os.getenv("ELASTIC_IP")
port = os.getenv("ELASTIC_PORT")
url = f"http://{ip}:{port}/"

client = Elasticsearch(url)
 
if __name__ =="__main":
    print(client.info())

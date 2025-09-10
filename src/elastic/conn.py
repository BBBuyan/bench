import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

ip = os.getenv("ELASTIC_IP")
port = os.getenv("ELASTIC_PORT")
url = f"http://{ip}:{port}/"

client = Elasticsearch(url)
 
if __name__ =="__main__":
    print("hello")
    print(client.info())

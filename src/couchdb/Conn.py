import os
from dotenv import load_dotenv

load_dotenv()

ip = os.getenv("COUCH_IP")
port = os.getenv("COUCH_PORT")
user = os.getenv("COUCH_USER")
password = os.getenv("COUCH_PASSWORD")
root_url = f"http://{user}:{password}@{ip}:{port}/"

print(root_url)

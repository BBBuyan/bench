import os
from dotenv import load_dotenv

load_dotenv()
ip = os.getenv("ELASTIC_IP")
port = os.getenv("ELASTIC_PORT")
url = f"http://{ip}:{port}/"


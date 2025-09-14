import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

ip = os.getenv("COUCH_IP")
port = os.getenv("COUCH_PORT")
user = os.getenv("COUCH_USER")
password = os.getenv("COUCH_PASSWORD")
root_url = f"http://{user}:{password}@{ip}:{port}/"

if __name__ == "__main__":
    print(root_url)

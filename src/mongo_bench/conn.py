from pymongo import MongoClient
from pymongo.collection import Collection
from dotenv import load_dotenv
from os import getenv

load_dotenv()
ip = load_dotenv("MONGO_URL")
port = load_dotenv("MONGO_PORT")
connectionString = f"mongodb://{ip}:{port}"

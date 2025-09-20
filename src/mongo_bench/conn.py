from pymongo import MongoClient
from pymongo.collection import Collection
from dotenv import load_dotenv
from os import getenv
from src.mongo_bench.mongo_types import ObjMongo, ArrMongo, FlatMongo

load_dotenv()
ip = getenv("MONGO_URL")
port = getenv("MONGO_PORT")
connectionString = f"mongodb://{ip}:{port}"

cl = MongoClient(connectionString)
db = cl["deep"]

levels = [1,2,4,8]

flat_list: list[FlatMongo]= [FlatMongo(db["flat"])]
obj_list: list[ObjMongo] = [ObjMongo(i, db[f"obj{i}"]) for i in levels]
arr_list: list[ArrMongo] = [ArrMongo(i, db[f"arr{i}"]) for i in levels]

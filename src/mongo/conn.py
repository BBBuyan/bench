from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
from .mongo_types import BaseMongo, ObjMongo, ArrMongo, FlatMongo

load_dotenv()
ip = getenv("MONGO_URL")
port = getenv("MONGO_PORT")
connectionString = f"mongodb://{ip}:{port}"

cl = MongoClient(connectionString)
db = cl["deep"]

levels = [1,2,4,8]

flat_list: list[BaseMongo]= [FlatMongo(db["flat"])]
obj_list: list[BaseMongo] = [ObjMongo(i, db[f"obj{i}"]) for i in levels]
arr_list: list[BaseMongo] = [ArrMongo(i, db[f"arr{i}"]) for i in levels]
all_list: list[BaseMongo] = flat_list + obj_list + arr_list

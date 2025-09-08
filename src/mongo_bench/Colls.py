import os
from pymongo import MongoClient
from pymongo.collection import Collection
from dotenv import load_dotenv
from coll_types.Arr import Arr
from coll_types.Flat import Flat
from coll_types.Obj import Obj
from coll_types.Base import Base

load_dotenv()
ip = os.getenv("MONGO_URL")
port = os.getenv("MONGO_PORT")

connection_string = f"mongodb://{ip}:{port}"

client = MongoClient(connection_string)
db = client["deep"]

levels = [1,2,4,8]

flat_list: list[Base] = [Flat(db.flat)]
obj_list: list[Base] = [Obj(db[f"obj{i}"], i) for i in levels]
arr_list: list[Base] = [Arr(db[f"arr{i}"], i) for i in levels]

from .mongo_types.BaseMongo import BaseMongo
from . import mongo_helper as helper

def insert_warmup(type: BaseMongo):
    print(f"  insert warmup {type.name}", end=" ", flush=True)
    batch = helper.fetch_data_from_file(type, 100)
    type.coll.insert_many(batch)
    print("done")


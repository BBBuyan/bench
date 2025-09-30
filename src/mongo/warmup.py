from .mongo_types.BaseMongo import BaseMongo
from . import mongo_helper as helper
from . import mongo_operations as op

def insert_warmup(type: BaseMongo):
    print(f"---INSERT WARMUP {type.name}", end=", ", flush=True)
    batch = helper.fetch_data_from_file(type, 100)
    type.coll.insert_many(batch)
    print("DONE---")

def read_warmup(type: BaseMongo):
    print(f"---WARMUP {type.name}", end=", ", flush=True)
    for _ in range(3):
        op.time_read(type)
    print("DONE---")

def read_by_shard_key(type: BaseMongo):
    print(f"---WARMUP {type.name}", end=", ", flush=True)
    for _ in range(3):
        op.time_read_by_shard_key(type)
    print("DONE---")


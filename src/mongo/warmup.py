from .mongo_types.BaseMongo import BaseMongo
from . import mongo_helper as helper
from . import mongo_operations as op

def insert_warmup(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    batch = helper.fetch_data_from_file(type, 100)
    type.coll.insert_many(batch)
    print("done")

def read_warmup(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    for _ in range(3):
        op.time_read(type)
    print("done")

def read_by_shard_key(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    for _ in range(3):
        op.time_read_by_shard_key(type)
    print("done")

def update_non_indexed_field(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    for _ in range(3):
        op.time_update_storage(type)
    print("done")

def update_indexed_field(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    for _ in range(3):
        op.time_update_error_count(type)
    print("done")

def update_by_shard_key(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    for _ in range(3):
        op.time_update_by_shard_key(type)
    print("done")


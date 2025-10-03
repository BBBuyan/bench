from .mongo_types.BaseMongo import BaseMongo
from . import mongo_helper as helper
from . import mongo_operations as op

def insert_warmup(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    batch = helper.fetch_for_warmup(type)
    type.coll.insert_many(batch, ordered=False)
    print("DONE---")

def read_warmup(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    for _ in range(3):
        op.time_read(type)
    print("DONE---")

def read_by_shard_key(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    for _ in range(3):
        op.time_read_by_shard_key(type)
    print("DONE---")

def update_non_indexed_field(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    for _ in range(3):
        op.time_update_storage(type)
    print("DONE---")

def update_indexed_field(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    for _ in range(3):
        op.time_update_error_count(type)
    print("DONE---")

def update_by_shard_key(type: BaseMongo):
    print(f"warmup {type.name}", end=" ", flush=True)
    for _ in range(3):
        op.time_update_by_shard_key(type)
    print("DONE---")


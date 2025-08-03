from random import randint
from pymongo.collection import Collection

def create_batch(batch_size):
    batch = []
    for _ in range(batch_size):
        el = {
            "num_of_records": randint(0,999),
            "activity_sec": randint(0,99),
            "application": "insert_batch_member",
            "device": randint(0,9999),
            "volume_total_bytes": randint(0,9999),
            "subscribers": randint(0,999),
        }
        batch.append(el)
    return batch

def create_index(coll: Collection):
    coll.create_index([("device", 1)])

def delete_indexes(coll: Collection):
    coll.drop_indexes()

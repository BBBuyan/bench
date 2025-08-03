from random import randint
from time import perf_counter
from pymongo.collection import Collection
from flat_helpers import create_batch

def time_read(coll: Collection, device_id: int)-> float:
    start = perf_counter()
    result = list(coll.find({"device": device_id}))
    end = perf_counter()
    return end - start

def time_update(coll: Collection, device_id: int)-> float:
    new_vol = randint(0, 9999)
    start = perf_counter()
    coll.update_many({"device": device_id}, {"$set": {"volume_total_bytes": new_vol}})
    end = perf_counter()
    return end - start

def time_group(coll: Collection)-> float:
    group_pipeline = [
        {"$group": {"_id": "$device"}},
        {"$sort": {"_id":1}}
    ]
    start = perf_counter()
    result = list(coll.aggregate(group_pipeline))
    end = perf_counter()

    return end - start

def time_avg(coll: Collection)-> float:
    avg_pipeline = [
        {"$match": {"device": {"$gte": 9000}}},
        {"$group": {"_id": None, "average_volume": {"$avg": "$volume_total_bytes"}}}
    ]
    start = perf_counter()
    result = list(coll.aggregate(avg_pipeline))
    end = perf_counter()

    return end - start

def time_insert(coll: Collection)-> float:
    batch = create_batch(100)

    start = perf_counter()
    coll.insert_many(batch)
    end = perf_counter()

    return end - start


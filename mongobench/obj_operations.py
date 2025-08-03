from time import perf_counter
from pymongo.collection import Collection
import obj_helpers as helper

def time_read(coll: Collection, depth: int, device_id: int):
    where_clause = helper.where_device_builder(depth, device_id)
    start = perf_counter()
    list(coll.find(where_clause))
    end = perf_counter()

    return (end - start) * 1000

def time_update(coll: Collection, depth: int, device_id: int):
    where_clause = helper.where_device_builder(depth, device_id)
    update_clause = helper.update_clause_builder(depth)
    start = perf_counter()
    coll.update_many(where_clause, update_clause)
    end = perf_counter()

    return (end - start) * 1000

def time_insert(coll: Collection):
    batch = helper.generate_insert_batch(coll, 500)
    start = perf_counter()
    coll.insert_many(batch)
    end = perf_counter()
    
    return (end - start) * 1000

def time_avg(coll: Collection, depth: int):
    avg_pipe = helper.avg_pipe_builder(depth)
    start = perf_counter()
    result = list(coll.aggregate(avg_pipe))
    end = perf_counter()

    return (end - start) * 1000

def time_group(coll: Collection, depth: int):
    group_pipe = helper.group_pipe_builder(depth)
    start = perf_counter()
    result = list(coll.aggregate(group_pipe))
    end = perf_counter()

    return (end - start) * 1000



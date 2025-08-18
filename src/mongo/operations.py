from time import perf_counter
from pymongo.collection import Collection
from coll_type import CollType
import builders
import helper

def time_read(
        depth: int, 
        sub_id: int, 
        type: CollType, 
        coll: Collection
)-> float:
    where_clause = builders.read_where_builder(type, depth, sub_id)

    start = perf_counter()
    result = list(coll.find(where_clause))
    end = perf_counter()

    return (end - start) * 1000

def time_update(
        depth: int, 
        sub_id: int, 
        type: CollType, 
        coll: Collection
)-> float:
    where_clause = builders.update_where_builder(type, depth, sub_id)
    update_clause = builders.update_clause_builder(type, depth)

    start = perf_counter()
    coll.update_many(where_clause, update_clause)
    end = perf_counter()

    return (end - start) * 1000

def time_insert(coll: Collection)-> float:
    batch = helper.generate_insert_batch(500, coll)

    start = perf_counter()
    coll.insert_many(batch)
    end = perf_counter()

    return (end - start) * 1000

def time_group(
        depth: int, 
        type: CollType, 
        coll: Collection
)-> float:
    group_pipe = builders.group_pipe_builder(type, depth)

    start = perf_counter()
    result = list(coll.aggregate(group_pipe))
    end = perf_counter()

    return (end - start) * 1000

def time_avg(
        depth: int, 
        type: CollType, 
        coll: Collection
)-> float:
    avg_pipe = builders.avg_pipe_builder(type, depth)

    start = perf_counter()
    result = list(coll.aggregate(avg_pipe))
    end = perf_counter()

    return (end - start) * 1000

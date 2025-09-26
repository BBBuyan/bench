from time import perf_counter
from . import mongo_helper as helper
from .mongo_types.BaseMongo import BaseMongo
from . import mongo_query as query

def time_read(type: BaseMongo):
    where_clause = query.where_error_clause(type)
    start = perf_counter()
    result = list(type.coll.find(where_clause))
    end = perf_counter()

    if BaseMongo.is_debug:
        print(result[0])
        print(len(result))
    return (end - start) * 1000

# Storage field is non indexed and not shard key
def time_update_storage(type: BaseMongo):
    where_clause = query.where_error_clause(type)
    update_clause = query.update_storage(type)
    start = perf_counter()
    result = type.coll.update_many(where_clause, update_clause)
    end = perf_counter()

    if BaseMongo.is_debug:
        print(result.matched_count)

    return (end - start) * 1000

# Error_count field is indexed field, but not shard keay
def time_update_error_count(type: BaseMongo):
    where_clause = query.where_error_clause(type)
    update_clause = query.update_error_count(type)
    start = perf_counter()
    result = type.coll.update_many(where_clause, update_clause)
    end = perf_counter()

    if BaseMongo.is_debug:
        print(result.matched_count)

    return (end - start) * 1000

# Memory_usage field is shard key, thus indexed
def time_update_memory(type: BaseMongo):
    where_clause = query.where_error_clause(type)
    update_clause = query.update_memory(type)
    start = perf_counter()
    result = type.coll.update_many(where_clause, update_clause)
    end = perf_counter()

    if BaseMongo.is_debug:
        print(result.matched_count)

    return (end - start) * 1000

def time_insert(type: BaseMongo):
    batch = helper.fetch_data_from_file(type)

    start = perf_counter()
    result = type.coll.insert_many(batch)
    end = perf_counter()

    if BaseMongo.is_debug:
        print(len(result.inserted_ids))

    return (end - start) * 1000

def time_group(type: BaseMongo):
    group_pipe = query.group_pipe(type)

    start = perf_counter()
    result = list(type.coll.aggregate(group_pipe))
    end = perf_counter()

    if BaseMongo.is_debug:
        print(len(result))

    return (end - start) * 1000

def time_avg(type: BaseMongo):
    avg_pipe = query.avg_pipe(type)

    start = perf_counter()
    result = list(type.coll.aggregate(avg_pipe))
    end = perf_counter()

    if BaseMongo.is_debug:
        print("---")
        print(avg_pipe)
        print(result)
        print("---")

    return (end - start) * 1000

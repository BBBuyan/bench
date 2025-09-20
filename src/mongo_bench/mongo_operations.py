from time import perf_counter
from src.mongo_bench import mongo_helper as helper
from src.mongo_bench.mongo_types.BaseMongo import BaseMongo
from src.mongo_bench import mongo_query as query


def time_read(type: BaseMongo):
    where_clause = query.where_error_clause(type)
    start = perf_counter()
    result = list(type.coll.find(where_clause))
    end = perf_counter()
    return (end - start) * 1000

def time_update(type: BaseMongo):
    where_clause = query.where_error_clause(type)
    update_clause = query.update_storage(type)
    start = perf_counter()
    type.coll.update_many(where_clause, update_clause)
    end = perf_counter()
    return (end - start) * 1000

def time_insert(type: BaseMongo):
    batch = helper.fetch_data_from_file(type)

    start = perf_counter()
    type.coll.insert_many(batch)
    end = perf_counter()

    return (end - start) * 1000

def time_group(type: BaseMongo):
    group_pipe = builder.group_pipe(type)

    start = perf_counter()
    result = list(type.coll.aggregate(group_pipe))
    end = perf_counter()

    return (end - start) * 1000

def time_avg(type: BaseMongo):
    avg_pipe = builder.avg_pipe(type)
    start = perf_counter()
    result = list(type.coll.aggregate(avg_pipe))
    end = perf_counter()
    return (end - start) * 1000

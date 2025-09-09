from coll_types.Base import Base
from time import perf_counter
import builder
import helper

def time_read(type: Base):
    where_clause = builder.where_sub_clause(type)
    start = perf_counter()
    result = list(type.coll.find(where_clause))
    end = perf_counter()
    return (end - start) * 1000

def time_update(type: Base):
    where_clause = builder.where_sub_clause(type)
    update_clause = builder.update_num_clause(type)
    start = perf_counter()
    type.coll.update_many(where_clause, update_clause)
    end = perf_counter()
    return (end - start) * 1000

def time_insert(type: Base):
    batch = helper.fetch_data_from_file(type)

    start = perf_counter()
    type.coll.insert_many(batch)
    end = perf_counter()

    return (end - start) * 1000

def time_group(type: Base):
    group_pipe = builder.group_pipe(type)

    start = perf_counter()
    result = list(type.coll.aggregate(group_pipe))
    end = perf_counter()

    return (end - start) * 1000

def time_avg(type: Base):
    avg_pipe = builder.avg_pipe(type)
    start = perf_counter()
    result = list(type.coll.aggregate(avg_pipe))
    end = perf_counter()
    return (end - start) * 1000

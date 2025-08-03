from time import perf_counter
from pymongo.collection import Collection
import arr_helpers as helper

select_1 = {"a1.device": {"$gte": 9480}}
select_2 = {"a1.a2.device": {"$gte": 9740}}
select_4 = {"a1.a2.a3.a4.device": {"$gte": 9930}}
select_8 = {"a1.a2.a3.a4.a5.a6.a7.a8.device": {"$gte": 9995}}
select_list = [select_1, select_2, select_4, select_8]

update_where_1=  {"a1.device": {"$gte": 9750}}
update_where_2=  {"a1.a2.device": {"$gte": 9870}}
update_where_4=  {"a1.a2.a3.a4.device": {"$gte": 9968}}
update_where_8 = {"a1.a2.a3.a4.a5.a6.a7.a8.device": {"$gte": 9998}}
update_where_list = [update_where_1,update_where_2,update_where_4,update_where_8]


def time_read(coll: Collection, depth: int, device_id: int)-> float:
    where_clause = helper.read_where_builder(depth, device_id)
    start = perf_counter()
    list(coll.find(where_clause))
    end = perf_counter()

    return (end - start) * 1000

def time_update(coll: Collection, depth: int, device_id: int)-> float:
    where_clause = helper.update_where_builder(depth, device_id)
    update_clause = helper.update_clause_builder(depth)
    start = perf_counter()
    coll.update_many(where_clause, update_clause)
    end = perf_counter()

    return (end - start) * 1000

def time_insert(coll: Collection)-> float:
    batch = helper.generate_insert_batch(coll, 500)
    start = perf_counter()
    coll.insert_many(batch)
    end = perf_counter()

    return (end - start) * 1000

def time_group(coll: Collection, depth: int)-> float:
    group_pipe = helper.group_pipe_builder(depth)
    start = perf_counter()
    result = list(coll.aggregate(group_pipe))
    end = perf_counter()

    return (end - start) * 1000

def time_avg(coll: Collection, depth: int)-> float:
    avg_pipe = helper.avg_pipe_builder(depth)
    start = perf_counter()
    result = list(coll.aggregate(avg_pipe))
    end = perf_counter()

    return (end - start) * 1000


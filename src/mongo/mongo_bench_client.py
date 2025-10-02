from .mongo_types import BaseMongo
from . import mongo_workloads as work
from .conn import flat_list, obj_list, arr_list
from . import mongo_logger as logger

db_type = "mongodb"

def run_bench(types: list[BaseMongo]):
    logger.mark_operation(types[0].coll_type)
    logger.mark_message(types[0].coll_type, "")

    work.run_read_only(types)
    work.run_read_only_by_shard_key(types)
    work.run_update_non_indexed_field(types)
    work.run_update_by_shard_key(types)
    work.run_update_indexed_field(types)
    work.run_avg(types)
    work.run_group(types)
    work.run_insert_only(types)

def bench_flat():
    run_bench(flat_list)

def bench_arr():
    run_bench(arr_list)

def bench_obj():
    run_bench(obj_list)



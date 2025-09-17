from src.base_types import Base
from src.elastic import es_workloads as work
from src import logger as log
from src import arr_types, flat_types, obj_types

file_name = "es_result"

def bench_analytics(types: list[Base], coll_type: str):
    read_0 = work.run_read_only(types)
    avg_0 = work.run_avg_only(types)
    group_0 = work.run_group_only(types)
    info_0 = work.run_info_search(types)
    description_0 = work.run_description_search(types)

    log.save_result(read_0, read_0, "read", file_name, coll_type)
    log.save_result(avg_0, avg_0, "avg", file_name, coll_type)
    log.save_result(group_0, group_0, "group", file_name, coll_type)
    log.save_result(info_0, info_0, "info", file_name, coll_type)
    log.save_result(description_0, description_0, "description", file_name, coll_type)

    log.calc_diffs(read_0, read_0, "read")
    log.calc_diffs(avg_0, avg_0, "avg")
    log.calc_diffs(group_0, group_0, "group")
    log.calc_diffs(info_0, info_0, "info")
    log.calc_diffs(description_0, description_0, "description")

def bench_flat():
    bench_analytics(flat_types, "flat")

def bench_obj():
    bench_analytics(obj_types, "obj")

def bench_arr():
    bench_analytics(arr_types, "arr")

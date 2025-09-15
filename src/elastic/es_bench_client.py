from src.base_types import Base
from src.elastic import es_workloads as work
from src import logger as log
from src import arr_types, flat_types, obj_types

file_name = "es_result"

def bench_analytics(types: list[Base]):
    avg_0 = work.run_avg_only(types)
    group_0 = work.run_group_only(types)
    info_0 = work.run_info_search(types)
    read_0 = work.run_read_only(types)
    description_0 = work.run_description_search(types)

    log.save_result(avg_0, avg_0, "read", file_name)
    log.save_result(group_0, group_0, "avg", file_name)
    log.save_result(info_0, info_0, "group", file_name)
    log.save_result(read_0, read_0, "info", file_name)
    log.save_result(description_0, description_0, "description", file_name)

    log.calc_diffs(avg_0, avg_0, "read")
    log.calc_diffs(group_0, group_0, "avg")
    log.calc_diffs(info_0, info_0, "group")
    log.calc_diffs(read_0, read_0, "info")
    log.calc_diffs(description_0, description_0, "description")

def bench_flat():
    log.mark_operation("flat", file_name)
    bench_analytics(flat_types)
    log.mark_end(file_name)

def bench_obj():
    log.mark_operation("obj", file_name)
    bench_analytics(obj_types)
    log.mark_end(file_name)

def bench_arr():
    log.mark_operation("arr", file_name)
    bench_analytics(arr_types)
    log.mark_end(file_name)

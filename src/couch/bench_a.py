from src.couch import logger
from src.couch.db_types import Base
from src.couch.workloads import analytic as work_a
from src.couch.Databases import flat_list, arr_list, obj_list

file_name = "result"
message =""

def bench(db_list: list[Base]):
    # work_a.run_avg_only(db_list)
    # work_a.run_avg_after_update(db_list)

    work_a.run_group_only(db_list)
    # work_a.run_group_after_update(db_list)

    # work_a.run_group_after_insert(db_list)
    # work_a.run_avg_after_insert(db_list)

def bench_obj():
    logger.mark_operation("obj")
    logger.mark_message("obj", message)
    bench(obj_list)

def bench_arr():
    logger.mark_operation("arr")
    logger.mark_message("obj", message)
    bench(arr_list)

def bench_flat():
    logger.mark_operation("flat")
    logger.mark_message("obj", message)
    bench(flat_list)

bench_flat()
bench_obj()
bench_arr()


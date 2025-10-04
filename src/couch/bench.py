from src.couch import logger
from .db_types import Base
from .Databases import flat_list, arr_list, obj_list
from .workloads import analytic as work_a
from .workloads import elementary as work


file_name = "result"
message =""

def bench(db_list: list[Base]):
    work.run_read_only(db_list)
    # work.run_read_after_update(db_list)
    # work.run_update_only(db_list)

    # work.run_insert_only(db_list)
    # work.run_read_after_insert(db_list)

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


import helper
import logger
import workloads as work
from Base import Base
from Databases import obj_list, flat_list, arr_list

file_name = "result_special"

def bench_indexes(dbs: list[Base]):
    work.run_read_only(dbs)
    read_only = work.run_read_only(dbs)

    read_update = work.run_read_after_update(dbs)
    read_insert = work.run_read_after_insert(dbs)
    mixed_special = work.run_mixed_special(dbs)

    helper.calc_diffs(read_only, read_update, "read_after_update")
    helper.calc_diffs(read_only, read_insert, "read_after_insert")
    helper.calc_diffs(read_only, mixed_special, "read_mixed")

    logger.save_result(read_only, read_update, "read_after_update", file_name)
    logger.save_result(read_only, read_insert, "read_after_insert", file_name)
    logger.save_result(read_only, mixed_special, "read_mixed_special", file_name)

def bench_indexes_obj():
    logger.mark_operation("obj special", file_name)
    bench_indexes(obj_list)
    logger.mark_end(file_name)

def bench_indexes_flat():
    logger.mark_operation("flat special", file_name)
    bench_indexes(flat_list)
    logger.mark_end(file_name)

if __name__ == "__main__":
    bench_indexes_flat()

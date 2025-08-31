import workloads
from Base import Base
from Databases import flat_list, arr_list, obj_list
import helper
import logger

def bench(db_list: list[Base]):
    # workloads.run_warmup(db_list)

    old_read = workloads.run_read_heavy(db_list)
    old_update = workloads.run_update_heavy(db_list)
    old_update_only = workloads.run_update_only(db_list)
    old_insert = workloads.run_insert_heavy(db_list)
    old_insert_only = workloads.run_insert_only(db_list)
    old_mixed = workloads.run_mixed(db_list)

    helper.create_indexes(db_list)

    # warmup
    # workloads.run_warmup(db_list)

    new_read = workloads.run_read_heavy(db_list)
    new_update = workloads.run_update_heavy(db_list)
    new_update_only = workloads.run_update_only(db_list)
    new_insert = workloads.run_insert_heavy(db_list)
    new_insert_only = workloads.run_insert_only(db_list)
    new_mixed = workloads.run_mixed(db_list)

    helper.delete_indexes(db_list)

    print("read")
    helper.calc_diffs(old_read, new_read)
    logger.save_result(old_read, new_read, "read")

    print("update heavy")
    helper.calc_diffs(old_update, new_update)
    logger.save_result(old_update, new_update, "update heavy")

    print("update only")
    helper.calc_diffs(old_update_only, new_update_only)
    logger.save_result(old_update_only, new_update_only, "update only")

    print("insert heavy")
    helper.calc_diffs(old_insert, new_insert)
    logger.save_result(old_insert, new_insert, "insert")

    print("insert only")
    helper.calc_diffs(old_insert_only, new_insert_only)
    logger.save_result(old_insert_only, new_insert_only, "insert only")

    print("mixed")
    helper.calc_diffs(old_mixed, new_mixed)
    logger.save_result(old_mixed, new_mixed, "mixed")

    logger.mark_end()


def bench_obj():
    logger.mark_operation("obj")
    bench(obj_list)

def bench_arr():
    logger.mark_operation("arr")
    bench(arr_list)

def bench_flat():
    logger.mark_operation("flat")
    bench(flat_list)

bench_obj()

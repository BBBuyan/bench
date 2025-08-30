import workloads
from Base import Base
from Arr import Arr
from Obj import Obj
from Flat import Flat
import helper
import logger

def bench(db_list: list[Base]):
    old_read = workloads.run_read_heavy(db_list)
    old_update = workloads.run_update_heavy(db_list)
    old_update_only = workloads.run_update_only(db_list)
    old_insert = workloads.run_insert_heavy(db_list)
    old_insert_only = workloads.run_insert_only(db_list)
    old_mixed = workloads.run_mixed(db_list)

    helper.create_indexes(db_list)

    Base.use_index = True

    
    #warmup
    workloads.run_read_heavy(db_list)

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
    logger.save_result(old_mixed, new_mixed, "read")

    logger.mark_end()


def bench_obj():
    obj: list[Base] = [Obj(1), Obj(2), Obj(4), Obj(8)]
    logger.mark_operation("obj")
    bench(obj)

def bench_arr():
    arr: list[Base] = [Arr(1), Arr(2), Arr(4), Arr(8)]
    logger.mark_operation("arr")
    bench(arr)

def bench_flat():
    flat: list[Base] = [Flat()]
    logger.mark_operation("flat")
    bench(flat)

bench_flat()

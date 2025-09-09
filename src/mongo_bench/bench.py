import workloads as work
from Colls import arr_list, obj_list, flat_list
from coll_types.Base import Base
from logger import save_result, mark_operation, mark_end

file_name = "base"

def bench(types: list[Base]):
    old_read = work.run_read_heavy(types)
    old_update = work.run_update_heavy(types)
    old_update_only = work.run_update_only(types)
    old_insert = work.run_insert_heavy(types)
    old_insert_only = work.run_insert_only(types)
    old_avg = work.run_avg(types)
    old_group = work.run_group(types)

    for type in types:
        type.create_index()

    new_read = work.run_read_heavy(types)
    new_update = work.run_update_heavy(types)
    new_update_only = work.run_update_only(types)
    new_insert = work.run_insert_heavy(types)
    new_insert_only = work.run_insert_only(types)
    new_avg = work.run_avg(types)
    new_group = work.run_group(types)

    for type in types:
        type.delete_index()

    save_result(old_read, new_read, "read heavy", file_name)
    save_result(old_update, new_update, "update heavy", file_name)
    save_result(old_update_only, new_update_only, "update only", file_name)
    save_result(old_insert, new_insert, "insert heavy", file_name)
    save_result(old_insert_only, new_insert_only, "insert only", file_name)
    save_result(old_avg, new_avg, "avg", file_name)
    save_result(old_group, new_group, "group", file_name)

def bench_flat():
    mark_operation("flat", file_name)
    bench(flat_list)
    mark_end(file_name)

def bench_obj():
    mark_operation("obj", file_name)
    bench(obj_list)
    mark_end(file_name)

def bench_arr():
    mark_operation("arr", file_name)
    bench(arr_list)
    mark_end(file_name)


bench_flat()

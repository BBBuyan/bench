from Base import Base
from Databases import flat_list, arr_list, obj_list
import workloads 


file_name = "result_misc"

def bench_misc(db_list: list[Base]):
    read = workloads.run_read_only(db_list)
    update = workloads.run_update_only(db_list)
    insert = workloads.run_insert_only(db_list)
    read_after_all = workloads.run_read_only(db_list)

    print(f"read: {read}")
    print(f"update: {update}")
    print(f"insert: {insert}")
    print(f"read_after_all: {read_after_all}")

bench_misc(flat_list)

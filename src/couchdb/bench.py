import workloads
from Base import Base
from Arr import Arr
from Obj import Obj
from Flat import Flat
import helper

def main():
    flat_list: list[Base] = [Flat()]
    obj_list: list[Base] = [Obj(1), Obj(2), Obj(4), Obj(8)]
    arr_list: list[Base] = [Arr(1), Arr(2), Arr(4), Arr(8)]

    old_read = workloads.run_read_heavy(flat_list)
    old_update = workloads.run_update_heavy(flat_list)
    old_insert = workloads.run_insert_heavy(flat_list)
    # old_mixed = workloads.run_mixed(flat_list)

    # print("creating index")
    helper.create_indexes(flat_list)
    Base.use_index = True

    new_read = workloads.run_read_heavy(flat_list)
    new_update = workloads.run_update_heavy(flat_list)
    new_insert = workloads.run_insert_heavy(flat_list)
    # new_mixed = workloads.run_mixed(flat_list)

    helper.delete_indexes(flat_list)

    print("read")
    helper.calc_diffs(old_read, new_read)
    print("update")
    helper.calc_diffs(old_update, new_update)
    print("insert")
    helper.calc_diffs(old_insert, new_insert)
    print("mixed")
    # helper.calc_diffs(old_mixed, new_mixed)

main()


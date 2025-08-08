from coll_type import CollType
import workloads
import helper

op_type = CollType.obj

def main():
    print("---Benchmark Started---")
    old_read = workloads.run_read_heavy(op_type)
    old_update = workloads.run_update_heavy(op_type)
    old_avg = workloads.run_avg(op_type)
    old_group = workloads.run_group(op_type)
    old_insert = workloads.run_insert_heavy(op_type)
    old_mixed = workloads.run_mixed(op_type)

    print("---creating indexes---")
    helper.create_indexes(op_type)

    new_read = workloads.run_read_heavy(op_type)
    new_update = workloads.run_update_heavy(op_type)
    new_avg = workloads.run_avg(op_type)
    new_group = workloads.run_group(op_type)
    new_insert = workloads.run_insert_heavy(op_type)
    new_mixed = workloads.run_mixed(op_type)

    helper.delete_indexes(op_type)

    print("---Benchmark Ended---")
    print("---------READ---------")
    helper.calc_diffs(old_read, new_read)
    print("---------UPDATE---------")
    helper.calc_diffs(old_update, new_update)
    print("---------GROUP---------")
    helper.calc_diffs(old_group, new_group)
    print("---------AVG---------")
    helper.calc_diffs(old_avg, new_avg)
    print("---------INSERT---------")
    helper.calc_diffs(old_insert, new_insert)
    print("---------MIXED---------")
    helper.calc_diffs(old_mixed, new_mixed)

if __name__ == "__main__":
    main()

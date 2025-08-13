from coll_type import CollType
import workloads
import helper

op_type = CollType.flat

def main():
    print("---Benchmark Started---")
    old_read = workloads.run_read_heavy(op_type)
    old_update = workloads.run_update_heavy(op_type)
    old_avg = workloads.run_avg(op_type)
    old_group = workloads.run_group(op_type)
    old_insert = workloads.run_insert_heavy(op_type)
    old_mixed = workloads.run_mixed(op_type)
    old_insert_only = workloady.run_insert_only(op_type)

    print("---creating indexes---")
    helper.create_indexes(op_type)

    new_read = workloads.run_read_heavy(op_type)
    new_update = workloads.run_update_heavy(op_type)
    new_avg = workloads.run_avg(op_type)
    new_group = workloads.run_group(op_type)
    new_insert = workloads.run_insert_heavy(op_type)
    new_mixed = workloads.run_mixed(op_type)
    new_insert_only = workloady.run_insert_only(op_type)

    helper.delete_indexes(op_type)

    print("---Benchmark Ended---")
    print("---------READ---------")
    helper.save_result(old_read, new_read, "read")
    print("---------UPDATE---------")
    helper.save_result(old_update, new_update, "update")
    print("---------GROUP---------")
    helper.save_result(old_group, new_group, "group")
    print("---------AVG---------")
    helper.save_result(old_avg, new_avg, "avg")
    print("---------INSERT---------")
    helper.save_result(old_insert, new_insert, "insert")
    print("---------MIXED---------")
    helper.save_result(old_mixed, new_mixed, "mixed")
    print("---------INSERT ONLY---------")
    helper.save_result(old_insert_only, new_insert_only, "insert only")

if __name__ == "__main__":
    main()

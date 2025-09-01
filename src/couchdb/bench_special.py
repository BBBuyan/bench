import helper
import workloads as work
from Base import Base
from Databases import flat_list, obj_list

def bench(dbs: list[Base]):
    helper.create_indexes(dbs)
    read_only = work.run_read_only(dbs)

    read_update = work.run_read_after_update(dbs)
    read_insert = work.run_read_after_insert(dbs)
    mixed_special = work.run_mixed_special(dbs)

    helper.calc_diffs(read_only, read_update)
    helper.calc_diffs(read_only, read_insert)
    helper.calc_diffs(read_only, mixed_special)

    helper.delete_indexes(dbs)

bench(obj_list)

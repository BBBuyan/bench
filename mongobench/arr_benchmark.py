import arr_workloads as arr_work
from arr_helpers import calc_diffs, create_indexes, delete_indexes
from connection import db

# arr_work.run_analytic(db)
read_heavy_0 = arr_work.run_read_heavy(db)
# update_heavy_0 = arr_work.run_update_heavy(db)
# insert_heavy_0 = arr_work.run_insert_heavy(db)
# mixed_0 = arr_work.run_mixed(db)

print("\n----CREATING INDEX---\n")
create_indexes(db)


# arr_work.run_analytic(db)
read_heavy_1 = arr_work.run_read_heavy(db)
# update_heavy_1 = arr_work.run_update_heavy(db)
# insert_heavy_1 = arr_work.run_insert_heavy(db)
# mixed_1 = arr_work.run_mixed(db)
delete_indexes(db)

print("---READ HEAVY---")
calc_diffs(read_heavy_0, read_heavy_1)
# print("---UPDATE HEAVY---")
# calc_diffs(update_heavy_0, update_heavy_1)
# print("---INSERT HEAVY---")
# calc_diffs(insert_heavy_0, insert_heavy_1)
# print("---MIXED---")
# calc_diffs(mixed_0, mixed_1)

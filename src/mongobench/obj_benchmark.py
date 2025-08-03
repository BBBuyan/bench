from connection import db
import obj_workloads as obj_work
import obj_helpers as obj_help

avg_0 = obj_work.run_avg(db)
group_0 = obj_work.run_group(db)
read_heavy_0 = obj_work.run_read_heavy(db)
update_heavy_0 = obj_work.run_update_heavy(db)
insert_heavy_0 = obj_work.run_insert_heavy(db)
mixed_0 = obj_work.run_mixed(db)

print("\n---CREATING INDEXES---\n")
obj_help.create_indexes(db)

avg_1 = obj_work.run_avg(db)
group_1 = obj_work.run_group(db)
read_heavy_1 = obj_work.run_read_heavy(db)
update_heavy_1 = obj_work.run_update_heavy(db)
insert_heavy_1 = obj_work.run_insert_heavy(db)
mixed_1 = obj_work.run_mixed(db)

obj_help.delete_indexes(db)

print("\nREAD HEAVY")
obj_help.calc_diffs(read_heavy_0, read_heavy_1)
print("\nUPDATE HEAVY")
obj_help.calc_diffs(update_heavy_0, update_heavy_1)
print("\nINSERT HEAVY")
obj_help.calc_diffs(insert_heavy_0, insert_heavy_1)
print("\nMIXED")
obj_help.calc_diffs(mixed_0, mixed_1)
print("\nGROUP")
obj_help.calc_diffs(group_0, group_1)
print("\nAVG")
obj_help.calc_diffs(avg_0, avg_1)


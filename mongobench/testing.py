from obj_workloads import run_avg, run_group, run_insert_heavy
import obj_helpers as helper
from pprint import pprint
from connection import db

# for i in range(4):
#     pprint(helper.group_pipe_builder(i))

# helper.count_device_gte(db)

# run_insert_heavy(db)
one = run_avg(db, 5)
helper.create_indexes(db)
two = run_avg(db, 5)
helper.delete_indexes(db)
helper.calc_diffs(one,two)

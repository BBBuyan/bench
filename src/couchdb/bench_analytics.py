from Base import Base
import workloads_analytic as work_a
import helper
from Databases import flat_list

def bench_analytics(types: list[Base]):
    avg_only = work_a.run_avg_only(types)
    group_only = work_a.run_group_only(types)

    avg_after_update = work_a.run_avg_after_update(types)
    avg_after_insert = work_a.run_avg_after_insert(types)

    group_after_update = work_a.run_group_after_update(types)
    group_after_insert = work_a.run_group_after_insert(types)

    avg_mixed = work_a.run_avg_mixed(types)
    group_mixed = work_a.run_group_mixed(types)

    helper.calc_diffs(avg_only, avg_after_update, "avg_after_update")
    helper.calc_diffs(avg_only, avg_after_insert, "avg_after_insert")
    helper.calc_diffs(avg_only, avg_mixed, "avg_mixed")


    helper.calc_diffs(group_only, group_after_update, "group_after_update")
    helper.calc_diffs(group_only, group_after_insert, "group_after_insert")
    helper.calc_diffs(group_only, group_mixed, "group_mixed")

bench_analytics(flat_list)

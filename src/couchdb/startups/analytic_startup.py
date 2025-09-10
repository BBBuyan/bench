from Databases import obj_list, flat_list, arr_list
import helper

def run_obj():
    for db in obj_list:
        helper.create_analytic_views(db)

def run_arr():
    for db in arr_list:
        helper.create_analytic_views(db)

def run_flat():
    helper.create_analytic_views(flat_list[0])

# run_flat()
# run_obj()
# run_arr()

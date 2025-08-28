import requests
import operations
import workloads
from pprint import pprint
from Arr import Arr 
from Obj import Obj
from Flat import Flat
from Base import Base
import helper

levels = [1,2,4,8]
arr_list: list[Base] = []
for level in levels:
    arr_list.append(Arr(level))

obj_list: list[Base] = []
for level in levels:
    obj_list.append(Obj(level))

# for arr in arr_list:
    # print(arr.group_map_func)
    # print("-----")
    # print(arr.average_map_func)
# print(helper.build_analytic_view_doc(arr_list[0]))

# for obj in obj_list:
    # pprint(obj.group_map_func)
    # pprint(obj.average_map_func)
# helper.delete_design_docs(test)

# helper.delete_design_docs(arr_list[0])
# helper.create_analytic_views(obj_list[0])
test = Flat()
# pprint(helper.fetch_random_without_meta(arr_list[0]))
# pprint(helper.fetch_insert_data(arr_list[0]))
# operations.time_update(test)
# pprint(helper.get_updated_data(test))
all_list = arr_list + obj_list
all_list.append(test)

# helper.create_indexes([test])
# helper.delete_indexes([test])
# helper.delete_databases(all_list)
# helper.create_analytic_views(test)

# print(workloads.run_group([test]))

print(helper.fetch_insert_data(obj_list[0]))
print(helper.fetch_insert_data(obj_list[1]))
print(helper.fetch_insert_data(obj_list[2]))
print(helper.fetch_insert_data(obj_list[3]))

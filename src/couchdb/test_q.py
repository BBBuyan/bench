import requests
import operations 
import workloads
from pprint import pprint
import database_operations
from Base import Base
import helper
from Databases import arr_list, obj_list, flat_list

# flat = flat_list[0]
obj = obj_list[0]

# helper.delete_indexes(obj_list)
# helper.create_indexes(obj_list)
# print(operations.time_read(obj))
# print(helper.get_updated_data(obj))

# for o in obj_list:
#     helper.create_analytic_views(o)
# print(operations.time_avg(obj))

# helper.create_analytic_views(flat_list[0])
# pprint(helper.build_analytic_view_doc(flat_list[0]))
# pprint(flat_list[0].get_index_query())
# helper.create_analytic_views(flat_list[0])
Base.debug = True

operations.time_group(flat_list[0])


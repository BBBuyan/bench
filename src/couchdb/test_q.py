import requests
import operations 
import workloads
import workloads_analytic as work_a
from pprint import pprint
import database_operations
from Base import Base
import helper
from Databases import arr_list, obj_list, flat_list


# helper.get_updated_data(arr_list[0])
# helper.delete_indexes(arr_list)
# print(operations.time_read(flat_list[0]))

# helper.create_indexes(flat_list)
# helper.create_analytic_views(flat_list[0])
# helper.delete_analytic_views(flat_list[0])
# operations.time_insert(flat_list[0])
helper.delete_indexes(flat_list)

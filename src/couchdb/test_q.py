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
Base.use_index = True

arr_list: list[Base] = []
for level in levels:
    arr_list.append(Arr(level))

obj_list: list[Base] = []
for level in levels:
    obj_list.append(Obj(level))


test = Flat()

all_dbs = arr_list + obj_list
all_dbs.append(test)

# helper.delete_databases(all_dbs)
# helper.create_indexes(obj_list)

# print(operations.time_read(obj_list[0]))
# helper.create_indexes(obj_list)
# print(operations.time_read(obj_list[0]))
# helper.create_indexes(obj_list)
# print(operations.time_read(arr_list[0]))

# print(arr_list[0].use_index)
# operations.time_read(arr_list[0])

# helper.create_indexes(arr_list)
# operations.time_insert(test)
# print(test.update_path)
# helper.get_updated_data(test)
# pprint(helper.get_updated_data(test))
# print(helper.get_updated_data(test))
print(helper.create_indexes([test]))

from db_types.Flat import Flat
from db_types.Obj import Obj
from db_types.Arr import Arr
from db_types.Base import Base

levels = [1,2,4,8]

arr_list: list[Base] = [Arr(i) for i in levels]
obj_list: list[Base] = [Obj(i) for i in levels]
flat_list: list[Base] = [Flat()]
all_dbs: list[Base] = flat_list + obj_list + arr_list

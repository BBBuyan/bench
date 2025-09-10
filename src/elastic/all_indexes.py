from index_types.Base import Base
from index_types.Arr import Arr
from index_types.Flat import Flat
from index_types.Obj import Obj

levels = [1,2,4,8]
flat_list: list[Base]=[Flat()]
obj_list: list[Base]=[Obj(i) for i in levels]
arr_list: list[Base]=[Arr(i) for i in levels]

all_list = flat_list + obj_list + arr_list

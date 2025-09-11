from src.base_types import Base, Flat, Arr, Obj

levels = [1,2,4,8]
flat_types: list[Base] = [Flat()]
obj_types: list[Base] = [Obj(i) for i in levels]
arr_types: list[Base] = [Arr(i) for i in levels]

all_types: list[Base] = flat_types + obj_types + arr_types



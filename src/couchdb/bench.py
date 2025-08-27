from op_types import Arr, Obj, Flat, Base
import workloads
from pprint import pprint

def main():
    flat_list: list[Base] = [Flat()]
    obj_list: list[Base] = [Obj(1), Obj(2), Obj(4), Obj(8)]
    arr_list: list[Base] = [Arr(1), Arr(2), Arr(4), Arr(8)]

    pprint(workloads.run_insert_heavy(arr_list))



main()

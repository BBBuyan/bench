from coll_type import CollType
from conn import arr_colls, obj_colls, flat
from pymongo.collection import Collection
import paths
from random import randint

def resolve_colls(type: CollType)-> list[Collection]:
    if(type == CollType.flat):
        return flat
    if(type == CollType.obj):
        return obj_colls
    if(type == CollType.arr):
        return arr_colls

def resolve_sub_paths(type: CollType)-> list[str]:
    if(type == CollType.flat):
        return paths.flat_sub_paths
    if(type == CollType.obj):
        return paths.obj_sub_paths
    if(type == CollType.arr):
        return paths.arr_sub_paths

def resolve_vol_paths(type: CollType)-> list[str]:
    if(type == CollType.flat):
        return paths.flat_vol_paths
    if(type == CollType.obj):
        return paths.obj_vol_paths
    if(type == CollType.arr):
        return paths.arr_vol_paths

def resolve_num_paths(type: CollType)-> list[str]:
    if(type == CollType.flat):
        return paths.flat_num_paths
    if(type == CollType.obj):
        return paths.obj_num_paths
    if(type == CollType.arr):
        return paths.arr_num_paths

def create_indexes(type: CollType):
    paths = resolve_sub_paths(type)
    colls = resolve_colls(type)

    for i in range(len(colls)):
        colls[i].create_index(paths[i])

def delete_indexes(type: CollType):
    colls = resolve_colls(type)
    for coll in colls:
        coll.drop_indexes()

def delete_inserted(type: CollType):
    colls = resolve_colls(type)
    for coll in colls:
        print(coll.delete_many({"inserted": True}))

def calc_diffs(old: list[float], new: list[float]):
    print(f"{'':-<45}")
    print(f"|{'depth':^10}|{'w/o index':^10}|{'w index':^10}|{'diff':^10}|")
    print(f"|{'':-^10}|{'':-^10}|{'':-^10}|{'':-^10}|")
    for i in range(len(old)):
        old_val = old[i]
        new_val = new[i]
        diff = ((new_val - old_val)/old_val)*100
        print(f"|{paths.depth_list[i]:^10}|{old[i]:>10.0f}|{new[i]:>10.0f}|{diff:>10.0f}|")
    print(f"{'':-<45}")
    print("\n")

def unwind_up_to(depth: int)-> list:
    unwind = []
    path = ""

    for i in range(paths.depth_list[depth]):
        if i !=0:
            path += "."
        path += f"a{i+1}"
        unwind.append({"$unwind": f"${path}"})

    return unwind

def generate_insert_batch(size: int, coll: Collection):
    offset = randint(0, 9000)
    new_device = randint(0, 9000)

    new_objs = list(coll.find({}, {"_id": 0, "device": 0}).skip(offset).limit(size))

    for el in new_objs:
        el["inserted"] = True
        el["device"] = new_device

    return new_objs


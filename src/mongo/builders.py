from coll_type import CollType
from helper import resolve_num_paths, resolve_sub_paths, resolve_vol_paths, unwind_up_to
from random import randint

thresholds = [8250, 9100, 9760, 9980]

def read_where_builder(type: CollType, depth: int, sub_id: int):
    paths = resolve_sub_paths(type)
    return {paths[depth]: sub_id}

def update_where_builder(type: CollType, depth: int, sub_id: int):
    paths = resolve_sub_paths(type)
    clause = {paths[depth]: sub_id}
    return clause

def update_clause_builder(type: CollType, depth: int):
    new_num = randint(0, 999)
    num_path = resolve_num_paths(type)[depth]

    update_clause = [{"$set": {num_path: new_num}}]
    return update_clause

def avg_pipe_builder(type: CollType, depth: int):
    sub_path = resolve_sub_paths(type)[depth]
    vol_path = resolve_vol_paths(type)[depth]
    threshold = thresholds[depth]
    
    avg_pipe = [
        {"$match": {f"{sub_path}": {"$gte": threshold}}},
        {"$group": {"_id": None, "avg_vol": {"$avg": f"${vol_path}"}}}
    ]

    if type == CollType.arr:
        unwind = unwind_up_to(depth)
        unwind.extend(avg_pipe)
        avg_pipe = unwind

    return avg_pipe

def group_pipe_builder(type: CollType, depth: int):
    sub_path = resolve_sub_paths(type)[depth]

    group_pipe = [
        {"$group": {"_id": f"${sub_path}"}},
        {"$sort": {"_id": 1}}
    ]

    if type == CollType.arr:
        unwind = unwind_up_to(depth)
        unwind.extend(group_pipe)
        group_pipe = unwind

    return group_pipe

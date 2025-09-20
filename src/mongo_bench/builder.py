from random import randint

def where_sub_clause(type: Base):
    clause = { type.sub_path: randint(0, 9999)}
    return clause

def update_num_clause(type: Base):
    update = {type.num_path: randint(0, 999)}
    update_clause = [{"$set": update}]
    return update_clause

def avg_pipe(type: Base):
    match = {type.sub_path: randint(0, 9999)}
    group = {"_id": None, "avg_vol": {"$avg": type.vol_path}}

    clause=[
        {"$match": match},
        {"$group": group}
    ]

    if isinstance(type, Arr):
        clause = type.unwind + clause

    return clause

def group_pipe(type: Base):
    group = {"_id": type.sub_path}
    sort = {"_id": 1}

    clause =[
        {"$group": group},
        {"$sort": sort}
    ]
    return clause

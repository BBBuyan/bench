from random import randint
from .mongo_types.ArrMongo import ArrMongo, BaseMongo

def where_error_clause(type: BaseMongo):
    clause = {type.error_path: randint(0,9999)}
    return clause

def update_storage(type: BaseMongo):
    new_num = randint(0,999)
    clause = [{"$set": {type.storage_path: new_num}}]
    return clause

def group_pipe(type: BaseMongo):
    match_num = randint(0,9999)
    pipe = [
        {"$match": {type.error_path: match_num}},
        {"$sort": {type.storage_path: 1}},
    ]
    if isinstance(type, ArrMongo):
        pipe = type.unwind + pipe

    return pipe

def avg_pipe(type: BaseMongo):
    match_num = randint(0,9999)
    pipe = [
        {"$match": {type.error_path: match_num}},
        {"$group": {"_id": None, "avg_storage": {"$avg": f"${type.storage_path}"}}}
    ]
    if isinstance(type, ArrMongo):
        pipe = type.unwind + pipe

    return pipe

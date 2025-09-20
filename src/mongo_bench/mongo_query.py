from src.base_types import Base
from random import randint

def where_error_clause(type: Base):
    clause = {type.error_path: randint(0,9999)}
    return clause

def update_storage(type: Base):
    new_num = randint(0,999)
    clause = [{"$set": {type.storage_path: new_num}}]
    return clause

def group_pipe(type: Base):
    match_num = randint(0,9999)
    pipe = [
        {"$match": {type.error_path: match_num}},
        {"$sort": {"_id": type.storage_path}},
    ]
    return pipe

def avg_pipe(type: Base):
    match_num = randint(0,9999)
    pipe = [
        {"$match": {type.error_path: match_num}},
        {"$group": {"_id": None, "avg_vol": {"$avg": type.storage_path}}}
    ]
    return pipe

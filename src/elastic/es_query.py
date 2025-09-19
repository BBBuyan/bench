from src.base_types import Arr, Base

def description_query(type: Base, match_str: str):
    query = {
        "match": {
            type.description_path: match_str
        }
    }
    if isinstance(type, Arr):
        query = {
            "nested": {
                "path": type.path,
                "query": query
            }
        }
    return query

def info_query(type: Base, match_str: str):
    query = {
        "match": {
            type.info_path: match_str
        }
    }
    if isinstance(type, Arr):
        query = {
            "nested": {
                "path": type.path,
                "query": query
            }
        }
    return query

def memory_query(type: Base, num: int):
    query = {
        "term": { type._memory_field: num }
    }
    return query

def avg_query(type: Base, num: int):
    filter_ = memory_query(type, num)
    average_ = {
        "average_vol": {
            "avg": { "field": type._storage_field}
        }
    }
    if isinstance(type, Arr):
        average_ = {
            "nested_avg": {
                "nested": {
                    "path": type.path
                },
                "aggs":average_
            }
        }
    query = {
        "size": 0,
        "query": filter_,
        "aggs": average_
    }
    return query

def group_query(type: Base, num: int): 
    filter_ = memory_query(type, num)
    order_clause: dict = {"order": "asc"}
    if isinstance(type, Arr):
        order_clause["nested"] = {"path": type.path}

    sort_ = [ {type.storage_path: order_clause} ]

    query = {
        "query": filter_,
        "sort": sort_
    }
    return query

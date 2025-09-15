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

def device_query(type: Base, num: int):
    query = {
        "term": { type._device_field: num }
    }
    return query

def avg_query(type: Base, num: int):
    filter_ = device_query(type, num)
    average_ = {
        "average_vol": {
            "avg": { "field": type.vol_path }
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
    filter_ = device_query(type, num)
    order_clause: dict = {"order": "desc"}
    if isinstance(type, Arr):
        order_clause["nested"] = {"path": type.path}

    sort_ = [ {type.vol_path: order_clause} ]

    query = {
        "query": filter_,
        "sort": sort_
    }
    return query

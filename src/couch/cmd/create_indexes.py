from ..db_types.Base import Base
from ..Databases import obj_list, flat_list
import requests

def get_analytics_index(type: Base):
    query = {
        "index": {
            "fields": [f"{type.error_path}", f"{type.storage_path}"]
        },
        "name": f"{type.name}-analytics-index",
        "ddoc": "_design/analytics",
        "type": "json"
    }
    return query

def get_error_index(type: Base):
    query = {
        "index": {
            "fields": [f"{type.error_path}"]
        },
        "name": f"{type.name}-error-index",
        "ddoc": "_design/error",
        "type": "json"
    }
    return query

def create_error_indexes():
    print("---Creating Indexes, ", end="", flush=True)
    for op_type in flat_list + obj_list:
        url = op_type.url + "_index"
        query = get_error_index(op_type)
        requests.post(url, json=query)
        print(op_type.name, end=", ", flush=True)
    print("done---")

def create_analytics_indexes():
    print("---Creating Indexes, ", end="", flush=True)
    for op_type in flat_list + obj_list:
        url = op_type.url + "_index"
        query = get_analytics_index(op_type)
        requests.post(url, json=query)
        print(op_type.name, end=", ", flush=True)
    print("done---")

if __name__ =="__main__":
    create_error_indexes()
    create_analytics_indexes()

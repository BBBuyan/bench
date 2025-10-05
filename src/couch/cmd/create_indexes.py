from ..db_types.Base import Base
from ..Databases import obj_list, flat_list
import requests

def get_analytics_query(type: Base):
    query = {
        "index": {
            "fields": [f"{type.error_path}", f"{type.storage_path}"]
        },
        "name": f"{type.name}-analytics-index",
        "type": "json"
    }
    return query

def get_error_index(type: Base):
    query = {
        "index": {
            "fields": [f"{type.error_path}"]
        },
        "name": f"{type.name}-error-index",
        "type": "json"
    }
    return query

def create_indexes(op_types: list[Base]):
    print("---Creating Indexes, ", end="", flush=True)
    for op_type in op_types:
        url = op_type.url + "_index"
        query = get_error_index(op_type)
        requests.post(url, json=query)

        op_type.use_index = True
    print("done---")

if __name__ =="__main__":
    create_indexes(obj_list)
    create_indexes(flat_list)

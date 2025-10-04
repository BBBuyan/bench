from ..db_types.Base import Base
import requests
from ..Databases import obj_list, flat_list

def delete_indexes(op_types: list[Base]):
    print("---Deleting Indexes, ", end="", flush=True)
    for op_type in op_types:
        url = op_type.url + "_index"
        res = requests.get(url)
        data = res.json()
        indexes: list[dict] = data["indexes"]
        my_indexes = filter(lambda i: i["type"] == "json", indexes)
        for ind in my_indexes:
            url += f"/{ind["ddoc"]}/json/{ind["name"]}"
            res = requests.delete(url)
    print("done---")

if __name__ =="__main__":
    delete_indexes(obj_list)
    delete_indexes(flat_list)

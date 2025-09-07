from random import randint
import requests
from db_types.Base import Base
from json import loads

fetch_limit = 50

def fetch_random_batch(op_type: Base):
    url = op_type.url + "_find"
    query = {
        "selector": {},
        "limit": fetch_limit,
        "skip": randint(0, 9500)
    }
    res = requests.post(url, json=query)
    data = res.json()

    return data["docs"]

def get_updated_data(op_type: Base):
    updating_batch = fetch_random_batch(op_type)
    new_batch = fetch_data_from_file(op_type)
    
    for i in range(len(updating_batch)):
        op_type.update(updating_batch[i], new_batch[i])

    return updating_batch

def fetch_data_from_file(op_type: Base):
    data = []
    path = f"../../data/{op_type.name}.json"
    offset = randint(0, 5000)
    i = 0

    with open(path, "r") as f:
        for _ in range(offset):
            next(f, None)

        for line in f:
            json_data = loads(line)
            data.append(json_data)

            i += 1
            if i >= fetch_limit:
                break

    return data

def create_analytic_views(op_type: Base):
    url = op_type.url +"_design/analytic"
    doc = build_analytic_view_doc(op_type)
    res = requests.put(url, json=doc)
    print(res.text)

def build_analytic_view_doc(op_type: Base):
    doc = {
        "id": "_design/analytic",
        "views": {
            "group": {
                "map": op_type.group_map_func,
                "reduce": op_type.group_reduce,
            },
            "average": {
                "map": op_type.average_map_func,
                "reduce": "_stats"
            }
        }
    }
    return doc

def delete_analytic_views(op_type: Base):
    fetch_url = op_type.url + "_design_docs"
    delete_url = op_type.url + "_design/analytic?rev="

    res = requests.get(fetch_url)
    data = res.json()
    docs = data["rows"]
    rev = ""

    for doc in docs:
        rev = doc["value"]["rev"]
        del_res = requests.delete(delete_url+rev)
        print(del_res.text)

def calc_diffs(old: list[float], new: list[float], operation: str):
    depth_list = [1, 2, 4, 8]
    print(f"##{operation}")
    print(f"{'':-<45}")
    print(f"|{'depth':^10}|{'before':^10}|{'after':^10}|{'diff':^10}|")
    print(f"|{'':-^10}|{'':-^10}|{'':-^10}|{'':-^10}|")
    for i in range(len(old)):
        old_val = old[i]
        new_val = new[i]
        diff = ((new_val - old_val)/old_val)*100
        print(f"|{depth_list[i]:^10}|{old[i]:>10.0f}|{new[i]:>10.0f}|{diff:>10.0f}|")
    print(f"{'':-<45}")

def create_indexes(op_types: list[Base]):
    print("---Creating Indexes, ", end="", flush=True)
    for op_type in op_types:
        url = op_type.url + "_index"
        query = op_type.get_index_query()
        requests.post(url, json=query)

        op_type.use_index = True
    print("done---")

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

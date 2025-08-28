from random import randint
import requests
from Base import Base
from pprint import pprint
from json import loads

fetch_limit = 1

def get_updated_data(op_type: Base):
    first_batch = fetch_update_data(op_type)
    second_batch = fetch_update_data(op_type)

    for i in range(len(first_batch)):
        first_batch[i][op_type.update_path] = second_batch[i][op_type.update_path]

    return first_batch

def fetch_update_data(op_type: Base):
    url = op_type.url + "_find"
    query = op_type.get_device_query()
    query["limit"] = 3
    res = requests.post(url, json=query)
    data = res.json()

    return data["docs"]

def fetch_insert_data(op_type: Base):
    data = []
    path = f"../../data/{op_type.name}.json"
    i = 0

    with open(path, "r") as f:
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
        "_id": "_design/analytic",
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

def delete_design_docs(op_type: Base):
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

def calc_diffs(old: list[float], new: list[float]):
    depth_list = [1, 2, 4, 8]
    print(f"{'':-<45}")
    print(f"|{'depth':^10}|{'w/o index':^10}|{'w index':^10}|{'diff':^10}|")
    print(f"|{'':-^10}|{'':-^10}|{'':-^10}|{'':-^10}|")
    for i in range(len(old)):
        old_val = old[i]
        new_val = new[i]
        diff = ((new_val - old_val)/old_val)*100
        print(f"|{depth_list[i]:^10}|{old[i] * 1000:>10.0f}|{new[i] * 1000:>10.0f}|{diff:>10.0f}|")
    print(f"{'':-<45}")

def create_indexes(op_types: list[Base]):
    for op_type in op_types:
        url = op_type.url + "_index"

        query = {
            "index": {
                "fields": [f"{op_type.device_path}"]
            },
            "name": f"{op_type.name}-device-index",
            "type": "json"
        }

        res = requests.post(url, json=query)
        print(res.text)

def delete_indexes(op_types: list[Base]):
    for op_type in op_types:
        url = op_type.url + "_index"
        res = requests.get(url)
        data = res.json()
        indexes: list[dict] = data["indexes"]
        my_indexes = filter(lambda i: i["type"] == "json", indexes)
        for ind in my_indexes:
            url += f"/{ind["ddoc"]}/json/{ind["name"]}"
            res = requests.delete(url)
            pprint(res.text)

def delete_databases(op_types: list[Base]):
    for op_type in op_types:
        res = requests.delete(op_type.url)
        print(res.text)

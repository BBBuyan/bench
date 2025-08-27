from random import randint
import requests
from op_types import Base
from pprint import pprint

fetch_limit = 5

def get_updated_data(op_type: Base):
    url = op_type.url
    first_batch = fetch_random(url)
    second_batch = fetch_random(url)

    for i in range(len(first_batch)):
        first_batch[i][op_type.update_path] = second_batch[i][op_type.update_path]

    return first_batch

def fetch_random(url):
    offset = randint(0, 9500)
    url += "_all_docs"
    url += f"?limit={fetch_limit}"
    url += "&include_docs=true"
    url += f"&skip={offset}"
    res = requests.get(url)
    data = res.json()
    docs = data["rows"]

    random_docs = []
    for doc in docs:
        random_docs.append(doc["doc"])

    return random_docs

def fetch_random_without_meta(url):
    offset = randint(0, 9500)
    url += "_all_docs"
    url += f"?limit={fetch_limit}"
    url += "&include_docs=true"
    url += f"&skip={offset}"
    res = requests.get(url)
    data = res.json()
    docs = data["rows"]

    random_docs = []
    for doc in docs:
        single_doc = doc["doc"]
        single_doc.pop("_id", None)
        single_doc.pop("_rev", None)
        random_docs.append(doc["doc"])

    return random_docs

def create_flat_design_doc(op_type: Base):
    url = op_type.url + "_design/flatgroup"
    doc = {
        "_id": "flatgroup",
        "views": {
            "group": {
                "map": "function (doc) { if(doc.subscribers) emit(doc.subscribers, null)}"
            }
        }
    }
    res = requests.put(url, json=doc)
    print(res.text)

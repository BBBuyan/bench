from random import randint
import requests
from .db_types.Base import Base
from json import loads
from pathlib import Path

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

def fetch_data_from_file(op_type: Base):
    data = []
    path = Path(__file__).parent.parent.parent/"data"/f"{op_type.name}.json"
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

def get_updated_data(op_type: Base):
    updating_batch: list[dict]= fetch_random_batch(op_type)
    new_batch: list[dict] = fetch_data_from_file(op_type)
    
    for i in range(len(updating_batch)):
        updating_batch[i].update(new_batch[i])

    return updating_batch

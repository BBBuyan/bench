from json import loads
from pathlib import Path
from .mongo_types import BaseMongo
from src.base_types import Arr

arr_limit = 500
# arr_limit = 50

base_limit = 50_000
# base_limit = 5000

def fetch_data_from_file(type: BaseMongo):
    path = Path(__file__).parent.parent.parent/"data"/f"{type.name}.json"
    limit = base_limit

    if isinstance(type, Arr):
        limit = arr_limit

    data =[]
    with open(path, "r") as f:
        i = 0
        for line in f:
            json_data = loads(line)
            data.append(json_data)
            i += 1
            if i >= limit:
                break
    return data

def fetch_for_warmup(type: BaseMongo):
    path = Path(__file__).parent.parent.parent/"data"/f"{type.name}.json"
    limit = 50

    data =[]
    with open(path, "r") as f:
        i = 0
        for line in f:
            json_data = loads(line)
            data.append(json_data)
            i += 1
            if i >= limit:
                break
    return data

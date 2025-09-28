from random import randint
from json import loads
from pathlib import Path
from .mongo_types import BaseMongo

def fetch_data_from_file(type: BaseMongo):
    path = Path(__file__).parent.parent.parent/"data"/f"{type.name}.json"
    data =[]
    with open(path, "r") as f:
        i = 0
        for line in f:
            json_data = loads(line)
            data.append(json_data)
            i += 1
            if i >= type.fetch_limit:
                break
    return data

def create_indexes(types: list[BaseMongo]):
    print("---CREATING INDEXES")
    for type in types:
        print(f"{type.name}", end=" ", flush=True)
        type.coll.create_index(type.error_path)
    print("DONE---")

def drop_indexes(types: list[BaseMongo]):
    for type in types:
        type.coll.drop_indexes()

from random import randint
from json import loads
from pathlib import Path
from .mongo_types import BaseMongo

fetch_limit = 50

def fetch_data_from_file(type: BaseMongo):
    path = Path(__file__).parent.parent.parent/"data"/f"{type.name}.json"
    offset = randint(0, type.max_docs)
    i = 0

    data =[]
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

def create_indexes(types: list[BaseMongo]):
    for type in types:
        type.coll.create_index(type.error_path)

def drop_indexes(types: list[BaseMongo]):
    for type in types:
        type.coll.drop_indexes()

from random import randint
from coll_types.Base import Base
from json import loads

fetch_limit = 500

def fetch_data_from_file(type: Base):
    offset = randint(0,5000)
    data = []
    i = 0

    with open(f"../../data/{type.name}.json", "r") as f:
        for _ in range(offset):
            next(f, None)

        for line in f:
            json_data = loads(line)
            data.append(json_data)

            i+=1
            if i >= fetch_limit:
                break

    return data



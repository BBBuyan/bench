from src.base_types import Base
from random import randint
from json import loads
from pathlib import Path

fetch_limit = 50

def fetch_data_from_file(type: Base):
    data =[]
    path = Path(__file__).parent.parent.parent/"data"/f"{type.name}.json"
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

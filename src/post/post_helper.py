from json import loads
from random import randint
from src.post.post_types import BasePost
from pathlib import Path
from psycopg2.extras import Json

insert_limit = 50

def get_data(table: BasePost):
    file_path = Path(__file__).parent.parent.parent/"data"/f"{table.name}.json"
    offset = randint(0,1000)
    batch = []
    i = 0
    with open(file_path, "r") as f:
        for _ in range(offset):
            next(f, None)
        for line in f:
            json_data = loads(line)
            batch.append((Json(json_data),))

            i += 1
            if i >= insert_limit:
                break

    return batch

def get_one_data(table: BasePost):
    file_path = Path(__file__).parent.parent.parent/"data"/f"{table.name}.json"
    offset = randint(0, 1000)
    with open(file_path, "r") as f:
        for _ in range(offset):
            next(f, None)
        line = f.readline()
        json_data = loads(line)
        return Json(json_data)


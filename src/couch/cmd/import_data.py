from time import time
import requests
from ..db_types.Base import Base
from json import loads
from ..Databases import all_dbs, arr_list, obj_list, flat_list
from pathlib import Path

def execute_import(type: Base, json_data: list[dict]):
    url = f"{type.url}_bulk_docs"

    payload = {"docs": json_data}
    r = requests.post(url, json=payload)

    if r.status_code >= 400:
        raise ValueError(r.text)

def import_docs(db: Base):
    batch = []
    start = time()
    file_path = Path(__file__).parent.parent.parent.parent/"data"/f"{db.name}.json"
    print(f"importing {db.name}")
    with open(file_path, "r") as f:
        counter = 0
        iteration = 0

        for line in f:
            json_data = loads(line)
            batch.append(json_data)

            if(len(batch) >= db.batch_limit):
                execute_import(db, batch)
                batch.clear()
                iteration += 1
                if iteration >= 250:
                    counter += iteration
                    iteration = 0
                    print(f"{counter}k")
    end = time()
    print(f"took: {end - start:.0f} s")

if __name__ == "__main__":
    for db in all_dbs:
        import_docs(db)

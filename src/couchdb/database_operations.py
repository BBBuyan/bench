from Base import Base
import requests
from json import loads
from time import time
from Databases import all_dbs

def delete_database(db: Base):
    res = requests.delete(db.url)
    print(res.text)

def create_database(db: Base):
    res = requests.put(db.url)
    print(res.text)

def execute_import(type: Base, json_data: list[dict]):
    url = f"{type.url}_bulk_docs"

    payload = {"docs": json_data}
    r = requests.post(url, json=payload)

    if r.status_code >= 400:
        raise ValueError(r.text)

def import_docs(db: Base):
    name = db.name
    batch = []
    start = time()
    print(f"importing {name}")
    with open(f"../../data/{name}.json", "r") as f:
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

def reset(db: Base):
    delete_database(db)
    create_database(db)

def reset_all():
    for db in all_dbs:
        reset(db)

def delete_databases():
    for db in all_dbs:
        delete_database(db)

def create_databases():
    for db in all_dbs:
        create_database(db)

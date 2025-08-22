import requests
from json import loads
from time import time


def execute_import(name: str, json_data: list[dict]):
    couch_url = "http://admin:secret@192.168.2.87:5984"
    url = f"{couch_url}/{name}/_bulk_docs"

    payload = {"docs": json_data}
    r = requests.post(url, json=payload)

    if r.status_code >= 400:
        raise ValueError(r.text)

def import_data(name: str, batch_limit: int):
    batch = []
    start = time()
    print(f"importing {name}")
    with open(f"../../data/{name}.json", "r") as f:
        counter = 0
        iteration = 0

        for line in f:
            json_data = loads(line)
            batch.append(json_data)

            if(len(batch) >= batch_limit):
                execute_import(name, batch)
                batch.clear()
                iteration += 1
                if iteration >= 250:
                    counter += iteration
                    iteration = 0
                    print(f"{counter}k")
    end = time()
    print(f"took: {end - start:.0f} s")

def import_arrs():
    import_data("arr1", 1000)
    import_data("arr2", 1000)
    import_data("arr4", 1000)
    import_data("arr8", 1000)

def import_objs():
    import_data("obj1", 1000)
    import_data("obj2", 1000)
    import_data("obj4", 1000)
    import_data("obj8", 1000)

def import_flat():
    import_data("flat", 1000)


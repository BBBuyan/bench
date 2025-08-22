from json import loads
from couchdb import Server 
import requests

flat_names = ["flat"]
arr_names = ["arr1", "arr2", "arr4", "arr8"]
obj_names = ["obj1", "obj2", "obj4", "obj8"]

couch_url = "http://admin:secret@192.168.2.87:5984"

def create_databases():
    couch = Server(url=couch_url)
    couch.create("flat")

    couch.create("arr1")
    couch.create("arr2")
    couch.create("arr4")
    couch.create("arr8")

    couch.create("obj1")
    couch.create("obj2")
    couch.create("obj4")
    couch.create("obj8")

def execute_import(name: str, json_data: list[dict]):
    url = f"{couch_url}/{name}/_bulk_docs"

    payload = {"docs": json_data}
    r = requests.post(url, json=payload)

    if r.status_code >= 400:
        raise ValueError(r.text)

def import_data(file_names: list[str], batch_limit: int):
    batch = []
    for i in range(len(file_names)):
        name = file_names[i]
        with open(f"../../data/{name}.json", "r") as f:
            print(f"importing {name}")
            counter = 0

            for line in f:
                json_data = loads(line)
                batch.append(json_data)

                if(len(batch) >= batch_limit):
                    execute_import(name, batch)
                    batch.clear()
                    counter += 1
                    if counter > 10:
                        print(f"inserted {counter * batch_limit}")
                        counter = 0

        if batch:
            execute_import(name, batch)

# create_databases()
import_data(flat_names, 1000)
# import_data(obj_names, 1000)
# import_data(arr_names, 1000)


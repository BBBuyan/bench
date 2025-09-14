from .conn import client
from elasticsearch import helpers
from json import loads
from src.base_types import Base
from pathlib import Path
from . import es_resources as resources

mapping_dict ={
    "flat": resources.flat_mapping,

    "obj1": resources.obj1_mapping,
    "obj2": resources.obj2_mapping,
    "obj4": resources.obj4_mapping,
    "obj8": resources.obj8_mapping,

    "arr1": resources.arr1_mapping,
    "arr2": resources.arr2_mapping,
    "arr4": resources.arr4_mapping,
    "arr8": resources.arr8_mapping,
}

def get_mapping(name: str):
    return mapping_dict[name]

def get_data(db: Base):
    file_path = Path(__file__).parent.parent.parent/"data"/f"{db.name}.json"
    with open(file_path, "r") as f:
        for line in f:
            json_data = loads(line)
            yield {
                "_index": db.name,
                **json_data
            }

def import_data(db: Base):
    if not client.indices.exists(index=db.name):
        print("---Creating Index:", db.name, end=" ")
        mapping_ = get_mapping(db.name)
        client.indices.create(index=db.name, mappings=mapping_)
        print("Created---")

    print(f"---Importing {db.name}", end="", flush=True)
    i = 0
    for ok, res in helpers.streaming_bulk(client, get_data(db)):
        i+=1
        if i % 100 == 0:
            print(res)
        if not ok:
            print("Error", res)
    print(f"  Done---")
    print(i)

if __name__ == "__main__":
    from src.all_types import all_types, arr_types
    # for type in arr_types:
    import_data(arr_types[3])

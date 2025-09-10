from index_types.Base import Base
from conn import client
from elasticsearch import helpers
from json import loads 

def get_data(db: Base):
    with open(f"../../data/{db.name}.json", "r") as f:
        for line in f:
            json_data = loads(line)
            yield {
                "_index": db.name,
                **json_data
            }

def import_data(db: Base):
    if not client.indices.exists(index=db.name):
        client.indices.create(index=db.name)
        print("Created Index: ", db.name)

    for ok, res in helpers.streaming_bulk(client, get_data(db)):
        if not ok:
            print("Error", res)

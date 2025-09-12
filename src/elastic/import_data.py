from .conn import client
from elasticsearch import helpers
from json import loads
from src.base_types import Base
from pathlib import Path

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
        print("---Creating Index: ", db.name)
        client.indices.create(index=db.name)
        print("Created---")

    for ok, res in helpers.streaming_bulk(client, get_data(db)):
        if not ok:
            print("Error", res)

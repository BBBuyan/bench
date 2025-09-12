from .conn import client
from random import randint
from time import perf_counter
from src.base_types import Base

def time_read(type: Base):
    start = perf_counter()
    res = client.search(index=type.name, query={
        "match": {
            type.device_path: randint(0,9999)
        }
    })
    end = perf_counter()

    if type.is_debug == True:
        for i in res["hits"]["hits"]:
            print(i["_source"])
        print(f"{'es took':<20}: {res["took"]} ms")
        print(f"{'count':<20}: {res["hits"]["total"]["value"]}")
        print(f"{'operation':<20}: {(end - start)*1000:.0f} ms")

    return (end-start)*1000

def time_string_read(type: Base):
    start = perf_counter()
    res = client.search(index=type.name, query= {
        "match": {
            type.description_path: "waterproof speaker"
        } 
    })

    end = perf_counter()

    if type.is_debug == True:
        for i in res["hits"]["hits"]:
            print(i["_id"], "| description:", i["_source"]["description"])
        print(f"{'es took':<20}: {res["took"]} ms")
        print(f"{'count':<20}: {res["hits"]["total"]["value"]}")
        print(f"{'operation':<20}: {(end - start)*1000:.0f} ms")

    return (end-start)*1000

def time_avg(type: Base):
    start = perf_counter()
    res = client.search(
        index=type.name,
        body={
            "size":3,
            "query": {
                "match": {type.device_path: randint(0,9999)}
            },
            "aggs": {
                "average_vol":{
                    "avg":{
                        "field": "total_volume_bytes"
                    }
                }

            }
    })
    end = perf_counter()

    if type.is_debug == True:
        for i in res["hits"]["hits"]:
            print(i["_source"])

        print(f"{'es took':<20}: {res["took"]} ms")
        print(f"{'count':<20}: {res["hits"]["total"]["value"]}")
        print(f"{'operation':<20}: {(end - start)*1000:.0f} ms")

    return (end-start)*1000

def time_group(type: Base):
    start = perf_counter()
    res = client.search(
        index=type.name,
        body={
            "query": {
                "match": {"device": randint(0,9999)}
            },
            "sort": [
                {"total_volume_bytes": {"order": "desc"}}
            ]

    })
    end = perf_counter()

    if type.is_debug == True:
        for i in res["hits"]["hits"]:
            print(i["_source"])

        print(f"{'es took':<20}: {res["took"]} ms")
        print(f"{'count':<20}: {res["hits"]["total"]["value"]}")
        print(f"{'operation':<20}: {(end - start)*1000:.0f} ms")

    return (end-start)*1000



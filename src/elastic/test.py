from all_indexes import flat_list, obj_list, arr_list
from conn import client
from index_types.Base import Base
from random import randint
from time import perf_counter

def time_read(type: Base):
    start = perf_counter()
    res = client.search(index=type.name, query={"match": {"device": randint(0,9999)}})
    end = perf_counter()
    # for i in res["hits"]["hits"]:
    #     print(i)

    print(f"{res["took"]} ms")
    print(res["hits"]["total"])
    print(f"{(end - start)*1000} operation ms")

def time_string_read(type: Base):
    start = perf_counter()
    res = client.search(index=type.name, query={"match": {"description": "waterproof speaker"}})
    end = perf_counter()
    for i in res["hits"]["hits"]:
        print(i["_id"], "| description:", i["_source"]["description"])

    print(f"{res["took"]} ms")
    print(res["hits"]["total"])
    print(f"{(end - start)*1000} operation ms")

def time_avg(type: Base):
    res = client.search(
        index=type.name,
        body={
            "size":3,
            "query": {
                "match": {"device": randint(0,9999)}
            },
            "aggs": {
                "average_vol":{
                    "avg":{
                        "field": "total_volume_bytes"
                    }
                }

            }
    })
    for i in res["hits"]["hits"]:
        print(i["_source"])

def time_group(type: Base):
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
    for i in res["hits"]["hits"]:
        print(i)

    print(f"\n{res["took"]} ms")

# time_read(flat_list[0])
# time_string_read(flat_list[0])
time_avg(flat_list[0])
# time_group(flat_list[0])

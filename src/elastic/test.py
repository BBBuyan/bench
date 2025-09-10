from all_indexes import flat_list, obj_list, arr_list
from conn import client
from index_types.Base import Base
from random import randint


def time_read(type: Base):
    res = client.search(index=type.name, query={"match": {"device": randint(0,9999)}})
    for i in res["hits"]["hits"]:
        print(i)

    print(res["took"])
    print(res["hits"]["total"])



def time_avg(type: Base):
    res = client.search(
        index=type.name,
        body={
            "size":0,
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
    print(res)

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
# time_avg(flat_list[0])
time_group(flat_list[0])

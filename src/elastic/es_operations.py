from .conn import client
from random import randint
from time import perf_counter
from src.base_types import Base
from . import es_helper as helper
from . import es_query

info_match_str = "high"
description_match_str = "water"

def time_memory_read(type: Base):
    start = perf_counter()
    num = randint(0,9999)
    query_ = es_query.memory_query(type, num)
    res = client.search(index=type.name, query=query_)
    end = perf_counter()

    if type.is_debug == True:
        helper.show_res(res)

    return (end-start)*1000

def time_info_read(type: Base):
    start = perf_counter()
    query_ = es_query.info_query(type, info_match_str)
    res = client.search(index=type.name, query= query_)
    end = perf_counter()

    if type.is_debug == True:
        helper.show_res(res)

    return (end-start)*1000

def time_description_read(type: Base):
    start = perf_counter()
    query_ = es_query.description_query(type, description_match_str)
    res = client.search(index=type.name, query=query_)
    end = perf_counter()

    if type.is_debug == True:
        helper.show_res(res)

    return (end-start)*1000

def time_avg(type: Base):
    num = randint(0, 9999)
    query_ = es_query.avg_query(type, num)

    start = perf_counter()
    res = client.search( index=type.name, body=query_)
    end = perf_counter()

    if type.is_debug == True:
        print(res)

    return (end-start)*1000

def time_group(type: Base):
    num = randint(0, 9999)
    query_ = es_query.group_query(type, num)

    start = perf_counter()
    res = client.search(index=type.name, body=query_)
    end = perf_counter()

    if type.is_debug == True:
        helper.show_res(res)

    return (end-start)*1000


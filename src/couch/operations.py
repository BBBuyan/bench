from random import randint
from time import perf_counter
import requests
from . import helper
from .db_types.Base import Base
from .db_types.Arr import Arr

def time_read(op_type: Base):
    if isinstance(op_type, Arr):
        return 0

    url = op_type.url + "_find"
    query = op_type.get_error_query()

    start = perf_counter()
    res = requests.post(url, json=query)
    end = perf_counter()

    if op_type.debug:
        print(query)
        print(res.text)

    return (end - start) * 1000

def time_update(op_type: Base):
    url = op_type.url + "_bulk_docs"
    updated_data = helper.get_updated_data(op_type)
    updated_data = {"docs": updated_data}

    start = perf_counter()
    res = requests.post(url, json=updated_data)
    end = perf_counter()
    if op_type.debug:
        print(res.text)

    return (end - start) * 1000

def time_insert(op_type: Base):
    url = op_type.url + "_bulk_docs"
    insert_data = helper.fetch_data_from_file(op_type)
    insert_data = {"docs": insert_data}

    start = perf_counter()
    res = requests.post(url, json=insert_data)
    end = perf_counter()

    if op_type.debug:
        print(res.text)

    return (end - start) * 1000

def time_group(op_type: Base):
    if isinstance(op_type, Arr):
        return 0

    url = op_type.url + "_find"
    query = op_type.get_sort_query()

    start = perf_counter()
    res = requests.post(url, json=query)
    end = perf_counter()

    if op_type.debug:
        print(res.text)

    return (end - start) * 1000

def time_avg(op_type: Base):
    url = op_type.url + "_design/analytic/_view/average?group=true"
    url += f"&key={randint(0, 9999)}"

    start = perf_counter()
    res = requests.get(url)
    end = perf_counter()

    if op_type.debug:
        print(res.text)

    return (end - start) * 1000

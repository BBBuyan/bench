from time import perf_counter
import requests
import helper
from op_types import Base

def time_read(op_type: Base):
    url = op_type.url + "_find"
    query = op_type.get_subscribers_query()

    start = perf_counter()
    res = requests.post(url, json=query)
    end = perf_counter()

    return (end - start)

def time_update(op_type: Base):
    url = op_type.url + "_bulk_docs"
    updated_data = helper.get_updated_data(op_type)
    updated_data = {"docs": updated_data}

    start = perf_counter()
    res = requests.post(url, json=updated_data)
    end = perf_counter()

    print(res.text)

    return (end - start)

def time_insert(op_type: Base):
    url = op_type.url + "_bulk_docs"
    insert_data = helper.fetch_random_without_meta(op_type.url)
    insert_data = {"docs": insert_data}

    start = perf_counter()
    res = requests.post(url, json=insert_data)
    end = perf_counter()

    return (end - start)


def time_group(op_type: Base):
    url = op_type.url + "_find"
    query = op_type.get_subscribers_query()


    pass


def time_avg(op_type: Base):
    pass

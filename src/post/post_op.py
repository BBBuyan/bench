from random import randint
from src.post import post_helper
from src.post.conn import pool
from src.post.post_types import BasePost
from psycopg2.extras import execute_batch
from pprint import pprint
from time import perf_counter

def time_read(table: BasePost):
    query = table.read_query
    param = (randint(0,9999),)

    conn = pool.getconn()
    with conn.cursor() as cursor:
        start = perf_counter()
        cursor.execute(query, param)
        res = cursor.fetchall()
        end = perf_counter()

    pool.putconn(conn)
    if BasePost.is_debug: 
        print(len(res))
        print(query)
        print("param ",  param[0])

    return (end - start) * 1000

def time_avg(table: BasePost):
    query = table.avg_query
    param = (randint(0,9999),)

    conn = pool.getconn()
    with conn.cursor() as cursor:
        start = perf_counter()
        cursor.execute(query, param)
        res = cursor.fetchall()
        end = perf_counter()

    pool.putconn(conn)
    if BasePost.is_debug: 
        pprint(res)
        print(query)
        print(param[0])
    return (end - start) * 1000

def time_sort(table: BasePost):
    query = table.sort_query
    param = (randint(0,9999), )

    conn = pool.getconn()
    with conn.cursor() as cursor:
        start = perf_counter()
        cursor.execute(query, param)
        res = cursor.fetchall()
        end = perf_counter()

    pool.putconn(conn)
    if BasePost.is_debug: 
        pprint(res)

    return (end - start) * 1000

def time_update(table: BasePost):
    conn = pool.getconn()

    oneData = post_helper.get_one_data(table)
    eqParam = randint(0,9999)

    param = (oneData, eqParam)
    query = table.update_storage

    with conn.cursor() as cursor:
        start = perf_counter()
        cursor.execute(query, param)
        end = perf_counter()

        if BasePost.is_debug:
            print(cursor.rowcount)

    conn.commit()
    pool.putconn(conn)

    return (end - start) * 1000

def time_insert(table: BasePost):
    data = post_helper.get_data(table)
    conn = pool.getconn()
    with conn.cursor() as cursor:
        start = perf_counter()
        execute_batch(cursor, f"insert into {table.name} (data) values (%s)", data)
        end = perf_counter()

        if BasePost.is_debug:
            print(cursor.rowcount)

    conn.commit()
    pool.putconn(conn)

    return (end - start) * 1000

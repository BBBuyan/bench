import json
import random
from psycopg2.pool import ThreadedConnectionPool
import time
from psycopg2.extras import execute_values
from resources import generate_batch 
from enum import Enum

data = generate_batch(1000)

class Operation(Enum):
    INSERT =                            "insert into flat (data) values %s"
    GROUP =                             "select (data->>'device')::int as device from flat group by device order by device asc"
    AVG =                               "select avg((data->> 'volume_total_bytes')::int) as average from flat where (data->>'device')::int > 9000"
    WHERE_INDEX_UPDATE_INDEX =          "update flat set data = jsonb_set(data, '{device}', %s, false ) where (data->>'device')::int = %s"
    WHERE_INDEX_UPDATE_NON_INDEX =      "update flat set data = jsonb_set(data, '{application}', %s, false ) where (data->>'device')::int = %s"
    WHERE_NON_INDEX_UPDATE_INDEX =      "update flat set data = jsonb_set(data, '{device}', %s, false ) where (data->>'volume_total_bytes')::int = %s"
    WHERE_NON_INDEX_UPDATE_NON_INDEX =  "update flat set data = jsonb_set(data, '{application}', %s, false ) where (data->>'volume_total_bytes')::int = %s"
    DELETE =                            "delete from flat where (data->>'device')::int > 5000"

def resolve_change(op: Operation,):
    if op in (Operation.WHERE_INDEX_UPDATE_NON_INDEX, Operation.WHERE_NON_INDEX_UPDATE_NON_INDEX):
        return json.dumps(f"updatedObject")
    else:
        return json.dumps(random.randint(0, 9999))

def resolve_operation(op: Operation):
    if op == Operation.INSERT:
        return time_insert
    if op in (Operation.GROUP, Operation.AVG):
        return time_read
    if op == Operation.DELETE:
        return time_delete
    else:
        return time_update

def time_insert(
    pool: ThreadedConnectionPool, 
    user_id,
    duration_list,
    op: Operation
):
    query = op.value
    conn = pool.getconn()

    with conn:
        with conn.cursor() as cursor:
            start = time.perf_counter()
            execute_values(cursor, query, data)
            end = time.perf_counter()
    pool.putconn(conn)

    duration = (end - start) * 1000
    duration_list[user_id] = duration

def time_read(
    pool: ThreadedConnectionPool,
    user_id,
    duration_list,
    op: Operation
):
    query = op.value

    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            start = time.perf_counter()
            cursor.execute(query)
            result = cursor.fetchall()
            end = time.perf_counter()
    pool.putconn(conn)

    duration = (end - start) * 1000
    duration_list[user_id] = duration

def time_update(
    pool: ThreadedConnectionPool,
    user_id,
    duration_list,
    op: Operation
):
    query = op.value
    change = resolve_change(op)

    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            start = time.perf_counter()
            cursor.execute(query, (change, user_id))
            end = time.perf_counter()
    pool.putconn(conn)

    duration = (end - start) * 1000
    duration_list[user_id] = duration

def time_delete(pool: ThreadedConnectionPool, user_id, duration_list, op: Operation):
    query = op.value

    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            start = time.perf_counter()
            cursor.execute(query)
            end = time.perf_counter()
    pool.putconn(conn)

    duration = (end - start) * 1000
    duration_list[user_id] = duration

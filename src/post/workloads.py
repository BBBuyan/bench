import json
from random import randint, random
from time import perf_counter
from psycopg2.extras import execute_values
from psycopg2.pool import ThreadedConnectionPool
from operations import Operation
from helpers import generate_device_mock, delete_inserted_mocks

number_of_operations = 50

# 90% Read, 10 % Update
def run_read_heavy(pool: ThreadedConnectionPool):
    print(f"---{'READ HEAVY':<20}: ", end="", flush=True)
    conn = pool.getconn()
    total_duration = 0.0
    device = 1

    with conn.cursor() as cursor:
        for _ in range(number_of_operations):
            prob = random()
            new_vol = json.dumps(randint(0, 9999))
            start = 0

            if prob < 0.9:
                start = perf_counter()
                cursor.execute(Operation.READ.value, (device,))
                cursor.fetchall()
            else:
                start = perf_counter()
                cursor.execute(Operation.UPDATE.value, (new_vol, device))
                conn.commit()

            end = perf_counter()
            total_duration += (end - start)

    print(f"{total_duration * 1000:>10.0f} ms")
    pool.putconn(conn)

# 50% group and order, 50% calculate avg
def run_analytic(pool: ThreadedConnectionPool):
    print(f"---{'ANALYTIC':<20}: ", end="", flush=True)
    conn = pool.getconn()
    total_duration = 0.0
    with conn.cursor() as cursor:
        for _ in range(number_of_operations):
            prob = random()
            start = 0
            if(prob < 0.5):
                start = perf_counter()
                cursor.execute(Operation.AVG.value)
            else:
                start = perf_counter()
                cursor.execute(Operation.GROUP.value)

            result = cursor.fetchall()
            end = perf_counter()
            total_duration += end - start

    print(f"{total_duration * 1000:>10.0f} ms")
    pool.putconn(conn)

# 50% read, 50% update
def run_update_heavy(pool: ThreadedConnectionPool):
    print(f"---{'UPDATE HEAVY':<20}: ", end="", flush=True)
    conn = pool.getconn()
    total_duration = 0.0
    device = 1

    with conn.cursor() as cursor:
        for _ in range(number_of_operations):
            prob = random()
            new_vol = json.dumps(randint(0, 9999))
            start = 0

            if prob < 0.5:
                start = perf_counter()
                cursor.execute(Operation.READ.value, (device,))
                cursor.fetchall()
            else:
                start = perf_counter()
                cursor.execute(Operation.UPDATE.value, (new_vol, device))
                conn.commit()
            end = perf_counter()
            total_duration += (end - start)

    print(f"{total_duration * 1000:>10.0f} ms")
    pool.putconn(conn)

# 50% read 50% insert
def run_insert_heavy(pool: ThreadedConnectionPool):
    print(f"---{'INSERT HEAVY':<20}: ", end="", flush=True)
    conn = pool.getconn()
    total_duration = 0.0
    device = 1

    with conn.cursor() as cursor:
        for _ in range(number_of_operations):
            prob = random()
            new_obj = generate_device_mock(device, 100)
            start = 0

            if prob < 0.5:
                start = perf_counter()
                cursor.execute(Operation.READ.value, (device,))
                cursor.fetchall()
            else:
                start = perf_counter()
                execute_values(cursor, Operation.INSERT.value, new_obj)
                conn.commit()
            end = perf_counter()
            total_duration += (end - start)

    delete_inserted_mocks(pool)

    print(f"{total_duration * 1000:>10.0f} ms")
    pool.putconn(conn)

# 40% read, 30% insert, 30% update
def run_mixed(pool: ThreadedConnectionPool):
    print(f"---{'MIXED':<20}: ", end="", flush=True)
    conn = pool.getconn()
    total_duration = 0.0
    device = 1

    with conn.cursor() as cursor:
        for _ in range(number_of_operations):
            prob = random()
            new_obj = generate_device_mock(device, 100)
            new_vol = json.dumps(randint(0, 9999))
            start = 0

            if prob < 0.4:
                start = perf_counter()
                cursor.execute(Operation.READ.value, (device,))
                cursor.fetchall()
            elif prob < 0.7:
                start = perf_counter()
                execute_values(cursor, Operation.INSERT.value, new_obj)
                conn.commit()
            else:
                start = perf_counter()
                cursor.execute(Operation.UPDATE.value, (new_vol, device))
                conn.commit()
            end = perf_counter()
            total_duration += (end - start)

    delete_inserted_mocks(pool)
    print(f"{total_duration * 1000:>10.0f} ms")
    pool.putconn(conn)


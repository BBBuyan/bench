from psycopg2.extras import Json, execute_batch
from psycopg2.pool import ThreadedConnectionPool
from json import loads
from random import randint

def createIndexes(pool: ThreadedConnectionPool):
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("create index if not exists idx_device on flat (((data ->> 'device')::int))")
    pool.putconn(conn)

def dropIndexes(pool: ThreadedConnectionPool):
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("drop index if exists idx_device")

    pool.putconn(conn)

def import_data(pool: ThreadedConnectionPool):
    print("---IMPORT BEGIN:", end=" ", flush=True)
    conn = pool.getconn()
    cursor = conn.cursor()
    batch = []
    batch_size = 100000
    with open("../data/flat.json", "r") as f:
        for line in f:
            json_data = loads(line)
            batch.append((Json(json_data),))
            if len(batch) >= batch_size:
                print("100000", end=", ", flush=True)
                execute_batch(cursor, "insert into flat (data) values (%s)", batch)
                batch.clear()

    if batch:
        execute_batch(cursor, "insert into flat (data) values (%s)", batch)

    conn.commit()
    cursor.close()
    pool.putconn(conn)
    print("IMPORT END---")

def deleteData(pool: ThreadedConnectionPool):
    print("---DELETE BEGIN: ", end="", flush=True)
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("delete from flat")

    pool.putconn(conn)
    print("END---")

def generate_batch(size):
    data = []
    offset = randint(0, 100000)
    with open("../data/flat.json") as f:
        lines = f.readlines()
        lines = lines[offset: offset + size]
        for l in lines:
            json_data = loads(l)
            json_data['application']="deepbench"
            data.append((Json(json_data),))
    return data

def delete_insert_data(pool: ThreadedConnectionPool):
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            query = "delete from flat where (data->>'application') = 'deepbench'"
            cursor.execute(query)
    conn.commit()
    print(cursor.rowcount)
    cursor.close()
    pool.putconn(conn)

# UPDATE HELPERS
def generate_device_mock(user_id):
    size = 10000
    data = []
    offset = randint(0, 100000)
    with open("../data/flat.json") as f:
        lines = f.readlines()
        lines = lines[offset: offset + size]
        for l in lines:
            json_data = loads(l)
            json_data['device']=user_id
            json_data['volume_total_bytes']= 999
            json_data['application']="updateMock"
            data.append((Json(json_data),))
    return data

def generate_sub_mock(user_id):
    size = 10000
    data = []
    offset = randint(0, 100000)
    with open("../data/flat.json") as f:
        lines = f.readlines()
        lines = lines[offset: offset + size]
        for l in lines:
            json_data = loads(l)
            json_data['device']=999
            json_data['volume_total_bytes']= user_id
            json_data['application']="updateMock"
            data.append((Json(json_data),))
    return data

def insert_update_mocks(pool: ThreadedConnectionPool):
    print("inserting mocks,", end=" ", flush=True)
    conn = pool.getconn()

    with conn:
        with conn.cursor() as cursor:
            for i in range(4):
                device_mocks = generate_device_mock(i)
                sub_mocks = generate_sub_mock(i)
                execute_batch(cursor, "insert into flat (data) values (%s)", device_mocks)
                execute_batch(cursor, "insert into flat (data) values (%s)", sub_mocks)

    pool.putconn(conn)

def delete_overlapping_data(pool: ThreadedConnectionPool):
    print("delete overlapping", end=" ", flush=True)
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            query = "delete from flat where ((data->>'device')::int < 5) or ((data->>'volume_total_bytes')::int < 5)"
            cursor.execute(query)
    print(f"{cursor.rowcount},", end=" ", flush=True)
    pool.putconn(conn)

def prepare_update_test(pool: ThreadedConnectionPool):
    print("---preparing update: ", end=" ", flush=True)
    delete_overlapping_data(pool)
    insert_update_mocks(pool)
    print("done---")

def delete_update_mocks(pool: ThreadedConnectionPool):
    print("deleting mocks,", end=" ", flush=True)
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            query = "delete from flat where (((data)->>'application') = 'updateMock') or (((data)->>'application') = 'updatedObject')"
            cursor.execute(query)
    pool.putconn(conn)

def refresh_update(pool: ThreadedConnectionPool):
    print("---refreshing:", end=" ", flush=True)
    delete_update_mocks(pool)
    insert_update_mocks(pool)
    print("done---")

def showIndexes(pool: ThreadedConnectionPool):
    query ="SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'flat'" 
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            print(cursor.fetchall())
    pool.putconn(conn)


def calculate_diffs(old, new, user_list):
    for u in range(len(user_list)):
        print(f"| {user_list[u]} ", end="")
        o_val = old[u]
        n_val = new[u]
        diff = ((n_val - o_val) / o_val) * 100
        print(f"| {o_val:10.0f}| {n_val:10.0f}| {diff:10.1f} |")

# Delete HELPERS
def insert_delete_mocks(pool: ThreadedConnectionPool):
    print("inserting mocks,", end=" ", flush=True)
    conn = pool.getconn()

    with conn:
        with conn.cursor() as cursor:
            for i in range(4):
                device_mocks = generate_device_mock(i)
                execute_batch(cursor, "insert into flat (data) values (%s)", device_mocks)
    print("done")
    pool.putconn(conn)

# EXPLAIN SELECT * FROM flat WHERE (data->>'device')::int > 9000;
# EXPLAIN ANALYZE SELECT * FROM flat WHERE (data->>'device')::int > 9000;

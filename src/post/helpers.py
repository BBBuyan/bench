from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import Json, execute_batch
from random import randint
from json import dumps, loads

def delete_overlapping_data(pool: ThreadedConnectionPool):
    print("delete overlapping", end=" ", flush=True)
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            query = "delete from flat where ((data->>'device')::int < 4)"
            cursor.execute(query)

    print(f"{cursor.rowcount},", end=" ", flush=True)
    pool.putconn(conn)


def reassign_overlapping(pool: ThreadedConnectionPool):
    conn = pool.getconn()
    with conn.cursor() as cursor:
        reassign_query = """
        update flat
        set data = jsonb_set(data, '{old_device}', to_jsonb((data->>'device')))
        where ((data->>'device')::int < 4) and not (data ? 'old_device')
        """
        cursor.execute(reassign_query)
        cursor.execute("update flat set data = jsonb_set(data, '{device}', %s, false) where ((data->>'device')::int < 4)", (dumps(randint(0,9999)), ))

    conn.commit()
    pool.putconn(conn)


def insert_update_mocks(pool: ThreadedConnectionPool):
    insert_mock_size = 100 
    print("inserting mocks,", end=" ", flush=True)
    conn = pool.getconn()

    with conn:
        with conn.cursor() as cursor:
            for i in range(4):
                device_mocks = generate_device_mock(i, insert_mock_size)
                execute_batch(cursor, "insert into flat (data) values (%s)", device_mocks)

    pool.putconn(conn)

def update_is_prepared(pool: ThreadedConnectionPool)->bool:
    conn = pool.getconn()
    is_prepared: bool = False
    
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("select data from flat where data ? 'old_device' limit 3")
            fetch = cursor.fetchall()
            is_prepared = len(fetch) > 0

    pool.putconn(conn)
    return is_prepared

def prepare_update(pool: ThreadedConnectionPool):
    if update_is_prepared(pool):
        return

    print("---prepare_update", end=" ", flush=True)
    reassign_overlapping(pool)
    insert_update_mocks(pool)
    print("ended---")

def generate_device_mock(user_id, size):
    data = []
    offset = randint(0, 100000 - size)
    with open("../data/flat.json") as f:
        lines = f.readlines()
        lines = lines[offset: offset + size]
        for l in lines:
            json_data = loads(l)
            json_data['device']=user_id
            json_data['application']="generatedMock"
            data.append((Json(json_data),))
    return data

def delete_inserted_mocks(pool: ThreadedConnectionPool):
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            query = "delete from flat where (((data)->>'application') = 'generatedMock')"
            cursor.execute(query)
    pool.putconn(conn)

def import_all_data(pool: ThreadedConnectionPool):
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

def delete_all_data(pool: ThreadedConnectionPool):
    print("---DELETE BEGIN: ", end="", flush=True)
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("delete from flat")

    pool.putconn(conn)
    print("END---")

def create_indexes(pool: ThreadedConnectionPool):
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("create index if not exists idx_device on flat (((data ->> 'device')::int))")
    pool.putconn(conn)

def drop_indexes(pool: ThreadedConnectionPool):
    conn = pool.getconn()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("drop index if exists idx_device")

    pool.putconn(conn)

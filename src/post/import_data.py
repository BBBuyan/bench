from json import loads
from src.base_types import Base, Arr
from src.post.conn import pool 
from psycopg2.extras import Json, execute_batch
from src import all_types, flat_types, obj_types, arr_types
from pathlib import Path

def get_batch_limit(type: Base)->int:
    if isinstance(type, Arr):
        return 500
    else:
        return 5_000

def get_log_limit(type: Base)->int:
    if isinstance(type, Arr):
        return 1_000
    else:
        return 100_000

def import_data(type: Base):
    print(f"---IMPORT {type.name}", end=" ", flush=True)
    file_path = Path(__file__).parent.parent.parent/"data"/f"{type.name}.json"
    batch_limit = get_batch_limit(type)
    log_limit = get_log_limit(type)
    batch = []
    i = 0

    conn = pool.getconn()
    cursor = conn.cursor()

    with open(file_path, "r") as f:
        for line in f:
            json_data = loads(line)
            batch.append((Json(json_data),))
            if len(batch) >= batch_limit:
                execute_batch(cursor, f"insert into {type.name} (data) values (%s)", batch)
                batch.clear()

                i += batch_limit
                if i % log_limit == 0:
                    print(f"{i:,}")
    if batch:
        execute_batch(cursor, f"insert into {type.name} (data) values (%s)", batch)

    conn.commit()
    cursor.close()
    pool.putconn(conn)
    print("IMPORT END---")

if __name__ == "__main__":
    for i in all_types:
        import_data(i)

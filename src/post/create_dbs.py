from src import all_types, flat_types, obj_types, arr_types
from src.base_types import Base
from src.post.conn import pool

def create_db(type: Base):
    print(f"---CREATE {type.name}:", end=" ", flush=True)
    conn = pool.getconn()
    cursor = conn.cursor()

    cursor.execute(f"CREATE TABLE {type.name} (id SERIAL PRIMARY KEY, data JSONB NOT NULL);")

    conn.commit()
    cursor.close()
    pool.putconn(conn)
    print("DONE---")

if __name__ == "__main__":
    for i in all_types:
        create_db(i)


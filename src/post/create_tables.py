from src.post.conn import pool
from src.post.post_types import BasePost
from src.post.tables import flat_tables, arr_tables, all_tables, obj_tables

def create_table(type: BasePost):
    print(f"---CREATE {type.name}:", end=" ", flush=True)
    conn = pool.getconn()
    cursor = conn.cursor()

    cursor.execute(f"CREATE TABLE {type.name} (id SERIAL PRIMARY KEY, data JSONB NOT NULL);")

    conn.commit()
    cursor.close()
    pool.putconn(conn)
    print("DONE---")

if __name__ == "__main__":
    for i in all_tables:
        create_table(i)

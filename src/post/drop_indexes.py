from src.post.conn import pool
from src.post.post_types import BasePost
from src.post.tables import flat_tables, arr_tables, all_tables, obj_tables
from src.post import indexes

def drop_index(table: BasePost):
    print(f"---INDEX {table.name}:", end=" ", flush=True)
    conn = pool.getconn()

    with conn.cursor() as cursor:
        cursor.execute(f"{table.index_drop}")

    conn.commit()
    pool.putconn(conn)
    print("DONE---")

if __name__ == "__main__":
    for i in all_tables:
        drop_index(i)


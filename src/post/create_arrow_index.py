from src.post.conn import pool
from src.post.post_types import BasePost
from src.post.tables import flat_arrows, obj_arrows, arrow_tables

def create_arrow_index(table: BasePost):
    print(f"---ARROW INDEX {table.name}:", end=" ", flush=True)
    conn = pool.getconn()

    with conn.cursor() as cursor:
        cursor.execute(f"{table.index}")

    conn.commit()
    pool.putconn(conn)
    print("DONE---")

if __name__ == "__main__":
    for i in arrow_tables:
        create_arrow_index(i)

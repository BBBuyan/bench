from src.post.conn import pool
from src.base_types import Base

def time_read(type: Base):
    query = ""

    conn = pool.getconn()
    with conn.cursor() as cursor:
        cursor.execute()
        pass

    conn.commit()
    pool.putconn(conn)

def time_update(type: Base):
    conn = pool.getconn()
    cursor = conn.cursor()


    conn.commit()
    cursor.close()
    pool.putconn(conn)

def time_insert(type: Base):
    conn = pool.getconn()
    cursor = conn.cursor()


    conn.commit()
    cursor.close()
    pool.putconn(conn)

def time_avg(type: Base):
    conn = pool.getconn()
    cursor = conn.cursor()


    conn.commit()
    cursor.close()
    pool.putconn(conn)

def time_sort(type: Base):
    conn = pool.getconn()
    cursor = conn.cursor()


    conn.commit()
    cursor.close()
    pool.putconn(conn)

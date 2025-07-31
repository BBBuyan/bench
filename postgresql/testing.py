from psycopg2.pool import ThreadedConnectionPool
from benchmarking import reset_database


pool = ThreadedConnectionPool( 1 ,4 , database="postdeep" , host="localhost" , user="user" , password="mypass",)

reset_database(pool)

pool.closeall()

from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv
from os import getenv

load_dotenv()
ip = getenv("POST_IP")

pool = SimpleConnectionPool( 
    1 
    ,4 
    , database="deep" 
    , host=ip 
    , port="5432"
    , user="user"
    , password="mypass"
)

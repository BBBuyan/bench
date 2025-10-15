from psycopg2.pool import ThreadedConnectionPool

pool = ThreadedConnectionPool( 
    1 
    ,4 
    , database="deep" 
    , host="192.168.2.87" 
    , port="5432"
    , user="user"
    , password="mypass",)


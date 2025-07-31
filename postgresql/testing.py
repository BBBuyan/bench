from psycopg2.pool import ThreadedConnectionPool
from operations import Operation
import workloads as wls
import helpers as hs
from mongodb.bench import sayhello
import pprint


# pool = ThreadedConnectionPool( 
#     1 
#     ,4 
#     , database="postdeep" 
#     , host="192.168.2.87" 
#     , port="5432"
#     , user="user"
#     , password="mypass",)
#
#
# wls.run_analytic(pool)
#
# pool.closeall()
#

def test(op: Operation):
    op.INSERT.value

sayhello()


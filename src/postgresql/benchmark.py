from psycopg2.pool import ThreadedConnectionPool
import workloads as workload
import helpers as hs

def start():
    pool = ThreadedConnectionPool( 
        1 
        ,4 
        , database="postdeep" 
        , host="192.168.2.87" 
        , port="5432"
        , user="user"
        , password="mypass",)

    hs.prepare_update(pool)

    workload.run_read_heavy(pool)
    workload.run_analytic(pool)
    workload.run_update_heavy(pool)
    workload.run_insert_heavy(pool)
    workload.run_mixed(pool)

    hs.create_indexes(pool)

    workload.run_read_heavy(pool)
    workload.run_analytic(pool)
    workload.run_update_heavy(pool)
    workload.run_insert_heavy(pool)
    workload.run_mixed(pool)

    hs.drop_indexes(pool)
    pool.closeall()

if __name__ == "__main__":
    start()


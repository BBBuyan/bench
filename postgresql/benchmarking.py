from db_ops import Operation, resolve_operation, time_insert
from resources import calculate_diffs, createIndexes, delete_insert_data, delete_update_mocks, deleteData, dropIndexes, import_data, insert_delete_mocks, prepare_update_test, refresh_update
from psycopg2.pool import ThreadedConnectionPool
from threading import Thread

user_list = [1, 2, 4]

def execute_with_threads(pool: ThreadedConnectionPool, num_of_users: int, op: Operation):
    threads_list = []
    duration_list: list[float] = [0.0] * num_of_users
    target_op = resolve_operation(op)
    
    for user_id in range(num_of_users):
        t = Thread(
            target=target_op
            , args=(pool, user_id, duration_list, op)
        )
        t.start()
        threads_list.append(t)

    for t in threads_list:
        t.join()

    result = sum(duration_list) / len(duration_list)
    return result

def simulate_users(op: Operation, pool: ThreadedConnectionPool):
    u_len = len(user_list)
    result = [0.0 for _ in range(u_len)]
    
    print(f"user: ", end=" ", flush=True)
    for u in range(u_len):
        result[u] = execute_with_threads(pool, user_list[u], op)
        print(f"{user_list[u]}", end=", ", flush=True)
    print("")

    return result

def bench_insert(pool: ThreadedConnectionPool):

    without_index = simulate_users(Operation.INSERT, pool)
    createIndexes(pool)

    with_index = simulate_users(Operation.INSERT, pool)
    dropIndexes(pool)

    delete_insert_data(pool)
    print("INSERT")
    calculate_diffs(without_index, with_index, user_list)

def bench_reads(pool: ThreadedConnectionPool):
    without_index_avg = simulate_users(Operation.AVG, pool)
    without_index_group = simulate_users(Operation.GROUP, pool)
    createIndexes(pool)

    with_index_avg =simulate_users(Operation.AVG, pool)
    with_index_group =simulate_users(Operation.GROUP, pool)
    dropIndexes(pool)

    print("AVG")
    calculate_diffs(without_index_avg, with_index_avg, user_list)
    print("GROUP")
    calculate_diffs(without_index_group, with_index_group, user_list)

def bench_updates(pool: ThreadedConnectionPool):
    prepare_update_test(pool)

    without_index = simulate_users(Operation.WHERE_NON_INDEX_UPDATE_NON_INDEX, pool)
    refresh_update(pool)
    createIndexes(pool)

    where_non_index_update_index = simulate_users(Operation.WHERE_NON_INDEX_UPDATE_INDEX, pool)
    refresh_update(pool)

    where_index_update_index = simulate_users(Operation.WHERE_INDEX_UPDATE_INDEX, pool)
    refresh_update(pool)

    where_index_update_non_index = simulate_users(Operation.WHERE_INDEX_UPDATE_NON_INDEX, pool)

    dropIndexes(pool)
    delete_update_mocks(pool)

    print("WHERE INDEX UPDATE INDEX")
    calculate_diffs(without_index, where_index_update_index, user_list)
    print("WHERE INDEX UPDATE NON INDEX")
    calculate_diffs(without_index, where_index_update_non_index, user_list)
    print("WHERE NON INDEX UPDATE INDEX")
    calculate_diffs(without_index, where_non_index_update_index, user_list)

def bench_delete(pool: ThreadedConnectionPool):
    reset_database(pool)

    without_index = simulate_users(Operation.DELETE, pool)

    reset_database(pool)
    createIndexes(pool)

    with_index = simulate_users(Operation.DELETE, pool)
    dropIndexes(pool)
    calculate_diffs(without_index, with_index, user_list)

def reset_database(pool: ThreadedConnectionPool):
    deleteData(pool)
    import_data(pool)

def main():
    pool = ThreadedConnectionPool( 1 ,4 , database="postdeep" , host="localhost" , user="user" , password="mypass",)

    # deleteData(pool)
    # import_data(pool)

    # bench_reads(pool)
    # bench_insert(pool)
    # bench_updates(pool)
    # bench_delete(pool)

    dropIndexes(pool)
    reset_database(pool)
    pool.closeall()

if __name__ == "__main__":
    main()

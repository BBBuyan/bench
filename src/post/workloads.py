from src.post import post_op as op
from src.post.post_types import BasePost
from src.post import post_logger as log

num_of_ops = 10

def run_read(tables: list[BasePost]):
    print(f"---READ", end=" ", flush=True)
    result = [0.0] * len(tables)

    for i in range(len(tables)):
        type_results = []
        print(f"{tables[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("r, ", end="", flush=True)
            tmp = op.time_read(tables[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    log.save_result(result, "READ", tables[0].coll_type)

def run_avg(tables: list[BasePost]):
    print(f"---AVG", end=" ", flush=True)
    result = [0.0] * len(tables)

    for i in range(len(tables)):
        type_results = []
        print(f"{tables[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("r, ", end="", flush=True)
            tmp = op.time_avg(tables[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    log.save_result(result, "AVG", tables[0].coll_type)

def run_sort(tables: list[BasePost]):
    print(f"---SORT", end=" ", flush=True)
    result = [0.0] * len(tables)

    for i in range(len(tables)):
        type_results = []
        print(f"{tables[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("r, ", end="", flush=True)
            tmp = op.time_sort(tables[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)
    log.save_result(result, "SORT", tables[0].coll_type)


def run_update(tables: list[BasePost]):
    print(f"---SORT", end=" ", flush=True)
    result = [0.0] * len(tables)

    for i in range(len(tables)):
        type_results = []
        print(f"{tables[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("r, ", end="", flush=True)
            tmp = op.time_update(tables[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)
    log.save_result(result, "UPDATE", tables[0].coll_type)

def run_insert(tables: list[BasePost]):
    print(f"---INSERT", end=" ", flush=True)
    result = [0.0] * len(tables)

    for i in range(len(tables)):
        type_results = []
        print(f"{tables[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("r, ", end="", flush=True)
            tmp = op.time_insert(tables[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)
        
    log.save_result(result, "INSERT", tables[0].coll_type)

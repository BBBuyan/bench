from src.post import post_op as op
from src.post.post_types import BasePost
from src.post import post_logger as log
from typing import Callable

num_of_ops = 10

def execute(
    tables: list[BasePost]
    , op: Callable[[BasePost], float]
    , opType: str
):
    print(f"---{opType}---")
    result = [0.0] * len(tables)
    for i in range(len(tables)):
        type_results = []
        print(f"{tables[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            tmp = op(tables[i])
            type_results.append(tmp)
            print(f"{tmp:>6.1f}, ", end="", flush=True)

        result[i] = sum(type_results)/len(type_results)
        print(f" [{result[i]:.0f}] ---")

    log.save_result(result, opType, tables[0].coll_type)

def run_read(tables: list[BasePost]):
    execute(tables, op.time_read, "READ")

def run_avg(tables: list[BasePost]):
    execute(tables, op.time_avg, "AVG")

def run_sort(tables: list[BasePost]):
    execute(tables, op.time_sort, "SORT")

def run_update(tables: list[BasePost]):
    execute(tables, op.time_update, "UPDATE")

def run_insert(tables: list[BasePost]):
    execute(tables, op.time_insert, "INSERT")

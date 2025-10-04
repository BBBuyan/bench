from src.couch.db_types.Base import Base
from random import random
from src.couch import logger
from src.couch import operations as op

num_of_tries = 10

def run_avg_only(types: list[Base]):
    print("---AVG Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)

        type_results = []
        for _ in range(num_of_tries):
            print("a,", end=" ", flush=True)
            type_results.append(op.time_avg(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "avg only", types[0].coll_type)
    return result

def run_group_only(types: list[Base]):
    print("---Group Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)

        type_results = []
        for _ in range(num_of_tries):
            print("g,", end=" ", flush=True)
            type_results.append(op.time_group(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "group only", types[0].coll_type)
    return result

def run_avg_after_update(types: list[Base]):
    print("---AVG after update---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)

        type_results = []
        for _ in range(num_of_tries):
            print("u,", end=" ", flush=True)
            op.time_update(types[i])
            type_results.append(op.time_avg(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "avg after update", types[0].coll_type)
    return result


def run_group_after_update(types: list[Base]):
    print("---Group after update---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)

        type_results = []
        for _ in range(num_of_tries):
            print("u,", end=" ", flush=True)
            op.time_update(types[i])
            type_results.append(op.time_group(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "group after update", types[0].coll_type)
    return result

def run_avg_after_insert(types: list[Base]):
    print("---AVG after Insert---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)
        
        type_results = []
        for _ in range(num_of_tries):
            print("i,", end=" ", flush=True)
            op.time_insert(types[i])
            type_results.append(op.time_avg(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "avg after insert", types[0].coll_type)
    return result

def run_group_after_insert(types: list[Base]):
    print("---Group after Insert---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)

        type_results = []
        for _ in range(num_of_tries):
            print("i,", end=" ", flush=True)
            op.time_insert(types[i])
            type_results.append(op.time_group(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "group after insert", types[0].coll_type)
    return result

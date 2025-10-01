from random import random
from . import warmup
from . import mongo_operations as op
from .mongo_types import BaseMongo

num_of_ops = 10

def run_read_only(types: list[BaseMongo]):
    print(f"---READ ONLY", end=" ", flush=True)
    result = [0.0] * len(types)

    for i in range(len(types)):
        #warmup
        warmup.read_warmup(types[i])

        type_results = []
        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("r, ", end="", flush=True)
            tmp = op.time_read(types[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])

        result[i] = sum(type_results)/len(type_results)
    return result

def run_read_only_by_shard_key(types: list[BaseMongo]):
    print(f"---READ ONLY BY SHARD KEY", end=" ", flush=True)
    result = [0.0] * len(types)

    for i in range(len(types)):
        #warmup
        warmup.read_by_shard_key(types[i])

        type_results = []
        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("r, ", end="", flush=True)
            tmp = op.time_read_by_shard_key(types[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])

        result[i] = sum(type_results)/len(type_results)

    return result

def run_update_non_indexed_field(types: list[BaseMongo]):
    print("---UPDATE NON INDEXED FIELD", end=" ", flush=True)
    result = [0.0] * len(types)

    for i in range(len(types)):
        warmup.update_non_indexed_field(types[i])
        type_results = []

        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("u, ", end="" , flush=True)
            tmp = op.time_update_storage(types[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])

        result[i] = sum(type_results)/len(type_results)

    return result

def run_update_indexed_field(types: list[BaseMongo]):
    print("---UPDATE INDEXED FIELD", end=" ", flush=True)
    result = [0.0] * len(types)

    for i in range(len(types)):
        warmup.update_indexed_field(types[i])
        type_results = []
        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("u, ", end="" , flush=True)
            tmp = op.time_update_error_count(types[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])

        result[i] = sum(type_results)/len(type_results)

    return result

def run_update_by_shard_key(types: list[BaseMongo]):
    print("---UPDATE BY SHARD KEY", end=" ", flush=True)
    result = [0.0] * len(types)

    for i in range(len(types)):
        warmup.update_by_shard_key(types[i])
        type_results = []
        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("u, ", end="" , flush=True)
            tmp = op.time_update_by_shard_key(types[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])

        result[i] = sum(type_results)/len(type_results)

    return result

def run_insert_only(types: list[BaseMongo]):
    print("---INSERT ONLY", end=" ", flush=True)
    result = [0.0] * len(types)
    for i in range(len(types)):
        warmup.insert_warmup(types[i])
        print(f"{types[i].name}")
        result[i] = op.time_insert(types[i])
    print("---DONE---")
    return result

def run_avg(types: list[BaseMongo]):
    print("---AVERAGE---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        type_results = []

        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(3):
            print("a, ", end="", flush=True)
            tmp = op.time_avg(types[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])

        result[i] = sum(type_results)/len(type_results)
    return result

def run_group(types: list[BaseMongo]):
    print("---GROUP---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        type_results = []

        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(3):
            print("g, ", end="", flush=True)
            tmp = op.time_group(types[i])
            type_results.append(tmp)
        print("---")

        print([f"{x:.1f}" for x in type_results])

        result[i] = sum(type_results)/len(type_results)

    return result

# 40% read 30% update 30% insert
# def run_mixed(types: list[BaseMongo]):
#     print("---MIXED---")
#     result = [0.0] * len(types)
#     for i in range(len(types)):
#         op.time_read(types[i])
#
#         print(f"{types[i].name} | ", end=" ", flush=True)
#         for _ in range(num_of_ops):
#             prob = random()
#             if prob<0.4:
#                 print("r, ", end="", flush=True)
#                 result[i] += op.time_read(types[i])
#             elif prob <0.7:
#                 print("u, ", end="" , flush=True)
#                 result[i] = op.time_update(types[i])
#             else:
#                 print("i, ", end="" , flush=True)
#                 result[i] += op.time_insert(types[i])
#         print("---")
#
#     return result


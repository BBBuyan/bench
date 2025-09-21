from random import random
from . import mongo_operations as op
from .mongo_types import BaseMongo

num_of_ops = 10

# 90% Read, 10 % Update
def run_read_heavy(types: list[BaseMongo]):
    print(f"---{'READ HEAVY'}---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            prob = random()
            if prob<0.9:
                print("r, ", end="", flush=True)
                result[i] += op.time_read(types[i])
            else:
                print("u, ", end="" , flush=True)
                result[i] += op.time_update(types[i])
        print("---")

    return result

def run_avg(types: list[BaseMongo]):
    print("---AVERAGE---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(3):
            print("a, ", end="", flush=True)
            result[i] += op.time_avg(types[i])
        print("---")
    return result

def run_group(types: list[BaseMongo]):
    print("---GROUP---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(3):
            print("g, ", end="", flush=True)
            result[i] += op.time_group(types[i])
        print("---")

    return result

# 10% read, 90% update
def run_update_heavy(types: list[BaseMongo]):
    print("---UPDATE HEAVY---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            prob = random()
            if prob<0.1:
                print("r, ", end="", flush=True)
                result[i] += op.time_read(types[i])
            else:
                print("u, ", end="" , flush=True)
                result[i] += op.time_update(types[i])
        print("---")

    return result

# 10% read 90% insert
def run_insert_heavy(types: list[BaseMongo]):
    print("---INSERT HEAVY---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)

        for _ in range(num_of_ops):
            prob = random()
            if prob<0.1:
                print("r, ", end="", flush=True)
                result[i] += op.time_read(types[i])
            else:
                print("i, ", end="" , flush=True)
                result[i] += op.time_insert(types[i])
        print("---")

    return result

# 40% read 30% update 30% insert
def run_mixed(types: list[BaseMongo]):
    print("---MIXED---")
    result = [0.0] * len(types)
    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)

        for _ in range(num_of_ops):
            prob = random()
            if prob<0.4:
                print("r, ", end="", flush=True)
                result[i] += op.time_read(types[i])
            elif prob <0.7:
                print("u, ", end="" , flush=True)
                result[i] = op.time_update(types[i])
            else:
                print("i, ", end="" , flush=True)
                result[i] += op.time_insert(types[i])
        print("---")

    return result

# 100% insert
def run_insert_only(types: list[BaseMongo]):
    print("---INSERT HEAVY---")
    result = [0.0] * len(types)
    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_ops):
            print("i, ", end="" , flush=True)
            result[i] += op.time_insert(types[i])
        print("---")

    return result

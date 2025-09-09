from coll_types.Base import Base
from random import random
import operations as op

num_of_ops = 10

def run_read_heavy(types: list[Base]):
    print(f"---{'READ HEAVY'}---")
    result = [0.0] * len(types)

    for depth in range(len(types)):
        print(f"{types[depth].name} | ", end="", flush=True)

        for _ in range(num_of_ops):
            prob = random()
            if prob<0.9:
                print("r, ", end="", flush=True)
                result[depth] += op.time_read(types[depth])
            else:
                print("u", end="", flush=True)
                result[depth] += op.time_update(types[depth])

    print("---")
    return result

def run_update_heavy(types: list[Base]):
    print(f"---{'UPDATE HEAVY'}---")
    result = [0.0] * len(types)

    for depth in range(len(types)):
        print(f"{types[depth].name} | ", end="", flush=True)

        for _ in range(num_of_ops):
            prob = random()
            if prob<0.1:
                print("r, ", end="", flush=True)
                result[depth] += op.time_read(types[depth])
            else:
                print("u, ", end="", flush=True)
                result[depth] += op.time_update(types[depth])

    print("---")
    return result

def run_update_only(types: list[Base]):
    print(f"---{'UPDATE ONLY'}---")
    result = [0.0] * len(types)

    for depth in range(len(types)):
        print(f"{types[depth].name} | ", end="", flush=True)

        for _ in range(num_of_ops):
            print("u, ", end="", flush=True)
            result[depth] += op.time_update(types[depth])

    print("---")
    return result

def run_insert_heavy(types: list[Base]):
    print(f"---{'INSERT HEAVY'}---")
    result = [0.0] * len(types)

    for depth in range(len(types)):
        print(f"{types[depth].name} | ", end="", flush=True)

        for _ in range(num_of_ops):
            prob = random()
            if prob<0.1:
                print("r, ", end="", flush=True)
                result[depth] += op.time_read(types[depth])
            else:
                print("i, ", end="", flush=True)
                result[depth] += op.time_insert(types[depth])
    print("---")
    return result

def run_insert_only(types: list[Base]):
    print(f"---{'INSERT ONLY'}---")
    result = [0.0] * len(types)

    for depth in range(len(types)):
        print(f"{types[depth].name} | ", end="", flush=True)

        for _ in range(num_of_ops):
            print("i, ", end="", flush=True)
            result[depth] += op.time_insert(types[depth])

    print("---")
    return result

def run_avg(types: list[Base]):
    print("---AVG---")
    result = [0.0]*len(types)

    for depth in range(len(types)):
        print(f"{types[depth].name} | ", end="", flush=True)
        for _ in range(3):
            print("a, ", end="", flush=True)
            result[depth] += op.time_avg(types[depth])
        print("---")
    return result

def run_group(types: list[Base]):
    print("---AVG---")
    result = [0.0]*len(types)

    for depth in range(len(types)):
        print(f"{types[depth].name} | ", end="", flush=True)
        for _ in range(3):
            print("g, ", end="", flush=True)
            result[depth] += op.time_group(types[depth])
        print("---")
    return result

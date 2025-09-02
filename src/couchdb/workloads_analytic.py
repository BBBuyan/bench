from Base import Base
from random import random
import operations as op

num_of_tries = 10

def run_avg_only(types: list[Base]):
    print("---AVG Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            print("a,", end=" ", flush=True)
            result[i] += op.time_avg(types[i])
        print("---")
    return result

def run_group_only(types: list[Base]):
    print("---Group Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            print("g,", end=" ", flush=True)
            result[i] += op.time_group(types[i])
        print("---")
    return result

def run_avg_after_update(types: list[Base]):
    print("---AVG after update---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            print("u,", end=" ", flush=True)
            op.time_update(types[i])
            result[i] += op.time_avg(types[i])
        print("---")
    return result


def run_group_after_update(types: list[Base]):
    print("---Group after update---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            print("u,", end=" ", flush=True)
            op.time_update(types[i])
            result[i] += op.time_group(types[i])
        print("---")
    return result

def run_avg_after_insert(types: list[Base]):
    print("---AVG after Insert---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            print("i,", end=" ", flush=True)
            op.time_insert(types[i])
            result[i] += op.time_avg(types[i])
        print("---")
    return result

def run_group_after_insert(types: list[Base]):
    print("---Group after Insert---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            print("i,", end=" ", flush=True)
            op.time_insert(types[i])
            result[i] += op.time_group(types[i])
        print("---")
    return result

def run_avg_mixed(types: list[Base]):
    print("---AVG mixed---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            prob = random()

            if prob < 0.4:
                print("a,", end=" ", flush=True)
                result[i] += op.time_avg(types[i])
            elif prob < 0.7:
                print("u,", end=" ", flush=True)
                op.time_update(types[i])
                result[i] += op.time_avg(types[i])
            else:
                print("i,", end=" ", flush=True)
                op.time_insert(types[i])
                result[i] += op.time_avg(types[i])

        print("---")

    return result

def run_group_mixed(types: list[Base]):
    print("---Group mixed---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            prob = random()

            if prob < 0.4:
                print("g,", end=" ", flush=True)
                result[i] += op.time_group(types[i])
            elif prob < 0.7:
                print("u,", end=" ", flush=True)
                op.time_update(types[i])
                result[i] += op.time_group(types[i])
            else:
                print("i,", end=" ", flush=True)
                op.time_insert(types[i])
                result[i] += op.time_group(types[i])

        print("---")

    return result

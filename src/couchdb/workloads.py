from random import random
import operations as op
from Base import Base

num_of_tries = 10

def run_read_heavy(types: list[Base]):
    print("---Read Heavy---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            prob = random()

            if prob < 0.9:
                print("r,", end=" ", flush=True)
                result[i] += op.time_read(types[i])
            else:
                pass
                print("u,", end=" ", flush=True)
                op.time_update(types[i])
        print("---")

    return result

def run_update_heavy(types: list[Base]):
    print("---Update Heavy---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            prob = random()

            if prob < 0.1:
                print("r,", end=" ", flush=True)
                result[i] += op.time_read(types[i])
            else:
                print("u,", end=" ", flush=True)
                result[i] += op.time_update(types[i])

        print("---")
    return result

def run_update_only(types: list[Base]):
    print("---Update Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            print("u,", end=" ", flush=True)
            result[i] += op.time_update(types[i])
        print("---")
    return result


def run_insert_heavy(types: list[Base]):
    print("---Insert Heavy---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            prob = random()
            if prob < 0.1:
                print("r,", end=" ", flush=True)
                result[i] += op.time_read(types[i])
            else:
                print("i,", end=" ", flush=True)
                result[i] += op.time_insert(types[i])
        print("---")

    return result

def run_insert_only(types: list[Base]):
    print("---Insert Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            print("i,", end=" ", flush=True)
            result[i] += op.time_insert(types[i])
        print("---")
    return result

def run_mixed(types: list[Base]):
    print("---Mixed---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        for _ in range(num_of_tries):
            prob = random()

            if prob < 0.4:
                print("r,", end=" ", flush=True)
                result[i] += op.time_read(types[i])
            elif prob < 0.7:
                print("u,", end=" ", flush=True)
                result[i] += op.time_update(types[i])
            else:
                print("i,", end=" ", flush=True)
                result[i] += op.time_insert(types[i])

        print("---")

    return result

def run_group(types: list[Base]):
    result = [0.0] * len(types)

    for i in range(len(types)):
        result[i] = op.time_group(types[i])

    print("---")
    return result

def run_avg(types: list[Base]):
    result = [0.0] * len(types)

    for i in range(len(types)):
        result[i] = op.time_avg(types[i])

    print("---")
    return result


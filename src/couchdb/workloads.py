from random import random
import operations as op
from op_types import Base

num_of_tries = 1

def run_read_heavy(types: list[Base]):
    result = [0.0] * len(types)

    for i in range(len(types)):
        for _ in range(num_of_tries):
            prob = random()

            if prob < 0.9:
                print("r,", end=" ", flush=True)
                result[i] = op.time_read(types[i])
            else:
                print("u,", end=" ", flush=True)
                op.time_update(types[i])

    return result

def run_update_heavy(types: list[Base]):
    result = [0.0] * len(types)

    for i in range(len(types)):
        for _ in range(num_of_tries):
            prob = random()

            if prob < 0.1:
                print("r,", end=" ", flush=True)
                result[i] = op.time_read(types[i])
            else:
                print("u,", end=" ", flush=True)
                result[i] = op.time_update(types[i])

    return result


def run_insert_heavy(types: list[Base]):
    result = [0.0] * len(types)

    for i in range(len(types)):
        for _ in range(num_of_tries):
            prob = random()

            if prob < 0.1:
                print("r,", end=" ", flush=True)
                result[i] = op.time_read(types[i])
            else:
                print("i,", end=" ", flush=True)
                result[i] = op.time_insert(types[i])
    return result

def run_group(types: list[Base]):
    result = [0.0] * len(types)
    for i in range(len(types)):
        prob = random()
        result[i] = op.time_group(types[i])


    return result

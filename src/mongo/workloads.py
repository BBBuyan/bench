from random import random
from coll_type import CollType
import helper
from paths import depth_list
import operations

num_of_ops = 1

# 90% Read, 10 % Update
def run_read_heavy(type: CollType):
    print(f"---{'READ HEAVY'}---")
    colls = helper.resolve_colls(type)
    result = [0.0] * len(colls)
    sub_id = 1

    for depth in range(len(colls)):
        print(f"depth: {depth_list[depth]}")

        for _ in range(num_of_ops):
            prob = random()
            if prob<0.9:
                print("r, ", end="", flush=True)
                result[depth] = operations.time_read(depth, sub_id, type, colls[depth])
            else:
                print("u, ", end="" , flush=True)
                result[depth] = operations.time_update(depth, sub_id, type, colls[depth])

        print("---")

    return result

def run_avg(type: CollType):
    print("---AVERAGE---")
    colls = helper.resolve_colls(type)
    result = [0.0] * len(colls)

    for depth in range(len(colls)):
        print(f"depth: {depth_list[depth]}")
        for _ in range(3):
            print("a, ", end="", flush=True)
            result[depth] += operations.time_avg(depth, type, colls[depth])
        print("---")

    return result

def run_group(type: CollType):
    print("---GROUP---")
    colls = helper.resolve_colls(type)
    result = [0.0] * len(colls)

    for depth in range(len(colls)):
        print(f"depth: {depth_list[depth]}")
        for _ in range(3):
            print("g, ", end="", flush=True)
            result[depth] += operations.time_group(depth, type, colls[depth])
        print("---")

    return result

# 40% read, 60% update
def run_update_heavy(type: CollType):
    print("---UPDATE HEAVY---")
    colls = helper.resolve_colls(type)
    result = [0.0] * len(colls)
    sub_id = 1

    for depth in range(len(colls)):
        print(f"depth: {depth_list[depth]}")
        for _ in range(num_of_ops):
            prob = random()

            if prob<0.4:
                print("r, ", end="", flush=True)
                result[depth] += operations.time_read(depth, sub_id, type, colls[depth])
            else:
                print("u, ", end="" , flush=True)
                result[depth] += operations.time_read(depth, sub_id, type, colls[depth])
        print("---")
    return result

# 40% read 60% insert
def run_insert_heavy(type: CollType):
    print("---INSERT HEAVY---")
    colls = helper.resolve_colls(type)
    result = [0.0] * len(colls)
    sub_id = 1

    for depth in range(len(colls)):
        print(f"depth: {depth_list[depth]}")
        for _ in range(num_of_ops):
            prob = random()
            if prob<0.6:
                print("r, ", end="", flush=True)
                result[depth] += operations.time_read(depth, sub_id, type, colls[depth])
            else:
                print("i, ", end="" , flush=True)
                result[depth] += operations.time_insert(colls[depth])
        print("---")

    helper.delete_inserted(type)
    return result

# 40% read 30% update 30% insert
def run_mixed(type: CollType):
    print("---MIXED---")
    colls = helper.resolve_colls(type)
    result = [0.0] * len(colls)
    sub_id = 1
    for depth in range(len(colls)):
        print(f"depth: {depth_list[depth]}")
        for _ in range(num_of_ops):
            prob = random()
            if prob<0.4:
                print("r, ", end="", flush=True)
                result[depth] += operations.time_read(depth, sub_id, type, colls[depth])
            elif prob <0.7:
                print("u, ", end="" , flush=True)
                result[depth] = operations.time_update(depth, sub_id, type, colls[depth])
            else:
                print("i, ", end="" , flush=True)
                result[depth] += operations.time_insert(colls[depth])
        print("---")

    helper.delete_inserted(type)
    return result

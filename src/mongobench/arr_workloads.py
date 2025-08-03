from random import random
from pymongo.collection import Collection
from pymongo.database import Database
import arr_operations as arr
from arr_helpers import delete_inserted

number_of_operations = 10

def run_read_heavy(db: Database):
    print(f"---{'READ HEAVY'}---")
    colls: list[Collection] = [db['arr1'], db['arr2'], db['arr4'], db['arr8']]
    result = [0.0] * len(colls)

    device_id = 1
    for depth in range(len(colls)):
        print(f"depth: {depth}")
        for _ in range(number_of_operations):
            prob = random()
            if prob<0.9:
                print("r, ", end="", flush=True)
                result[depth] += arr.time_read(colls[depth], depth, device_id)
            else:
                print("u, ", end="" , flush=True)
                result[depth] += arr.time_update(colls[depth], depth, device_id)
        print("---")

    return result

def run_analytic(db: Database):
    run_avg(db, 3)
    run_group(db, 3)


def run_avg(db: Database, op_count: int):
    print("---AVERAGE---")
    colls: list[Collection] = [db['arr1'], db['arr2'], db['arr4'], db['arr8']]
    result = [0.0] * len(colls)

    for depth in range(len(colls)):
        print(f"depth: {colls[depth].name}")
        for _ in range(op_count):
            print("a, ", end="", flush=True)
            result[depth] += arr.time_avg(colls[depth], depth)
        print("---")

    return result

def run_group(db: Database, op_count: int):
    print("---GROUP---")
    colls: list[Collection] = [db['arr1'], db['arr2'], db['arr4'], db['arr8']]
    result = [0.0] * len(colls)

    for depth in range(len(colls)):
        print(f"depth: {colls[depth].name}")
        for _ in range(op_count):
            print("g, ", end="", flush=True)
            result[depth] += arr.time_group(colls[depth], depth)
        print("---")

    return result

# 40% read, 60% update
def run_update_heavy(db: Database):
    print("---UPDATE HEAVY---")
    colls: list[Collection] = [db['arr1'], db['arr2'], db['arr4'], db['arr8']]
    result = [0.0] * len(colls)
    device_id = 1
    for depth in range(len(colls)):
        print(f"depth: {depth}")
        for _ in range(number_of_operations):
            prob = random()
            if prob<0.4:
                print("r, ", end="", flush=True)
                result[depth] += arr.time_read(colls[depth], depth, device_id)
            else:
                print("u, ", end="" , flush=True)
                result[depth] += arr.time_update(colls[depth], depth, device_id)
        print("---")
    return result

# 40% read 60% insert
def run_insert_heavy(db: Database):
    print("---INSERT HEAVY---")
    colls: list[Collection] = [db['arr1'], db['arr2'], db['arr4'], db['arr8']]
    result = [0.0] * len(colls)
    device_id = 1
    for depth in range(len(colls)):
        print(f"depth: {depth}")
        for _ in range(number_of_operations):
            prob = random()
            if prob<0.6:
                print("r, ", end="", flush=True)
                result[depth] += arr.time_read(colls[depth], depth, device_id)
            else:
                print("i, ", end="" , flush=True)
                result[depth] += arr.time_insert(colls[depth])
        print("---")
    delete_inserted(db)
    return result

# 40% read 30% update 30% insert
def run_mixed(db: Database):
    print("---MIXED---")
    colls: list[Collection] = [db['arr1'], db['arr2'], db['arr4'], db['arr8']]
    result = [0.0] * len(colls)
    device_id = 1
    for depth in range(len(colls)):
        print(f"depth: {depth}")
        for _ in range(number_of_operations):
            prob = random()
            if prob<0.4:
                print("r, ", end="", flush=True)
                result[depth] += arr.time_read(colls[depth], depth, device_id)
            elif prob <0.7:
                print("u, ", end="" , flush=True)
                result[depth] += arr.time_update(colls[depth], depth, device_id)
            else:
                print("i, ", end="" , flush=True)
                result[depth] += arr.time_insert(colls[depth])
        print("---")

    delete_inserted(db)
    return result

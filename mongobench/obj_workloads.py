from random import random
from pymongo.collection import Collection
from pymongo.database import Database
from obj_helpers import delete_inserted
import obj_operations as obj

number_of_ops = 10
depth_list = [1,2,4,8]

def run_read_h():
    print("f")

def run_read_heavy(db: Database):
    print(f"---{'READ HEAVY'}---")
    colls: list[Collection] = [db['obj1'], db['obj2'], db['obj4'], db['obj8']]
    result = [0.0] * len(colls)

    device_id = 1
    for depth in range(len(colls)):
        print(f"    depth: {depth_list[depth]} ", end="| ", flush=True)
        prob = random()
        for _ in range(number_of_ops):
            prob = random()
            if prob<0.9:
                print("r, ", end="", flush=True)
                result[depth] += obj.time_read(colls[depth], depth, device_id)
            else:
                print("u, ", end="" , flush=True)
                result[depth] += obj.time_update(colls[depth], depth, device_id)
        print("---")

    return result

# 40% read, 60% update
def run_update_heavy(db: Database):
    print("---UPDATE HEAVY---")
    colls: list[Collection] = [db['obj1'], db['obj2'], db['obj4'], db['obj8']]
    result = [0.0] * len(colls)
    device_id = 1
    for depth in range(len(colls)):
        print(f"    depth: {depth_list[depth]} ", end="| ", flush=True)
        for _ in range(number_of_ops):
            prob = random()
            if prob<0.4:
                print("r, ", end="", flush=True)
                result[depth] += obj.time_read(colls[depth], depth, device_id)
            else:
                print("u, ", end="" , flush=True)
                result[depth] += obj.time_update(colls[depth], depth, device_id)
        print("---")
    return result

# 40% read 60% insert
def run_insert_heavy(db: Database):
    print("---INSERT HEAVY---")
    colls: list[Collection] = [db['obj1'], db['obj2'], db['obj4'], db['obj8']]
    result = [0.0] * len(colls)
    device_id = 1
    for depth in range(len(colls)):
        print(f"    depth: {depth_list[depth]} ", end="| ", flush=True)
        for _ in range(number_of_ops):
            prob = random()
            if prob<0.6:
                print("r, ", end="", flush=True)
                result[depth] += obj.time_read(colls[depth], depth, device_id)
            else:
                print("i, ", end="" , flush=True)
                result[depth] += obj.time_insert(colls[depth])
        print("---")

    delete_inserted(db)
    return result

# 40% read 30% update 30% insert
def run_mixed(db: Database):
    print("---MIXED---")
    colls: list[Collection] = [db['obj1'], db['obj2'], db['obj4'], db['obj8']]
    result = [0.0] * len(colls)
    device_id = 1
    for depth in range(len(colls)):
        print(f"    depth: {depth_list[depth]} ", end="| ", flush=True)
        for _ in range(number_of_ops):
            prob = random()
            if prob<0.4:
                print("r, ", end="", flush=True)
                result[depth] += obj.time_read(colls[depth], depth, device_id)
            elif prob <0.7:
                print("u, ", end="" , flush=True)
                result[depth] += obj.time_update(colls[depth], depth, device_id)
            else:
                print("i, ", end="" , flush=True)
                result[depth] += obj.time_insert(colls[depth])
        print("---")

    delete_inserted(db)
    return result

def run_group(db: Database):
    print("---GROUP---")
    colls: list[Collection] = [db['obj1'], db['obj2'], db['obj4'], db['obj8']]
    result = [0.0] * len(colls)

    for depth in range(len(colls)):
        print(f"    depth: {depth_list[depth]} ", end="| ", flush=True)
        for _ in range(number_of_ops):
                print("g, ", end="", flush=True)
                result[depth] += obj.time_group(colls[depth], depth)
        print("---")

    return result

def run_avg(db: Database):
    print("---AVERAGE---")
    colls: list[Collection] = [db['obj1'], db['obj2'], db['obj4'], db['obj8']]
    result = [0.0] * len(colls)

    for depth in range(len(colls)):
        print(f"    depth: {depth_list[depth]} ", end="| ", flush=True)
        for _ in range(number_of_ops):
                print("a, ", end="", flush=True)
                result[depth] += obj.time_avg(colls[depth], depth)
        print("---")

    return result

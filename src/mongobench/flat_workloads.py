from random import random
from pymongo.collection import Collection
from flat_helpers import create_batch
from flat_operations import time_avg, time_group, time_insert, time_read, time_update

operations_count = 50

# 90% Read, 10 % Update
def run_read_heavy(coll: Collection):
    print(f"---{'READ HEAVY':<20}: ", end="", flush=True)
    total_duration = 0.0
    device_id = 1

    for _ in range(operations_count):
        prob = random()
        
        if prob < 0.9:
            total_duration += time_read(coll, device_id)
        else:
            total_duration += time_update(coll, device_id)

    print(f"{total_duration * 1000:>10.0f} ms")

# 50% group and order, 50% calculate avg
def run_analytic(coll: Collection):
    print(f"---{'ANALYTIC':<20}: ", end="", flush=True)
    total_duration = 0.0

    for _ in range(operations_count):
        prob = random()
        if prob < 0.5:
            total_duration += time_group(coll)
        else:
            total_duration += time_avg(coll)

    print(f"{total_duration * 1000:>10.0f} ms")

# 50% read, 50% update
def run_update_heavy(coll: Collection):
    print(f"---{'UPDATE HEAVY':<20}: ", end="", flush=True)
    total_duration = 0.0
    device_id = 1

    for _ in range(operations_count):
        prob = random()
        
        if prob < 0.5:
            total_duration += time_read(coll, device_id)
        else:
            total_duration += time_update(coll, device_id)

    print(f"{total_duration * 1000:>10.0f} ms")


# 50% read, 50% insert
def run_insert_heavy(coll: Collection):
    print(f"---{'INSERT HEAVY':<20}: ", end="", flush=True)
    total_duration = 0.0
    device_id = 1

    for _ in range(operations_count):
        prob = random()
        
        if prob < 0.5:
            total_duration += time_read(coll, device_id)
        else:
            total_duration += time_insert(coll)

    print(f"{total_duration * 1000:>10.0f} ms")

# 40% read, 30% insert, 30% update
def run_mixed(coll: Collection):
    print(f"---{'MIXED':<20}: ", end="", flush=True)
    total_duration = 0.0
    device_id = 1

    for _ in range(operations_count):
        prob = random()
        
        if prob < 0.4:
            total_duration += time_read(coll, device_id)
        elif prob < 0.7:
            total_duration += time_insert(coll)
        else:
            total_duration += time_update(coll, device_id)

    print(f"{total_duration * 1000:>10.0f} ms")

from src.base_types.Base import Base
import src.elastic.es_operations as op

num_of_tries = 10

def run_read_only(types: list[Base]):
    print("---Read Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        op.time_memory_read(types[i])
        for _ in range(num_of_tries):
            print("r,", end=" ", flush=True)
            result[i] += op.time_memory_read(types[i])
        print("---")

    return result

def run_avg_only(types: list[Base]):
    print("---AVG Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        op.time_avg(types[i])
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
        op.time_group(types[i])
        for _ in range(num_of_tries):
            print("g,", end=" ", flush=True)
            result[i] += op.time_group(types[i])
        print("---")
    return result

def run_info_search(types: list[Base]):
    print("---INFO Search---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        op.time_info_read(types[i])
        for _ in range(num_of_tries):
            print("g,", end=" ", flush=True)
            result[i] += op.time_info_read(types[i])
        print("---")
    return result

def run_description_search(types: list[Base]):
    print("---TEXT Search---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        op.time_description_read(types[i])
        for _ in range(num_of_tries):
            print("g,", end=" ", flush=True)
            result[i] += op.time_description_read(types[i])
        print("---")
    return result

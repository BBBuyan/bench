from src.base_types.Base import Base
from src.elastic import logger
import src.elastic.es_operations as op

num_of_tries = 10

def run_read_only(types: list[Base]):
    print("---Read Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        ### warmup ###
        for _ in range(3):
            t = op.time_memory_read(types[i])
            print(f"{round(t)}, ", end="", flush=True)

        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        type_results = []
        for _ in range(num_of_tries):
            print("r,", end=" ", flush=True)
            type_results.append(op.time_memory_read(types[i]))
        print("---")
        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "read model_nr", types[0].coll_type)
    return result

def run_avg_only(types: list[Base]):
    print("---AVG Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        ### warmup ###
        for _ in range(3):
            t = op.time_avg(types[i])
            print(f"{round(t)}, ", end="", flush=True)


        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        type_results = []
        for _ in range(num_of_tries):
            print("a,", end=" ", flush=True)
            type_results.append(op.time_avg(types[i]))
        print("---")
        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "avg", types[0].coll_type)
    return result

def run_group_only(types: list[Base]):
    print("---Group Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        ### warmup ###
        for _ in range(3):
            t = op.time_group(types[i])
            print(f"{round(t)}, ", end="", flush=True)



        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        type_results = []
        for _ in range(num_of_tries):
            print("g,", end=" ", flush=True)
            type_results.append(op.time_group(types[i]))
        print("---")
        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "group", types[0].coll_type)
    return result

def run_info_search(types: list[Base]):
    print("---INFO Search---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        ### warmup ###
        for _ in range(3):
            t = op.time_info_read(types[i])
            print(f"{round(t)}, ", end="", flush=True)

        
        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        type_results = []
        for _ in range(num_of_tries):
            print("g,", end=" ", flush=True)
            type_results.append(op.time_info_read(types[i]))
        print("---")
        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "info", types[0].coll_type)
    return result

def run_description_search(types: list[Base]):
    print("---TEXT Search---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        ### warmup ###
        for _ in range(3):
            t = op.time_description_read(types[i])
            print(f"{round(t)}, ", end="", flush=True)



        print(f"depth: {types[i].name} | ", end=" ", flush=True)
        type_results = []
        for _ in range(num_of_tries):
            print("g,", end=" ", flush=True)
            type_results.append(op.time_description_read(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "description", types[0].coll_type)
    return result

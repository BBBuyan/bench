from random import random
from src.couch import logger
from src.couch.db_types.Base import Base
from src.couch import operations as op

num_of_tries = 10

def run_read_only(types: list[Base]):
    print("---Read Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)
        type_results = []
        for _ in range(num_of_tries):
            print("r,", end=" ", flush=True)
            type_results.append(op.time_read(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "read_only", types[0].coll_type)
    return result

def run_update_only(types: list[Base]):
    print("---Update Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)

        type_results = []
        for _ in range(num_of_tries):
            print("u,", end=" ", flush=True)
            type_results.append(op.time_update(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "update_only", types[0].coll_type)
    return result

def run_insert_only(types: list[Base]):
    print("---Insert Only---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)

        type_results = []
        for _ in range(num_of_tries):
            print("i,", end=" ", flush=True)
            type_results.append(op.time_insert(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "insert_only", types[0].coll_type)
    return result

def run_read_after_update(types: list[Base]):
    print("---Read after Update---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)
        type_results = []
        for _ in range(num_of_tries):
            print("u,", end=" ", flush=True)
            op.time_update(types[i])
            type_results.append(op.time_read(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "read after update", types[0].coll_type)
    return result

def run_read_after_insert(types: list[Base]):
    print("---Read after Insert---")
    result = [0.0] * len(types)

    for i in range(len(types)):
        print(f"{types[i].name} | ", end=" ", flush=True)
        type_results = []
        for _ in range(num_of_tries):
            print("i,", end=" ", flush=True)
            op.time_insert(types[i])
            type_results.append(op.time_read(types[i]))
        print("---")

        print([f"{x:.1f}" for x in type_results])
        result[i] = sum(type_results)/len(type_results)

    logger.save_result(result, "read after insert", types[0].coll_type)
    return result

# def run_read_heavy(types: list[Base]):
#     print("---Read Heavy---")
#     result = [0.0] * len(types)
#
#     for i in range(len(types)):
#         print(f"depth: {types[i].name} | ", end=" ", flush=True)
#
#         type_results = []
#         for _ in range(num_of_tries):
#             prob = random()
#
#             if prob < 0.9:
#                 print("r,", end=" ", flush=True)
#                 tmp = op.time_read(types[i])
#             else:
#                 print("u,", end=" ", flush=True)
#                 tmp = op.time_update(types[i])
#         print("---")
#
#     print(result)
#
#
#     return result

# def run_update_heavy(types: list[Base]):
#     print("---Update Heavy---")
#     result = [0.0] * len(types)
#
#     for i in range(len(types)):
#         print(f"depth: {types[i].name} | ", end=" ", flush=True)
#         for _ in range(num_of_tries):
#             prob = random()
#
#             if prob < 0.1:
#                 print("r,", end=" ", flush=True)
#                 result[i] += op.time_read(types[i])
#             else:
#                 print("u,", end=" ", flush=True)
#                 result[i] += op.time_update(types[i])
#
#         print("---")
#     return result
#
# def run_insert_heavy(types: list[Base]):
#     print("---Insert Heavy---")
#     result = [0.0] * len(types)
#
#     for i in range(len(types)):
#         print(f"depth: {types[i].name} | ", end=" ", flush=True)
#         for _ in range(num_of_tries):
#             prob = random()
#             if prob < 0.1:
#                 print("r,", end=" ", flush=True)
#                 result[i] += op.time_read(types[i])
#             else:
#                 print("i,", end=" ", flush=True)
#                 result[i] += op.time_insert(types[i])
#         print("---")
#
#     return result

# def run_mixed(types: list[Base]):
#     print("---Mixed---")
#     result = [0.0] * len(types)
#
#     for i in range(len(types)):
#         print(f"depth: {types[i].name} | ", end=" ", flush=True)
#         for _ in range(num_of_tries):
#             prob = random()
#
#             if prob < 0.4:
#                 print("r,", end=" ", flush=True)
#                 result[i] += op.time_read(types[i])
#             elif prob < 0.7:
#                 print("u,", end=" ", flush=True)
#                 result[i] += op.time_update(types[i])
#             else:
#                 print("i,", end=" ", flush=True)
#                 result[i] += op.time_insert(types[i])
#
#         print("---")

    # return result

# def run_mixed_special(types: list[Base]):
#     print("---Mixed Special---")
#     result = [0.0] * len(types)
#
#     for i in range(len(types)):
#         print(f"depth: {types[i].name} | ", end=" ", flush=True)
#         for _ in range(num_of_tries):
#             prob = random()
#
#             if prob < 0.4:
#                 print("r,", end=" ", flush=True)
#                 result[i] += op.time_read(types[i])
#             elif prob < 0.7:
#                 print("u,", end=" ", flush=True)
#                 op.time_update(types[i])
#                 result[i] += op.time_read(types[i])
#             else:
#                 print("i,", end=" ", flush=True)
#                 op.time_insert(types[i])
#                 result[i] += op.time_read(types[i])
#
#         print("---")
#
#     return result

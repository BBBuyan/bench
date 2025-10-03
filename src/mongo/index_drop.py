from .mongo_types import BaseMongo
from .conn import all_list, arr_list, flat_list, obj_list


def drop_indexes(types: list[BaseMongo]):
    print("---DROPPING INDEXES", end=" ", flush=True)
    for type in types:
        print(f"{type.name},", end=" ", flush=True)
        type.coll.drop_indexes()
    print("DONE---")

if __name__ == "__main__":
    drop_indexes(all_list)

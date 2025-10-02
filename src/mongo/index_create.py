from .mongo_types import BaseMongo
from .conn import all_list, arr_list, flat_list, obj_list


def create_indexes(types: list[BaseMongo]):
    print("---CREATING INDEXES", end=" ", flush=True)
    for type in types:
        print(f"{type.name},", end=" ", flush=True)
        type.coll.create_index(type.error_path)
    print("DONE---")

if __name__ == "__main__":
    create_indexes(flat_list)

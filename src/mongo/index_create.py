from .mongo_helper import create_indexes
from .conn import all_list, arr_list, flat_list, obj_list

if __name__ == "__main__":
    create_indexes(flat_list)


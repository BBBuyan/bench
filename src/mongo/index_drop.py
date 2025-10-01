from .mongo_helper import drop_indexes
from .conn import all_list, arr_list, flat_list, obj_list

if __name__ == "__main__":
    drop_indexes(flat_list)

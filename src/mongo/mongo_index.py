from .mongo_helper import create_indexes, drop_indexes
from .conn import all_list

if __name__ == "__main__":
    create_indexes(all_list)

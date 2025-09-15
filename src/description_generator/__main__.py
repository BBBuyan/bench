from src.base_types import Arr
from src.description_generator.exec_type import ExecType
from .assigner import assign_data
from src import flat_types, obj_types, arr_types, all_types

if __name__ == "__main__":
    for type in all_types:
        assign_data(type, ExecType.INFO)
        assign_data(type, ExecType.DESCRIPTION)

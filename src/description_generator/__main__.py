from src.description_generator.exec_type import ExecType
from .generator import sequential_exec, concurrent_exec
from .assigner import assign_data
from src import flat_types, obj_types, arr_types

if __name__ == "__main__":
    print("Description Generator Started")
    # for i in range(5):
    #     print(i, end=", ", flush=True)
    #     thread_main()
    #
    # print("")
    #
    # for type in all_types:
    #     print(type.name)
    #     assign_descriptions(type)

    # concurrent_exec(ExecType.DESCRIPTION)
    # sequential_exec(ExecType.DESCRIPTION)
    assign_data(arr_types[0], ExecType.INFO)
        

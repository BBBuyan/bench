from .generator import execute_batch, thread_main
from .assigner import assign_descriptions
from src import all_types

if __name__ == "__main__":
    print("Description Generator Started")
    for i in range(5):
        print(i, end=", ", flush=True)
        thread_main()

    print("")

    for type in all_types:
        print(type.name)
        assign_descriptions(type)
        

from .generator import execute_100
from .assigner import assign_descriptions
from src import all_types

if __name__ == "__main__":
    for i in range(100):
        print(i, end=" ", flush=True)
        # execute_100()

    print("")

    for type in all_types:
        print(type.name)
        # assign_descriptions(type)
        

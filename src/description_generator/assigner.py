import os
from json import loads, dumps
from pathlib import Path
from base_types.Base import Base

def assign_descriptions(type: Base):
    description_path =  Path(__file__).parent.parent.parent/"data"/"descriptions.json"
    type_path = Path(__file__).parent.parent.parent/"data"/f"{type.name}.json"
    temp_path = Path(__file__).parent.parent.parent/"data"/f"{type.name}_temp.json"

    print("Assigning descriptions for ", type.name)
    with open(description_path, "r") as f:
        descriptions = [loads(line)["description"] for line in f]

    with \
        open(type_path, "r") as read_file,\
        open(temp_path, "w") as out_file:
        i = 0
        for line in read_file:
            json_data = loads(line)
            type.add_description(descriptions, json_data)
            out_file.write(dumps(json_data) + "\n")
            i += 1
            if i % type.assign_log_threshold == 0:
                print(i, end=", ", flush=True)

    os.replace(temp_path, type_path)
    print("---DONE---")


from uuid import uuid4
import os
from json import loads, dumps
from db_types.Base import Base

def assign_uuid(type: Base):
    print("Assigning uuids for", type.name)
    with \
        open(f"../../data/{type.name}.json", "r") as read_file,\
        open(f"../../data/{type.name}_temp.json", "w") as out_file:
        i = 0
        for line in read_file:
            json_data = loads(line)
            type.add_id(uuid4().hex, json_data)

            out_file.write(dumps(json_data) + "\n")
            i += 1
            if i % type.assign_log_threshold == 0:
                print(i)

    os.replace(f"../../data/{type.name}_temp.json", f"../../data/{type.name}.json")
    print("done")

def assign_descriptions(type: Base):
    print("Assigning descriptions for", type.name)
    with open("../../data/descriptions.json", "r") as f:
        descriptions = [loads(line)["description"] for line in f]

    with \
        open(f"../../data/{type.name}.json", "r") as read_file,\
        open(f"../../data/{type.name}_temp.json", "w") as out_file:
        i = 0
        for line in read_file:
            json_data = loads(line)
            type.add_description(descriptions, json_data)

            out_file.write(dumps(json_data) + "\n")
            i += 1
            if i % type.assign_log_threshold == 0:
                print(i, end=", ", flush=True)

    os.replace(f"../../data/{type.name}_temp.json", f"../../data/{type.name}.json")
    print("done")

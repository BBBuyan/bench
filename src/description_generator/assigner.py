import os
from json import loads, dumps
from pathlib import Path
from src.base_types import Base
from .exec_type import ExecType

def assign_data(type: Base, exec_type: ExecType):
    data_path =  Path(__file__).parent.parent.parent/"data"/f"{exec_type.value}.json"
    type_path = Path(__file__).parent.parent.parent/"data"/f"{type.name}.json"
    temp_path = Path(__file__).parent.parent.parent/"data"/f"{type.name}_temp.json"

    print(f"---{type.name} {exec_type.value}", end=" ", flush=True)
    inputs =[]
    line_num = 0
    parsed =0
    with open(data_path, "r") as f:
        for line in f:
            line_num +=1
            try:
                obj = loads(line)[exec_type.value]
                inputs.append(obj)
                parsed += 1
            except:
                pass

    with \
        open(type_path, "r") as read_file,\
        open(temp_path, "w") as out_file:
        i = 0
        for line in read_file:
            json_data = loads(line)
            type.add_field(json_data, inputs, exec_type.value)
            out_file.write(dumps(json_data) + "\n")

            i += 1
            if i % type.assign_log_threshold == 0:
                print(i, end=", ", flush=True)

    os.replace(temp_path, type_path)
    print("---DONE---")


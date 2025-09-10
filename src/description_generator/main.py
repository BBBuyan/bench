import requests
from base_types.Base import Base
from conn import url, headers, my_data
from json import loads

def get_descriptions():
    r = requests.post(url, headers=headers, json=my_data)
    data: dict = r.json()
    doc = data["content"]["text"]
    print(" | ", end="", flush=True)
    return doc

def save(lines):
    with open("descriptions.json", "a") as f:
        for line in lines:
            f.write(line + "\n")
    print(len(lines), end=", ", flush=True)

def execute_100():
    descs: str = get_descriptions()
    lines = descs.splitlines()
    save(lines)

def main():
    print("---STARTED---")
    for i in range(50):
        print(i, end="", flush=True)
        execute_100()
    print("\n---DONE---")


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


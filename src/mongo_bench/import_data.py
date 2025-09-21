from json import loads
from .mongo_types import BaseMongo
from .conn import arr_list, obj_list, flat_list, all_list
from pathlib import Path

def execute_import(type: BaseMongo, json_data: list[dict]):
    type.coll.insert_many(json_data)

def import_docs(type: BaseMongo):
    print(f"---Import---")
    print(f"  {type.name}")
    file_path = Path(__file__).parent.parent.parent/"data"/f"{type.name}.json"

    batch = []
    i = 0
    with open(file_path, "r") as f:
        for line in f:
            json_data = loads(line)
            batch.append(json_data)

            if(len(batch) >= 1000):
                execute_import(type, batch)

                batch.clear()
                i += 1000
                if i % type.assign_log_threshold == 0:
                    print(f"{i:,}")

if __name__ == "__main__":
    # import_docs(flat_list[0])
    # for i in arr_list:
    #     import_docs(i)
    for i in all_list:
        import_docs(i)

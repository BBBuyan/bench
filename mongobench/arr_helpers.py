from random import randint
from pymongo.collection import Collection
from pymongo.database import Database

device_path_1 = "a1.device"
device_path_2 = "a1.a2.device"
device_path_4 = "a1.a2.a3.a4.device"
device_path_8 = "a1.a2.a3.a4.a5.a6.a7.a8.device"
device_paths = [device_path_1, device_path_2, device_path_4, device_path_8]

vol_path_1 = "a1.total_volume_bytes"
vol_path_2 = "a1.a2.total_volume_bytes"
vol_path_4 = "a1.a2.a3.a4.total_volume_bytes"
vol_path_8 = "a1.a2.a3.a4.a5.a6.a7.a8.total_volume_bytes"
vol_paths = [vol_path_1, vol_path_2, vol_path_4, vol_path_8]

unwind_path_1 = "a1"
unwind_path_2 = "a1.a2"
unwind_path_4 = "a1.a2.a3.a4"
unwind_path_8 = "a1.a2.a3.a4.a5.a6.a7.a8"
unwind_paths = [unwind_path_1, unwind_path_2, unwind_path_4, unwind_path_8]

depth_list = [1,2,4,8]
device_gte_list = [8250, 9100, 9760, 9980]

def unwind_up_to(depth: int):
    unwind = []
    path = ""
    for i in range(depth_list[depth]):
        if i !=0:
            path += "."
        path += f"a{i+1}"
        unwind.append({"$unwind": f"${path}"})
    return unwind

def read_where_builder(depth: int, device_id: int):
    clause = {device_paths[depth]: device_id}
    return clause

def update_where_builder(depth: int, device_id: int):
    clause = {device_paths[depth]: device_id}
    return clause

def update_clause_builder(depth: int):
    new_vol = randint(0, 9999)
    update_clause = [{"$set": {vol_paths[depth]: new_vol}}]
    return update_clause

def group_pipe_builder(depth: int):
    main_clause = unwind_up_to(depth)
    group_clause = [
        {"$group": {"_id": f"${device_paths[depth]}"}},
        {"$sort": {"_id": 1}}
    ]
    main_clause.extend(group_clause)

    return main_clause

def avg_pipe_builder(depth: int):
    main_clause = unwind_up_to(depth)
    avg_pipe = [
        {"$match": {f"{device_paths[depth]}": {"$gte": device_gte_list[depth]}}},
        {"$group": {"_id": None, "average_volume": {"$avg": f"${vol_paths[depth]}"}}}
    ]
    main_clause.extend(avg_pipe)
    return main_clause

def generate_insert_batch(coll: Collection, size: int)-> list:
    offset = randint(0, 9000)
    new_objs = list(coll.find({}, {"_id": 0}).skip(offset).limit(size))
    for el in new_objs:
        el["inserted"] = True
    return new_objs

def create_indexes(db: Database):
    db.arr1.create_index([("a1.device", 1)])
    db.arr2.create_index([("a1.a2.device", 1)])
    db.arr4.create_index([("a1.a2.a3.a4.device", 1)])
    db.arr8.create_index([("a1.a2.a3.a4.a5.a6.a7.a8.device", 1)])

def delete_indexes(db: Database):
    db.arr1.drop_indexes()
    db.arr2.drop_indexes()
    db.arr4.drop_indexes()
    db.arr8.drop_indexes()

def calc_diffs(old: list[float], new: list[float]):
    for i in range(len(old)):
        old_val = old[i]
        new_val = new[i]
        diff = ((new_val - old_val)/old_val)*100
        print(f"|{old[i]:>10.0f}|{new[i]:>10.0f}|{diff:>10.0f}|")

def delete_inserted(db: Database):
    print(db.arr1.delete_many({"inserted": True}))
    print(db.arr2.delete_many({"inserted": True}))
    print(db.arr4.delete_many({"inserted": True}))
    print(db.arr8.delete_many({"inserted": True}))

def count_gte(db: Database):
    print(db.arr1.count_documents({"a1.device": {"$gte": device_gte_list[0]}}))
    print(db.arr2.count_documents({"a1.a2.device": {"$gte": device_gte_list[1]}}))
    print(db.arr4.count_documents({"a1.a2.a3.a4.device": {"$gte": device_gte_list[2]}}))
    print(db.arr8.count_documents({"a1.a2.a3.a4.a5.a6.a7.a8.device": {"$gte": device_gte_list[3]}}))


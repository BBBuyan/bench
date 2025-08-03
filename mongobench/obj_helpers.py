from random import randint
from pymongo.collection import Collection
from pymongo.database import Database

device_path_1 = "l1.device"
device_path_2 = "l1.l2.device"
device_path_4 = "l1.l2.l3.l4.device"
device_path_8 = "l1.l2.l3.l4.l5.l6.l7.l8.device"
device_paths = [device_path_1, device_path_2, device_path_4, device_path_8]

vol_path_1 = "l1.total_volume_bytes"
vol_path_2 = "l1.l2.total_volume_bytes"
vol_path_4 = "l1.l2.l3.l4.total_volume_bytes"
vol_path_8 = "l1.l2.l3.l4.l5.l6.l7.l8.total_volume_bytes"
vol_paths = [vol_path_1, vol_path_2, vol_path_4, vol_path_8]

depth_list = [1,2,4,8]
device_gte_list = [9650 , 9650, 9660, 9650]


def where_device_builder(depth: int, device_id: int):
    return {device_paths[depth]: device_id}

def update_clause_builder(depth: int):
    new_vol = randint(0, 9999)
    update_clause = [{"$set": {vol_paths[depth]: new_vol}}]
    return update_clause

def generate_insert_batch(coll: Collection, size: int):
    offset = randint(0, 9000)
    new_objs = list(coll.find({}, {"_id": 0}).skip(offset).limit(size))
    for el in new_objs:
        el["inserted"]=True
    return new_objs

def group_pipe_builder(depth: int):
    clause = [
        {"$group": {"_id": f"${device_paths[depth]}"}},
        {"$sort": {"_id": 1}}
    ]
    return clause

def avg_pipe_builder(depth: int):
    clause = [
        {"$match": {f"{device_paths[depth]}": {"$gte": device_gte_list[depth]}}},
        {"$group": {"_id": None, "avg_vol": {"$avg": f"{vol_paths[depth]}"}}}
    ]
    return clause

def create_indexes(db: Database):
    db.obj1.create_index([("l1.device")])
    db.obj2.create_index([("l1.l2.device")])
    db.obj4.create_index([("l1.l2.l3.l4.device")])
    db.obj8.create_index([("l1.l2.l3.l4.l5.l6.l7.l8.device")])

def delete_indexes(db: Database):
    db.obj1.drop_indexes()
    db.obj2.drop_indexes()
    db.obj4.drop_indexes()
    db.obj8.drop_indexes()

def delete_inserted(db: Database):
    print(db.obj1.delete_many({"inserted": True}))
    print(db.obj2.delete_many({"inserted": True}))
    print(db.obj4.delete_many({"inserted": True}))
    print(db.obj8.delete_many({"inserted": True}))

def calc_diffs(old: list[float], new: list[float]):
    for i in range(len(old)):
        old_val = old[i]
        new_val = new[i]
        diff = ((new_val - old_val)/old_val)*100
        print(f"|{old[i]:>10.0f}|{new[i]:>10.0f}|{diff:>10.0f}|")

def count_device_gte(db: Database):
    print(db.obj1.count_documents({"l1.device": {"$gte": device_gte_list[0]}}))
    print(db.obj2.count_documents({"l1.l2.device": {"$gte": device_gte_list[1]}}))
    print(db.obj4.count_documents({"l1.l2.l3.l4.device": {"$gte": device_gte_list[2]}}))
    print(db.obj8.count_documents({"l1.l2.l3.l4.l5.l6.l7.l8.device": {"$gte": device_gte_list[3]}}))


from coll_type import CollType
import builders 
import helper
from paths import depth_list
from pprint import pprint
from conn import db
import paths
from helper import resolve_colls

op_types = [CollType.flat, CollType.arr, CollType.obj]
sub_id = 1


print("---Read---")
for type in op_types:
    colls = resolve_colls(type)
    print(f"{type.name}")
    for depth in range(len(colls)):
        pprint(builders.read_where_builder(type, depth, sub_id))

print("\n---Update Where---")
for type in op_types:
    colls = resolve_colls(type)
    print(f"{type.name}")
    for depth in range(len(colls)):
        pprint(builders.update_where_builder(type, depth, sub_id))

print("\n---Update Clause---")
for type in op_types:
    colls = resolve_colls(type)
    print(f"{type.name}")
    for depth in range(len(colls)):
        pprint(builders.update_clause_builder(type, depth))

print("\n---AVG---")
for type in op_types:
    colls = resolve_colls(type)
    print(f"{type.name}")
    for depth in range(len(colls)):
        pprint(builders.avg_pipe_builder(type, depth))

print("\n---Group---")
for type in op_types:
    colls = resolve_colls(type)
    print(f"{type.name}")
    for depth in range(len(colls)):
        pprint(builders.group_pipe_builder(type, depth))

# pprint(generate_insert_batch(db.flat, 1)




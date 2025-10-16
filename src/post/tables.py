from src.post.post_types import ArrPost, ObjPost, FlatPost, BasePost

levels = [1,2,4,8]

arr_tables = [ArrPost(i) for i in levels]
obj_tables = [ObjPost(i) for i in levels]
flat_tables = [FlatPost() for _ in levels]

all_tables = flat_tables + obj_tables + arr_tables

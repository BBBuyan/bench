from src.post.post_types import ArrPost, BasePost, ObjPost, FlatPost, FlatArrow, ObjArrow

levels = [1,2,4,8]

arr_tables: list[BasePost] = [ArrPost(i) for i in levels]
obj_tables: list[BasePost] = [ObjPost(i) for i in levels]
flat_tables: list[BasePost] = [FlatPost()]

obj_arrows: list[BasePost] = [ObjArrow(i) for i in levels]
flat_arrows: list[BasePost] = [FlatArrow()]

all_tables: list[BasePost] = flat_tables + obj_tables + arr_tables

arrow_tables: list[BasePost] = flat_arrows + obj_arrows

from src.post import post_bulder, post_op
from src.post.post_types import FlatPost
from src.post.post_types.ArrPost import ArrPost
from src.post.tables import all_tables, arr_tables, obj_tables, flat_tables


for i in all_tables:
    print(i.read_query)


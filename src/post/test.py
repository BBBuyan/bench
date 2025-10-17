from src.post import post_op as op
from src.post.post_types import BasePost
from src.post.tables import all_tables, arr_tables, obj_tables, flat_tables
from pprint import pprint

BasePost.is_debug = True
# print(post_op.time_read(arr_tables[1]), "ms")
# for i in post_helper.get_data(flat_tables[0]):
#     print(i[0])
    # break
print(op.time_avg(flat_tables[0]))
# print(obj_tables[0].get_sort_query())


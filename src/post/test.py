from src.post import post_op
from src.post.post_types import BasePost
from src.post.tables import all_tables, arr_tables, obj_tables, flat_tables
from pprint import pprint

BasePost.is_debug = True
# post_op.time_read(arr_tables[2])
print("hello")
post_op.time_read(flat_tables[0])
# for i in post_helper.get_data(flat_tables[0]):
#     print(i[0])
    # break

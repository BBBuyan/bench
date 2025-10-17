from src.post import post_works as work
from src.post.post_types import BasePost
from src.post.post_logger import mark_message, mark_operation
from src.post import tables

msg = "with index"

def bench(tables: list[BasePost]):
    mark_operation(tables[0].coll_type)
    mark_message(tables[0].coll_type, msg)

    work.run_read(tables)
    work.run_sort(tables)
    work.run_avg(tables)
    work.run_update(tables)
    work.run_insert(tables)

def flat():
    bench(tables.flat_tables)

def flat_arrow():
    bench(tables.flat_arrows)

def obj():
    bench(tables.obj_tables)

def obj_arrow():
    bench(tables.obj_arrows)

def arr():
    bench(tables.arr_tables)

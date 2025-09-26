from .mongo_types import BaseMongo
from . import mongo_workloads as work
from src.logger import logger 
from .conn import flat_list, obj_list, arr_list
from .mongo_helper import create_indexes, drop_indexes

file = "mongo_result"

class MongoBench():
    def _run_bench(self, types: list[BaseMongo], coll: str):
        read_only_0 = work.run_read_only(types)

        update_non_indexed_0 = work.run_update_non_indexed_field(types)

        avg_0 = work.run_avg(types)
        group_0 = work.run_group(types)
        insert_only_0 = work.run_insert_only(types)

        print("---CREATING INDEX", end=" ", flush=True)
        create_indexes(types)
        print("DONE---")

        read_only_1 = work.run_read_only(types)
        update_non_indexed_1 = work.run_update_non_indexed_field(types)
        update_indexed = work.run_update_indexed_field(types)

        avg_1 = work.run_avg(types)
        group_1 = work.run_group(types)
        insert_only_1 = work.run_insert_only(types)

        drop_indexes(types)

        logger.save_result(read_only_0, read_only_1, "read_only", file, coll)

        logger.save_result(update_non_indexed_0, update_non_indexed_1, "update_non_indexed", file, coll)

        logger.save_result(update_non_indexed_1, update_indexed, "update_indexed", file, coll)

        logger.save_result(avg_0, avg_1, "avg", file, coll)
        logger.save_result(group_0, group_1, "group", file, coll)
        logger.save_result(insert_only_0, insert_only_1, "insert_only", file, coll)

    def bench_flat(self):
        self._run_bench(flat_list, "flat")

    def bench_arr(self):
        self._run_bench(arr_list, "arr")

    def bench_obj(self):
        self._run_bench(obj_list, "obj")

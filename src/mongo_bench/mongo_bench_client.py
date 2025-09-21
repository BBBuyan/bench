from .mongo_types import BaseMongo
from . import mongo_workloads as work
from src.logger import logger 
from .conn import flat_list, obj_list, arr_list

file = "mongo_result"

class MongoBench():
    def _run_bench(self, types: list[BaseMongo], coll: str):
        read_0 = work.run_read_heavy(types)
        avg_0 = work.run_avg(types)
        group_0 = work.run_group(types)
        update_0 = work.run_update_heavy(types)
        insert_0 = work.run_insert_heavy(types)
        insert_only_0 = work.run_insert_only(types)

        read_1 = work.run_read_heavy(types)
        avg_1 = work.run_avg(types)
        group_1 = work.run_group(types)
        update_1 = work.run_update_heavy(types)
        insert_1 = work.run_insert_heavy(types)
        insert_only_1 = work.run_insert_only(types)

        logger.save_result(read_0, read_1, "read", file, coll)
        logger.save_result(avg_0, avg_1, "read", file, coll)
        logger.save_result(group_0, group_1, "read", file, coll)
        logger.save_result(update_0, update_1, "read", file, coll)
        logger.save_result(insert_0, insert_1, "read", file, coll)
        logger.save_result(insert_only_0, insert_only_1, "read", file, coll)

    def bench_flat(self):
        self._run_bench(flat_list, "flat")

    def bench_arr(self):
        self._run_bench(arr_list, "arr")

    def bench_obj(self):
        self._run_bench(obj_list, "obj")

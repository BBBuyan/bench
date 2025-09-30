from .mongo_types import BaseMongo
from . import mongo_workloads as work
from .conn import flat_list, obj_list, arr_list
from .mongo_helper import create_indexes, drop_indexes
from . import mongo_logger as logger

db_type = "mongodb"

class MongoBench():
    def _run_bench(self, types: list[BaseMongo], coll_name: str):

        logger.mark_operation(coll_name)
        logger.mark_message(coll_name, "")
        read_error_field = work.run_read_only(types)
        logger.save_result(read_error_field, "read by error", coll_name)

        read_by_shard_key = work.run_read_only_by_shard_key(types)
        logger.save_result(read_by_shard_key, "read by shard key", coll_name)

        update_storage = work.run_update_non_indexed_field(types)
        logger.save_result(update_storage, "update non indexed", coll_name)

        # update_indexed_field = work.run_update_non_indexed_field(types)
        # logger.save_result(update_indexed_field, "update indexed", coll_name)

        avg = work.run_avg(types)
        logger.save_result(avg, "average", coll_name)

        group = work.run_group(types)
        logger.save_result(group, "group", coll_name)

        insert = work.run_insert_only(types)
        logger.save_result(insert, "insert", coll_name)


    def bench_flat(self):
        self._run_bench(flat_list, "flat")

    def bench_arr(self):
        self._run_bench(arr_list, "arr")

    def bench_obj(self):
        self._run_bench(obj_list, "obj")

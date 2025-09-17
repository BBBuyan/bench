from src.base_types import Base
from src.elastic import es_workloads as work
from src import logger as log
from src import arr_types, flat_types, obj_types

file_name = "es_result"

class ElasticBench():

    def run_bench(self, types: list[Base] ,coll_type: str):
        read_0 = work.run_read_only(types)
        avg_0 = work.run_avg_only(types)
        group_0 = work.run_group_only(types)
        info_0 = work.run_info_search(types)
        description_0 = work.run_description_search(types)

        log.save_es_result(read_0,"read", file_name, coll_type)
        log.save_es_result(avg_0,"avg", file_name, coll_type)
        log.save_es_result(group_0,"group", file_name, coll_type)
        log.save_es_result(info_0,"info", file_name, coll_type)
        log.save_es_result(description_0,"description", file_name, coll_type)

    def bench_flat(self):
        self.run_bench(flat_types, "flat")

    def bench_arr(self):
        self.run_bench(arr_types, "arr")

    def bench_obj(self):
        self.run_bench(obj_types, "obj")

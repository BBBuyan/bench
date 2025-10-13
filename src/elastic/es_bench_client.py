from src.base_types import Base
from src.elastic import es_workloads as work
from src import arr_types, flat_types, obj_types
from . import logger

file_name = "es_result"

class ElasticBench():

    def run_bench(self, types: list[Base] ,coll_type: str):
        read_0 = work.run_read_only(types)
        avg_0 = work.run_avg_only(types)
        group_0 = work.run_group_only(types)
        info_0 = work.run_info_search(types)
        description_0 = work.run_description_search(types)


    def bench_flat(self):
        logger.mark_operation("flat")
        self.run_bench(flat_types, "flat")

    def bench_arr(self):
        logger.mark_operation("arr")
        self.run_bench(arr_types, "arr")

    def bench_obj(self):
        logger.mark_operation("obj")
        self.run_bench(obj_types, "obj")

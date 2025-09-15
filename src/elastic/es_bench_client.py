from src.base_types import Base
from src.elastic import es_workloads as work

def bench_analytics(types: list[Base]):
    avg_0 = work.run_avg_only(types)
    group_0 = work.run_group_only(types)
    info_0 = work.run_info_search(types)
    read_0 = work.run_read_only(types)
    description_0 = work.run_description_search(types)

    print(avg_0)
    print(group_0)
    print(info_0)
    print(read_0)
    print(description_0)


from src import arr_types, flat_types, obj_types
from .es_bench_client import bench_analytics

bench_analytics(flat_types)
bench_analytics(obj_types)
bench_analytics(arr_types)

from src.base_types import Base
from . import mongo_bench_client as bench

if __name__ == "__main__":
    bench.bench_flat()
    bench.bench_obj()
    bench.bench_arr()

from src.base_types import Base
from .mongo_bench_client import MongoBench

if __name__ == "__main__":
    bench = MongoBench()

    bench.bench_flat()
    # bench.bench_obj()
    # bench.bench_arr()

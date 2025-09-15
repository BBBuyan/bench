from src.elastic import es_bench_client as bench

if __name__ == "__main__":
    bench.bench_flat()
    bench.bench_obj()
    bench.bench_arr()

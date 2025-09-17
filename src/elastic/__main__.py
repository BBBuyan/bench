from src.elastic.es_bench_client import ElasticBench

if __name__ == "__main__":
    bench = ElasticBench()

    bench.bench_flat()
    bench.bench_obj()
    bench.bench_arr()

from .BasePost import BasePost
from src.post import queries_arr as query
from src.post import indexes, indexes_path_ops

class ArrPost(BasePost):
    def __init__(self, level: int) -> None:
        super().__init__(f"arr{level}")

        self.coll_type = "arr"
        self.read_query = query.read[level]
        self.sort_query = query.sort[level]
        self.avg_query = query.avg[level]
        self.update_storage = query.update_storage[level]

        self.index = indexes_path_ops.arr_indexes[level]
        self.index_drop = indexes_path_ops.arr_indexes_drop[level]


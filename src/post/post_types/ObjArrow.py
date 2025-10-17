from .BasePost import BasePost
from src.post import indexes_arrow
from src.post import queries_obj_arrow 

class ObjArrow(BasePost):
    def __init__(self, level: int) -> None:
        super().__init__(f"obj{level}")
        self.coll_type = "obj_arrow"

        self.read_query = queries_obj_arrow.read[level]
        self.sort_query = queries_obj_arrow.sort[level]
        self.avg_query = queries_obj_arrow.avg[level]
        self.update_storage = queries_obj_arrow.update_storage[level]

        self.index = indexes_arrow.obj_indexes_arrow[level]
        self.index_drop = indexes_arrow.obj_indexes_arrow_drop[level]



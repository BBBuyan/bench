from .BasePost import BasePost
from src.post import indexes_arrow
from src.post import queries_flat_arrow as query

class FlatArrow(BasePost):
    def __init__(self) -> None:
        super().__init__("flat")
        self.coll_type = "flat_arrow"

        self.read_query = query.read_flat
        self.sort_query = query.sort_flat
        self.avg_query = query.avg_flat
        self.update_storage = query.update_flat

        self.index = indexes_arrow.flat_index_arrow
        self.index_drop = indexes_arrow.flat_index_arrow_drop
 

from .BasePost import BasePost
from src.post import indexes

class FlatPost(BasePost):
    def __init__(self) -> None:
        super().__init__("flat")
        self.coll_type = "flat"

        self.read_query = self.get_read_query()
        self.sort_query = self.get_sort_query()
        self.avg_query = self.get_avg_query()
        self.update_storage = self.get_update_storage()

        self.index = indexes.flat_index
        self.index_drop = indexes.flat_index_drop
 
    def get_read_query(self):
        select_from = "select (data) from flat "
        where = "where data @@ '$.error_count == %s'"
        return select_from + where

    def get_sort_query(self):
        select = "select (data) "
        from_ = "from flat "
        where = "where data @@ '$.error_count == %s' "
        order_by = f"order by (data ->> 'total_storage_gb')::int"
        return select + from_ + where + order_by

    def get_avg_query(self):
        select = f"select avg((data ->> 'total_storage_gb')::numeric) "
        from_ = f"from flat"
        where = f" where data @@ '$.error_count == %s'"
        return select + from_ + where

    def get_update_storage(self):
        update_ = "update flat "
        set_ = "set data = %s "
        where = "where data @@ '$.error_count == %s'"
        return update_ + set_ + where 


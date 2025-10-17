from .BasePost import BasePost
from src.post import indexes

class ObjPost(BasePost):
    def __init__(self, level: int) -> None:
        super().__init__(f"obj{level}")
        self.coll_type = "obj"

        all_levels = ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8"]
        self.level = level
        self.levels = all_levels[:(level)]

        self.path = str.join(".", self.levels) 
        self.error_path = self.path + "." + self._error_field
        self.storage_path = self.path + "." + self._storage_field

        self.read_query = self.get_read_query()
        self.sort_query = self.get_sort_query()
        self.avg_query = self.get_avg_query()
        self.update_storage = self.get_update_storage()

        self.index = indexes.obj_indexes[level]
        self.index_drop = indexes.obj_indexes_drop[level]

    def get_read_query(self):
        select = f"select (data) "
        from_ = f"from {self.name} "
        where = f"where data @@ '$.{self.error_path} == %s'"
        return select + from_ + where

    def get_sort_query(self):
        select = f"select (data) "
        from_ = f"from {self.name} "
        where = f"where data @@ '$.{self.error_path} == %s' "
        order_by = f"order by (data #>> '{{ {str.join(",",self.levels)+","+self._storage_field} }}')::int"

        return select + from_ + where + order_by

    def get_avg_query(self):
        select = f"select avg((data #>> '{{ {str.join(",",self.levels)+","+self._storage_field} }}')::numeric) "
        from_ = f"from {self.name} "
        where = f"where data @@ '$.{self.error_path} == %s'"

        return select + from_ + where

    def get_update_storage(self):
        update_ = f"update {self.name} "
        set_ = f"set data = %s"
        where = f"where data @@ '$.{self.error_path} == %s'"

        return update_ + set_ + where 

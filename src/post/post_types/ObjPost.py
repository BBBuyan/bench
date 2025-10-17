from random import randint
from .BasePost import BasePost
from src.post import indexes

class ObjPost(BasePost):
    def __init__(self, level: int) -> None:
        super().__init__(f"obj{level}")

        all_levels = ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8"]
        self.level = level
        self.levels = all_levels[:(level)]

        self.path = str.join(",", self.levels) 

        self.model_path = self.path + "," + self._model_field
        self.error_path = self.path + "," + self._error_field
        self.storage_path = self.path + "," + self._storage_field
        self.temp_path = self.path + "," + self._temp_field
        self.uptime_path = self.path + "," + self._uptime_field
        self.app_path = self.path + "," + self._app_field

        self.description_path = self.path + "," + self._description_field
        self.info_path = self.path + "," + self._info_field

        self.coll_type = "obj"

        self.read_query = self.get_read_query()
        self.sort_query = self.get_sort_query()
        self.avg_query = self.get_avg_query()
        self.update_storage = self.get_update_storage()

        self.index = indexes.obj_indexes[level]
        self.index_drop = indexes.obj_indexes_drop[level]

    def get_read_query(self):
        select_from = f"select (data) from {self.name}"
        where = f" where (data #>> '{{ {self.model_path} }}')::int = %s"
        return select_from + where

    def get_sort_query(self):
        select_from = f"select (data) from {self.name} "
        where = f"where (data #>> '{{ {self.error_path} }}')::int = %s "
        order_by = f"order by (data #>> '{{ {self.storage_path} }}')::int"
        return select_from + where + order_by

    def get_avg_query(self):
        select = f"select avg((data #>> '{{ {self.storage_path} }}')::numeric) "
        from_ = f"from {self.name} "
        where = f"where (data #>> '{{ {self.error_path} }}')::int = %s"
        return select + from_ + where

    def get_update_storage(self):
        update_ = f"update {self.name} "
        set_ = f"set data = %s"
        where = f" where (data #>> '{{ {self.error_path} }}')::int = %s"
        return update_ + set_ + where 

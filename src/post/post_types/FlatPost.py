from .BasePost import BasePost

class FlatPost(BasePost):
    def __init__(self) -> None:
        super().__init__("flat")

        self.model_path = self._model_field
        self.error_path = self._error_field
        self.storage_path = self._storage_field
        self.temp_path = self._temp_field
        self.uptime_path = self._uptime_field
        self.app_path = self._app_field

        self.info_path = self._info_field
        self.description_path = self._description_field

        self.coll_type = "flat"
        self.read_query = self.get_read_query()
        self.sort_query = self.get_sort_query()

    def get_read_query(self):
        select_from = f"select (data) from {self.name}"
        where = f" where (data #>> '{{ {self.error_path} }}')::int = %s"
        return select_from + where

    def get_sort_query(self):
        select_from = f"select (data) from {self.name}"
        where = f" where (data #>> '{{ {self.error_path} }}')::int = %s"
        order_by = f"order by (data #>> '{{ {self.storage_path} }}')::int"
        return select_from + where + order_by

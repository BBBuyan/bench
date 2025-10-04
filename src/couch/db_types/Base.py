from random import randint
from src.couch.Conn import root_url

class Base:
    debug = False
    base_url = root_url

    def __init__(self, name) -> None:
        self.name = name
        self.url = root_url + name + "/"

        self.max_offset=0
        self.use_index=False

        self._memory_field = "model_number"
        self._error_field = "error_count"
        self._storage_field = "total_storage_gb"
        self._temp_field = "temp"
        self._uptime_field = "uptime_hours"
        self._app_field = "app"
        self._info_field = "info"
        self._description_field = "description"

        self.path=""
        self.memory_path = ""
        self.error_path = ""
        self.storage_path = ""
        self.temp_path = ""
        self.uptime_path = ""
        self.app_path = ""

        self.average_map_func=""

        self.batch_limit = 1000
        self.assign_log_threshold = 0
        self.coll_type = ""

    def get_error_query(self):
        query: dict = {
            "selector": {
                self.error_path: randint(0,9999)
            },
        }
        if self.use_index:
            query["use_index"] = f"{self.name}-error-index"

        return query

    def get_sort_query(self):
        query: dict = {
            "selector": {
                self.memory_path: randint(0,9999)
            },
            "sort":[
                {self.storage_path: "asc"}
            ]
        }
        return query


from src.base_types import Base

class BasePost():
    is_debug = False
    def __init__(self, name: str) -> None:
        self.database_name=""
        self.name = name

        self._model_field = "model_number"
        self._error_field = "error_count"
        self._storage_field = "total_storage_gb"
        self._temp_field = "temp"
        self._uptime_field = "uptime_hours"
        self._app_field = "app"
        self._info_field = "info"
        self._description_field = "description"

        self.path=""
        self.model_path = ""
        self.error_path = ""
        self.storage_path = ""
        self.temp_path = ""
        self.uptime_path = ""
        self.app_path = ""

        self.description_path = ""
        self.info_path = ""

        self.assign_log_threshold = 100_000
        self.max_docs = 1_000_000
        self.fetch_limit = 50_000

        self.coll_type = "base"
        self.levels = []

        self.read_query =""
        self.sort_query = ""
        self.avg_query = ""
        self.update_storage =""

        self.index = ""
        self.index_drop = ""

    def say_hi(self):
        print("")


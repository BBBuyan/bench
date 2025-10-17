class BasePost():
    is_debug = False
    def __init__(self, name: str) -> None:
        self.name = name
        self.coll_type = "base"

        self._model_field = "model_number"
        self._error_field = "error_count"
        self._storage_field = "total_storage_gb"
        self._temp_field = "temp"
        self._uptime_field = "uptime_hours"
        self._app_field = "app"
        self._info_field = "info"
        self._description_field = "description"

        self.read_query =""
        self.sort_query = ""
        self.avg_query = ""
        self.update_storage =""

        self.index = ""
        self.index_drop = ""

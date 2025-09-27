
class Base:
    is_debug = False
    def __init__(self, name: str) -> None:
        self.database_name=""
        self.name = name

        self._memory_field = "memory_usage_mb"
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

        self.description_path = ""
        self.info_path = ""

        self.assign_log_threshold = 100_000
        self.max_docs = 1_000_000
        self.fetch_limit = 50_000

    def add_field(self, editing_data: dict, inputs: list[str], field_name: str):
        raise NotImplementedError("Subclasses should implement")

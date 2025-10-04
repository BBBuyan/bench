from .Base import Base

class Flat(Base):
    def __init__(self) -> None:
        super().__init__("flat")
        self.assign_log_threshold = 100_000

        self.memory_path = self._memory_field
        self.error_path = self._error_field
        self.storage_path = self._storage_field
        self.temp_path = self._temp_field
        self.uptime_path = self._uptime_field
        self.app_path = self._app_field

        self.info_path = self._info_field
        self.description_path = self._description_field

        self.group_map_func = ""
        self.average_map_func = f"function (doc) {{ emit(doc.{self.error_path}, doc.{self.storage_path}) }}"
        self.coll_type = "flat"



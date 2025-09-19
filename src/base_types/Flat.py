from .Base import Base
from random import choice

class Flat(Base):
    def __init__(self) -> None:
        super().__init__("flat")

        self.memory_path = self._memory_field
        self.error_path = self._error_field
        self.storage_path = self._storage_field
        self.temp_path = self._temp_field
        self.uptime_path = self._uptime_field
        self.app_path = self._app_field

        self.info_path = self._info_field
        self.description_path = self._description_field

    def add_field(self, editing_data: dict, inputs: list[str], field_name: str):
        editing_data[field_name] = choice(inputs)

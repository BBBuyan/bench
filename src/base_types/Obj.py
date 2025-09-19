from .Base import Base
from random import choice

class Obj(Base):

    def __init__(self, level: int) -> None:
        super().__init__(f"obj{level}")

        all_levels = ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8"]
        self.level = level
        self.levels = all_levels[:(level)]

        self.path = str.join(".", self.levels) 

        self.memory_path = self.path + f".{self._memory_field}"
        self.error_path = self.path + f".{self._error_field}"
        self.storage_path = self.path + f".{self._storage_field}"
        self.temp_path = self.path + f".{self._temp_field}"
        self.uptime_path = self.path + f".{self._uptime_field}"
        self.app_path = self.path + f".{self._app_field}"

        self.description_path = self.path + f".{self._description_field}"
        self.info_path = self.path + f".{self._info_field}"

    def add_field(self, editing_data: dict, inputs: list[str], field_name: str):
        for k in self.levels[:-1]:
            editing_data = editing_data[k]
        editing_data[self.levels[-1]][field_name] = choice(inputs)

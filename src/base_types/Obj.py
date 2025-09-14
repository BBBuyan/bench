from .Base import Base
from random import choice

class Obj(Base):

    def __init__(self, level: int) -> None:
        super().__init__(f"obj{level}")

        all_levels = ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8"]
        self.level = level
        self.levels = all_levels[:(level)]

        self.path = str.join(".", self.levels) 
        self.device_path = self.path + f".{self._device_field}"
        self.vol_path = self.path + f".{self._vol_field}"
        self.app_path = self.path + f".{self._app_field}"
        self.num_path = self.path + f".{self._num_field}"
        self.sub_path = self.path + f".{self._sub_field}"
        self.description_path = self.path + f".{self._description_field}"
        self.info_path = self.path + f".{self._info_field}"

    def add_field(self, editing_data: dict, inputs: list[str], field_name: str):
        for k in self.levels[:-1]:
            editing_data = editing_data[k]
        editing_data[self.levels[-1]][field_name] = choice(inputs)

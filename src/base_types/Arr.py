from .Base import Base
from random import choice

class Arr(Base):
    def __init__(self, level: int) -> None:
        super().__init__(f"arr{level}")

        all_levels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
        self.level = level
        self.levels = all_levels[:(level)]

        self.assign_log_threshold = 1000

        self.device_path = str.join(".", self.levels) + f".{self._device_field}"
        self.vol_path = str.join(".", self.levels) + f".{self._vol_field}"
        self.app_path = str.join(".", self.levels) + f".{self._app_field}"
        self.num_path = str.join(".", self.levels) + f".{self._num_field}"
        self.sub_path = str.join(".", self.levels) + f".{self._sub_field}"
        self.description_path = str.join(".", self.levels) + f".{self._description_field}"

    def add_field(self, editing_data: dict, inputs: list[str], field_name: str, current_level: int = 0):
        if current_level > self.level:
            return

        key = self.levels[current_level]
        for item in editing_data.get(key, []):
            if current_level == self.level - 1:
                item[field_name] = choice(inputs)
            else:
                self.add_field(editing_data, inputs , field_name, current_level +1)



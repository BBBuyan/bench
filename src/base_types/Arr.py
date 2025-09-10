from base_types.Base import Base
from random import choice

class Arr(Base):
    device_map = {
        1: "a1.device",
        2: "a1.a2.device",
        4: "a1.a2.a3.a4.device",
        8: "a1.a2.a3.a4.a5.a6.a7.a8.device",
    }
    all_levels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]

    def __init__(self, level: int) -> None:
        super().__init__(f"arr{level}")
        self.level = level
        self.levels = self.all_levels[(8-level)]
        self.device_path = self.device_map[level]

    def add_description(self, descriptions: list[str], data: dict, current_level: int=0):
        if current_level > len(self.levels):
            return

        key = self.levels[current_level]
        for item in data.get(key, []):
            if current_level == self.level - 1:
                item["description"] = choice(descriptions)
            else:
                self.add_description(descriptions, item, current_level + 1)

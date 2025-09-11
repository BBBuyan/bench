from .Base import Base
from random import choice

class Obj(Base):
    all_levels = ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8"]

    def __init__(self, level: int) -> None:
        super().__init__(f"obj{level}")
        self.level = level
        self.levels = self.all_levels[:(level)]

    def add_description(self, descriptions: list[str], data: dict):
        for k in self.levels[:-1]:
            data = data[k]
        data[self.levels[-1]][self._description_field] = choice(descriptions)

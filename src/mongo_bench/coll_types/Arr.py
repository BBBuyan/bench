from coll_types.Base import Base
from pymongo.collection import Collection

class Arr(Base):
    def __init__(self, coll: Collection, level: int) -> None:
        super().__init__(coll)
        all_levels = ["a1","a2","a3","a4","a5","a6","a7","a8"]
        self.level = level
        self.levels = all_levels[:(level)]


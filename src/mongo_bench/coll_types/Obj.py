from coll_types.Base import Base
from pymongo.collection import Collection

class Obj(Base):
    def __init__(self, coll: Collection, level: int) -> None:
        super().__init__(coll)
        all_levels = ["l1","l2","l3","l4","l5","l6","l7","l8"]
        self.level = level
        self.levels = all_levels[:(level)]


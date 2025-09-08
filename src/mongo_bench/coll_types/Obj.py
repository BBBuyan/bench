from coll_types.Base import Base
from pymongo.collection import Collection

class Obj(Base):
    def __init__(self, coll: Collection, level: int) -> None:
        super().__init__(coll)
        all_levels = ["l1","l2","l3","l4","l5","l6","l7","l8"]
        self.level = level
        self.levels = all_levels[:(level)]

        self.vol_path = ".".join(self.levels) + "." + self._vol_field
        self.num_path = ".".join(self.levels) + "." + self._num_field
        self.sub_path = ".".join(self.levels) + "." + self._sub_field
        self.app_path = ".".join(self.levels) + "." + self._app_field




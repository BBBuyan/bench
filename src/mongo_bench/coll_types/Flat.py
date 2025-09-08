from coll_types.Base import Base
from pymongo.collection import Collection

class Flat(Base):
    def __init__(self, coll: Collection) -> None:
        super().__init__(coll)
        self.vol_path = self._vol_field
        self.num_path = self._num_field
        self.sub_path = self._sub_field
        self.app_path = self._app_field


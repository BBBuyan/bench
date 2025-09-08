from coll_types.Base import Base
from pymongo.collection import Collection

class Flat(Base):
    def __init__(self, coll: Collection) -> None:
        super().__init__(coll)


from src.base_types import Base
from pymongo.collection import Collection

class BaseMongo(Base):
    def __init__(self, name: str, coll: Collection) -> None:
        super().__init__(name)
        self.coll = coll

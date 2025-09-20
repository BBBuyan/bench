from pymongo.collection import Collection
from abc import ABC, abstractmethod
from src.base_types.Base import Base

class BaseMongo(ABC, Base):
    @property
    @abstractmethod
    def coll(self) -> Collection:
        pass

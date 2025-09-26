from src.base_types import Flat
from pymongo.collection import Collection
from .BaseMongo import BaseMongo

class FlatMongo(BaseMongo, Flat):
    def __init__(self, coll: Collection) -> None:
        super().__init__()
        self._coll = coll

    @property
    def coll(self) -> Collection:
        return self._coll


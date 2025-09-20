from src.base_types import Obj
from pymongo.collection import Collection
from src.mongo_bench.mongo_types.BaseMongo import BaseMongo

class ObjMongo(BaseMongo, Obj):
    def __init__(self, level: int, coll) -> None:
        super().__init__(level)
        self._coll = coll

    @property
    def coll(self) -> Collection:
        return self._coll

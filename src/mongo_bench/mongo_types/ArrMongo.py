from pymongo.collection import Collection
from src.base_types import Arr
from src.mongo_bench.mongo_types.BaseMongo import BaseMongo

class ArrMongo(BaseMongo, Arr):
    def __init__( self , level: int, coll: Collection ) -> None:
        super().__init__(level)
        self._coll = coll

    @property
    def coll(self) -> Collection:
        return self._coll


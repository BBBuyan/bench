from pymongo.collection import Collection
from src.base_types import Arr
from .BaseMongo import BaseMongo

class ArrMongo(BaseMongo, Arr):
    def __init__( self , level: int, coll: Collection ) -> None:
        super().__init__(level)
        self._coll = coll
        self._unwind = self._get_unwind(level)

    @property
    def coll(self) -> Collection:
        return self._coll

    @property
    def unwind(self):
        return self._unwind

    def _get_unwind(self, level: int):
        unwind = []
        path = ""
        for i in range(level):
            if i != 0:
                path += "."
            path += f"a{i+1}"
            unwind.append({"$unwind": f"${path}"})

        return unwind

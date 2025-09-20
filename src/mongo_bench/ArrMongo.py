from pymongo.collection import Collection
from src.mongo_bench.BaseMongo import BaseMongo

class ArrMongo(BaseMongo):
    def __init__( self , name: str , coll: Collection , level: int) -> None:
        super().__init__(name, coll)
        self.level = level


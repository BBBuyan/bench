from src.base_types import Flat
from pymongo.collection import Collection

class FlatMongo(Flat):
    def __init__(self, coll: Collection) -> None:
        super().__init__()

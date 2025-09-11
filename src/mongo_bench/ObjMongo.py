from src.base_types import Obj

class ObjMongo(Obj):
    def __init__(self, level: int, coll) -> None:
        super().__init__(level)

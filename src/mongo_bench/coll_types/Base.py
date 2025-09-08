from pymongo.collection import Collection

class Base:
    where_clause={}
    sub_path=""
    vol_path=""
    num_path=""
    app_path=""

    def __init__(self, coll: Collection) -> None:
        self.coll = coll


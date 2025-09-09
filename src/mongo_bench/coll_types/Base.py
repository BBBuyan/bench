from pymongo.collection import Collection

class Base:
    def __init__(self, coll: Collection) -> None:
        self.coll = coll
        self.name = coll.name

        self._vol_field = "total_volume_bytes"
        self._app_field = "app"
        self._num_field = "number_of_records"
        self._sub_field = "subscribers"

        self.sub_path=""
        self.vol_path=""
        self.num_path=""
        self.app_path=""
        self.where_clause={}
        self.batch_limit = 0

    def create_index(self):
        self.coll.create_index(self.sub_path)

    def delete_index(self):
        self.coll.drop_indexes()

    def explain(self):
        print(f"{self.name}")
        print(f"sub_path: {self.sub_path}")
        print(f"vol_path: {self.vol_path}")
        print(f"app_path: {self.app_path}")
        print(f"num_path: {self.num_path}")

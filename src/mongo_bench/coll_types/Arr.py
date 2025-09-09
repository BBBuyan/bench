from coll_types.Base import Base
from pymongo.collection import Collection

class Arr(Base):
    def __init__(self, coll: Collection, level: int) -> None:
        super().__init__(coll)
        all_levels = ["a1","a2","a3","a4","a5","a6","a7","a8"]
        self.level = level
        self.levels = all_levels[:(level)]

        self.vol_path = ".".join(self.levels) + "." + self._vol_field
        self.num_path = ".".join(self.levels) + "." + self._num_field
        self.sub_path = ".".join(self.levels) + "." + self._sub_field
        self.app_path = ".".join(self.levels) + "." + self._app_field

        self.unwind = self._build_unwind()
        self.batch_limit = 1000

    def _build_unwind(self):
        unwind =[]
        path = ""
        for i in range(self.level):
            if i != 0:
                path += "."
            path += f"a{i+1}"
            unwind.append({"$unwind": f"{path}"})

        return unwind

    def explain(self):
        print(f"{self.name}")
        print(f"sub_path: {self.sub_path}")
        print(f"vol_path: {self.vol_path}")
        print(f"app_path: {self.app_path}")
        print(f"num_path: {self.num_path}")
        print(f"unwind  : {self.unwind}")

from .BasePost import BasePost
from src.post.arr_queries import read


class ArrPost(BasePost):

    def __init__(self, level: int) -> None:
        super().__init__(f"arr{level}")

        all_levels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
        self.level = level
        self.levels = all_levels[:(level)]

        self.assign_log_threshold = 1000

        self.path = str.join(",", self.levels)
        self.model_path = self.path +"," + self._model_field
        self.error_path = self.path + "," + self._error_field
        self.storage_path = self.path + "," + self._storage_field
        self.temp_path = self.path + "," + self._temp_field
        self.uptime_path = self.path + "," + self._uptime_field
        self.app_path = self.path + "," + self._app_field

        self.description_path = self.path + "," + self._description_field
        self.info_path = self.path + "," + self._info_field

        self.max_docs = 10_000
        self.fetch_limit = 500

        self.coll_type = "arr"
        self.read_query = read[self.level]


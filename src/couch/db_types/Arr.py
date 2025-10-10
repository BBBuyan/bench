from .Base import Base
from random import randint

class Arr(Base):
    def __init__(self, level: int) -> None:
        super().__init__(f"arr{level}")

        all_levels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
        self.level = level
        self.levels = all_levels[:(level)]

        self.max_offset = 9500
        self.assign_log_threshold = 1000
        self.batch_limit = 100

        self.path = str.join(".", self.levels)
        self.memory_path = self.path + f".{self._memory_field}"
        self.error_path = self.path + f".{self._error_field}"
        self.storage_path = self.path + f".{self._storage_field}"
        self.temp_path = self.path + f".{self._temp_field}"
        self.uptime_path = self.path + f".{self._uptime_field}"
        self.app_path = self.path + f".{self._app_field}"
        self.description_path = self.path + f".{self._description_field}"
        self.info_path = self.path + f".{self._info_field}"

        self.max_docs = 10_000
        self.average_map_func = self._generate_emit()

        self.coll_type = "arr"

    def get_error_query(self):
        nest: dict = {
            self._error_field: randint(0,9999)
        }
        reverse = list(reversed(self.levels))
        for r in reverse:
            nest = {
                r: {
                    "$elemMatch": nest
                }
            }
        query = {
            "selector": nest
        }

        return query

    def _generate_emit(self):
        reverse = list(reversed(self.levels))
        emit = f"emit({reverse[0]}.{self._error_field}, {reverse[0]}.{self._error_field})"

        for i in range(len(reverse)-1):
            emit = f"{reverse[i+1]}.{reverse[i]}.forEach(function ({reverse[i]}) {{ {emit} }})"

        emit = f"function (doc) {{ doc.{reverse[-1]}.forEach(function ({reverse[-1]}) {{ {emit} }} )  }}"

        return emit

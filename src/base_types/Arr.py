from .Base import Base
from random import choice

class Arr(Base):
    def __init__(self, level: int) -> None:
        super().__init__(f"arr{level}")

        all_levels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
        self.level = level
        self.levels = all_levels[:(level)]

        self.assign_log_threshold = 1000

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
        self.fetch_limit = 500

    def add_field(
            self
            , editing_data: dict
            , inputs: list[str]
            , field_name: str
            , current_level: int = 0
    ):
        if current_level > self.level:
            raise Exception("Max level in Arr exceeded")
        key = self.levels[current_level]
        for item in editing_data.get(key, []):
            if current_level == self.level - 1:
                item[field_name] = choice(inputs)
            else:
                self.add_field(
                    item
                    , inputs
                    , field_name
                    , current_level + 1
                )



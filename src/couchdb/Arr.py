from Base import Base
from random import randint

class Arr(Base):
    levels: list[str] = []

    device_map = {
        1: "a1.device",
        2: "a1.a2.device",
        4: "a1.a2.a3.a4.device",
        8: "a1.a2.a3.a4.a5.a6.a7.a8.device",
    }

    def __init__(self, level: int) -> None:
        all_levels = ["a8", "a7", "a6", "a5", "a4", "a3", "a2", "a1"]
        self.level = level

        self.name = f"arr{level}"
        self.url = self.base_url + self.name + "/"
        self.max_offset = 9500

        self.device_path = self.device_map[level]
        self.levels = all_levels[(8-level):]
        self.group_map_func = self._generate_group_map_func()
        self.average_map_func = self._generate_average_map_func()

    def get_device_query(self):
        new_id = randint(0, 9999)
        nest: dict = {
            "device": new_id
        }
        for level in self.levels:
            nest = { 
                level: {
                    "$elemMatch": nest
                }
            }

        query: dict = {
            "selector": nest
        }

        return query

    def _generate_group_map_func(self):
        depth = len(self.levels)
        base = f"emit({self.levels[0]}.subscribers, null)"

        for i in range(depth-1):
            base = f"{self.levels[i+1]}.{self.levels[i]}.forEach(function({self.levels[i]}) {{ {base} }}) "

        base = f"function (doc) {{ doc.{self.levels[-1]}.forEach( function({self.levels[-1]}) {{ {base} }} )}}"

        return base

    def _generate_average_map_func(self):
        depth = len(self.levels)
        base = f"emit({self.levels[0]}.subscribers, {self.levels[0]}.total_volume_bytes)"

        for i in range(depth - 1):
            base = f"{self.levels[i+1]}.{self.levels[i]}.forEach(function({self.levels[i]}) {{ {base} }}) "


        base = f"function (doc) {{ doc.{self.levels[-1]}.forEach( function({self.levels[-1]}) {{ {base} }} )}}"

        return base

from db_types.Base import Base
from random import choice

class Flat(Base):
    name = "flat"

    def __init__(self) -> None:
        self.name = "flat"
        self.url = self.base_url + self.name + "/"
        self.max_offset = 999500
        self.assign_log_threshold = 100000

        self.subscribers_path = "subscribers"
        self.volume_path = "total_volume_bytes"
        self.device_path = "device"

        self.group_map_func = "function(doc) { if(doc.subscribers !== undefined) emit(doc.subscribers, null)}"
        self.average_map_func = "function(doc) { if(doc.total_volume_bytes !== undefined) emit(doc.subscribers, doc.total_volume_bytes)}"

    def add_description(self, descriptions: list[str], data: dict):
        data["description"] = choice(descriptions)


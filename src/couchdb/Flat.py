from Base import Base
from random import randint

class Flat(Base):
    name = "flat"

    def __init__(self) -> None:
        self.name = "flat"
        self.url = self.base_url + self.name + "/"
        self.max_offset = 999500

        self.subscribers_path = "subscribers"
        self.volume_path = "total_volume_bytes"
        self.update_path = "device"
        self.device_path = "device"

        self.group_map_func = "function(doc) { if(doc.subscribers !== undefined) emit(doc.subscribers, null)}"
        self.average_map_func = "function(doc) { if(doc.total_volume_bytes !== undefined) emit(doc.subscribers, doc.total_volume_bytes)}"

    def update_innermost_num_of_records(self, data: dict):
        data["number_of_records"] = randint(0,999)

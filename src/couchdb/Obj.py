from Base import Base

class Obj(Base):
    subscribers_map = {
        1: "l1.subscribers",
        2: "l1.l2.subscribers",
        4: "l1.l2.l3.l4.subscribers",
        8: "l1.l2.l3.l4.l5.l6.l7.l8.subscribers",
    }
    device_map = {
        1: "l1.device",
        2: "l1.l2.device",
        4: "l1.l2.l3.l4.device",
        8: "l1.l2.l3.l4.l5.l6.l7.l8.device",
    }
    volume_map = {
        1: "l1.total_volume_bytes",
        2: "l1.l2.total_volume_bytes",
        4: "l1.l2.l3.l4.total_volume_bytes",
        8: "l1.l2.l3.l4.l5.l6.l7.l8.total_volume_bytes",
    }

    def __init__(self, level: int) -> None:
        self.name = f"obj{level}"
        self.url = self.base_url + self.name + "/"
        self.max_offset = 999500

        self.device_path = self.device_map[level]
        self.update_path = "l1"
        self.subscribers_path = self.subscribers_map[level]
        self.volume_path = self.volume_map[level]

        self.group_map_func = f"function (doc) {{ if(doc.{self.subscribers_path} !== undefined) emit(doc.{self.subscribers_path}, null) }}"
        self.average_map_func = f"function (doc) {{ if(doc.{self.volume_path} !== undefined) emit(doc.{self.subscribers_path}, doc.{self.volume_path})}}"

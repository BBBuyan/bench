from random import randint
from Conn import root_url

class Base:
    def __init__(self) -> None:
        self.base_url = root_url
        self.name=""
        self.url=""
        self.max_offset=0
        self.use_index=False
        self.debug = False
        self.num_of_tries = 10

        self.device_path=""
        self.subscribers_path=""
        self.volume_path=""

        self.group_map_func=""
        self.average_map_func=""

        self.group_reduce="_count"
        self.average_reduce="_stats"

        self.batch_limit = 1000
        self.assign_log_threshold = 0

    def get_device_query(self):
        query: dict = {
            "selector": {
                self.device_path: randint(0,9999)
            },
        }
        if self.use_index:
            query["use_index"] = f"{self.name}-device-index"

        return query

    def get_index_query(self):
        query = {
            "index": {
                "fields": [f"{self.device_path}"]
            },
            "name": f"{self.name}-device-index",
            "type": "json"
        }
        return query

    def update(self, data: dict, new_data: dict):
        data.update(new_data)

    def add_id(self, id: str, data: dict):
        data["_id"] = id

    def add_description(self, descriptions: list[str], data:dict):
        raise NotImplementedError("Subclasses should implement")


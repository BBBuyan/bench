from random import randint
from Conn import root_url

class Base:
    base_url = root_url
    name=""
    url=""
    max_offset=0
    use_index=False

    device_path=""
    subscribers_path=""
    volume_path=""

    group_map_func=""
    average_map_func=""

    group_reduce="_count"
    average_reduce="_stats"

    def get_device_query(self):
        new_id = randint(0, 9999)
        query: dict = {
            "selector": {
                self.device_path: new_id
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

    def update_innermost_device(self, data: dict):
        raise NotImplementedError("must be implemented in subclasses")


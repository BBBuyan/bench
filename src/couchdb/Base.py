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
            "ddoc": "custom-indexes",
            "name": f"{self.name}-device-index",
            "type": "json"
        }
        return query

    def update_innermost_num_of_records(self, data: dict):
        raise NotImplementedError("must be implemented in subclasses")


from random import randint

class Base:
    base_url = "http://admin:secret@192.168.2.87:5984/"
    name=""
    url=""
    max_offset=0
    use_index=False

    device_path=""
    update_path=""
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

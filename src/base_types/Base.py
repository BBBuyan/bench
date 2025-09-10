
class Base:
    def __init__(self, name: str) -> None:
        self.database_name=""
        self.name = name
        self._vol_field = "total_volume_bytes"
        self._app_field = "app"
        self._num_field = "number_of_records"
        self._sub_field = "subscribers"
        self._description_field = "description"
        self.assign_log_threshold = 100_000

    def add_description(self, descriptions: list[str], data:dict):
        print(self.name)
        raise NotImplementedError("Subclasses should implement")

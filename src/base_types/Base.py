
class Base:
    def __init__(self, name: str) -> None:
        self.name= name
        self._vol_field = "total_volume_bytes"
        self._app_field = "app"
        self._num_field = "number_of_records"
        self._sub_field = "subscribers"
        self._description_field = "description"

    def add_description(self, descriptions: list[str], data:dict):
        raise NotImplementedError("Subclasses should implement")

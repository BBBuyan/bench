
class Base:
    is_debug = False
    def __init__(self, name: str) -> None:
        self.database_name=""
        self.name = name

        self._device_field = "device"
        self._vol_field = "total_volume_bytes"
        self._app_field = "app"
        self._num_field = "number_of_records"
        self._sub_field = "subscribers"
        self._description_field = "description"

        self.device_path = ""
        self.vol_path = ""
        self.app_path = ""
        self.num_path = ""
        self.sub_path = ""
        self.description_path = ""

        self.assign_log_threshold = 100_000

    def add_field(self, editing_data: dict, inputs: list[str], field_name: str):
        raise NotImplementedError("Subclasses should implement")

from .Base import Base
from random import choice

class Flat(Base):
    def __init__(self) -> None:
        super().__init__("flat")

        self.vol_path = self._vol_field
        self.app_path = self._app_field
        self.num_path = self._num_field
        self.sub_path = self._sub_field
        self.description_path = self._description_field

    def add_field(self, editing_data: dict, inputs: list[str], field_name: str):
        editing_data[field_name] = choice(inputs)

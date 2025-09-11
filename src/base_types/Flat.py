from .Base import Base
from random import choice

class Flat(Base):
    def __init__(self) -> None:
        super().__init__("flat")

    def add_description(self, descriptions: list[str], data: dict):
        data["description"] = choice(descriptions)

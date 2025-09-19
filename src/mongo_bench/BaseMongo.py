from src.base_types import Base

class BaseMongo(Base):
    def __init__(self, name: str) -> None:
        super().__init__(name)

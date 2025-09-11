from src.base_types import Base

class BaseMongo(Base):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.sub_path=""
        self.vol_path=""
        self.num_path=""
        self.app_path=""

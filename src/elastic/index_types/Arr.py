from index_types.Base import Base

class Arr(Base):
    def __init__(self, level: int) -> None:
        super().__init__(f"arr{level}")

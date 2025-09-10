from index_types.Base import Base

class Obj(Base):
    def __init__(self, level: int) -> None:
        super().__init__(f"obj{level}")

from conn import url

class Base:
    def __init__(self, name: str) -> None:
        self.name = name
        self.url = url + self.name

from random import randint

class Base:
    base_url = "http://admin:secret@192.168.2.87:5984/"
    subscribers_map = {}
    name=""
    update_path=""
    url=""

    def get_subscribers_query(self):
        sub_id = randint(0, 9999)
        return {
            "selector": {
                self.subscribers_map[self.name]: sub_id
            }
        }

    def get_group_query(self):
        sub_id = randint(0, 9999)
        query = {
            "selector": {
                self.subscribers_map[self.name]: sub_id
            },
            "sort": [
                { ""}
            ]
        }



class Arr(Base):
    levels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
    levels_cut = {
        "arr1": -7,
        "arr2": -6,
        "arr4": -4,
        "arr8": None,
    }
    update_path = "a1"

    def __init__(self, level: int) -> None:
        self.name = f"arr{level}"
        self.url = self.base_url + self.name + "/"

    def get_subscribers_query(self):
        sub_id = randint(0, 9999)
        nest: dict = {
            "subscribers": sub_id
        }

        cut = self.levels_cut[self.name]
        nest_levels = self.levels[:cut]

        for level in reversed(nest_levels):
            nest = { 
                level: {
                    "$elemMatch": nest
                }
            }

        result = {
            "selector": nest
        }
        return result


class Flat(Base):
    update_path = "subscribers"
    subscribers_map = {
        "flat": "subscribers",
    }

    def __init__(self) -> None:
        self.name = "flat"
        self.url = self.base_url + self.name + "/"


class Obj(Base):
    update_path = "l1"
    subscribers_map = {
        "obj1": "l1.subscribers",
        "obj2": "l1.l2.subscribers",
        "obj4": "l1.l2.l3.l4.subscribers",
        "obj8": "l1.l2.l3.l4.l5.l6.l7.l8.subscribers",
    }

    def __init__(self, level: int) -> None:
        self.name = f"obj{level}"
        self.url = self.base_url + self.name + "/"

import requests
from ..db_types import Base
from ..Databases import all_dbs, arr_list, obj_list, flat_list

def create_databases(db: Base):
    res = requests.put(db.url)
    print(res.text)

if __name__ == "__main__":
    for db in all_dbs:
        create_databases(db)


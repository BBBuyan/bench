import requests
from ..db_types import Base
from ..Databases import all_dbs, arr_list, obj_list, flat_list

def create_databases(db: Base):
    url = db.base_url + db.name + "?q=8&n=3"
    res = requests.put(url)
    print(res.text)

if __name__ == "__main__":
    for db in all_dbs:
        create_databases(db)


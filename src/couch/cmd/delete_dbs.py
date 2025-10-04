from ..db_types.Base import Base
import requests
from ..Databases import all_dbs, arr_list, obj_list, flat_list

def delete_database(db: Base):
    res = requests.delete(db.url)
    print(res.text)

if __name__ == "__main__":
    for db in all_dbs:
        delete_database(db)

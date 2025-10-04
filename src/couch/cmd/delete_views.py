from ..db_types.Base import Base
from ..Databases import all_dbs, arr_list, obj_list, flat_list
import requests

def delete_analytic_views(op_type: Base):
    fetch_url = op_type.url + "_design_docs"
    delete_url = op_type.url + "_design/analytic?rev="

    res = requests.get(fetch_url)
    data = res.json()
    docs = data["rows"]

    for doc in docs:
        rev = doc["value"]["rev"]
        if rev is None:
            continue

        del_res = requests.delete(delete_url+rev)
        print(del_res.text)

if __name__ == "__main__":
    for db in all_dbs:
        delete_analytic_views(db)

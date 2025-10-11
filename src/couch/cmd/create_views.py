from ..db_types.Base import Base
from ..Databases import all_dbs, arr_list, obj_list, flat_list
import requests

def build_avg_view_doc(op_type: Base):
    doc = {
        "id": "_design/avg",
        "views": {
            "average": {
                "map": op_type.average_map_func,
                "reduce": "_stats"
            }
        }
    }
    return doc

def create_avg_views(op_type: Base):
    url = op_type.url +"_design/avg"
    doc = build_avg_view_doc(op_type)
    res = requests.put(url, json=doc)
    print(res.text)

if __name__ == "__main__":
    for db in all_dbs:
        create_avg_views(db)

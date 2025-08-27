from operations import time_read, time_update
import requests
from pprint import pprint
import helper
import op_types 


query = {
    "selector": {
        "a1": {
            "$elemMatch":
                {
                    "subscribers": 6270
            }
        }
    },
    "limit": 2
}

url= "http://admin:secret@192.168.2.87:5984/arr1/"

# res = requests.post(url, json=query)
# data = res.json()
# docs = data["docs"]
# for doc in docs:
#     pprint(doc["a1"])

# pprint(helper.get_updated_arr(url))
test = op_types.Flat()

# time_update(test)
# print(helper.fetch_random_without_meta(test.url))
helper.create_flat_design_doc(test)

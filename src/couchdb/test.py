# from json import loads
# import requests
# from couchdb import Server
#
# couch_url = "http://admin:secret@192.168.2.87:5984"
#
# def main():
#     couch = Server(url=couch_url)
#     couch.create("flat")
#
# main()

from requests import post, request
import conn
from pprint import pprint

def testing():
    print("start")
    url = conn.url_map[CollType.obj1]+ "_find/"

    # query = {
    #     "selector": {
    #         "a1":{
    #             "$elemMatch": {
    #                 "a2": {
    #                     "$elemMatch": {
    #                         "device": 10
    #                     }
    #                 }
    #             }
    #         }
    #     },
    #     "limit": 3
    # }
    #
    query = {
        "selector":
            {
            "l1.device": 50
        }
    }
    res = post(url, json=query)
    data = res.json()
    docs = data["docs"]
    pprint(docs)


# testing()

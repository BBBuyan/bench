from json import loads
import requests
from couchdb import Server

couch_url = "http://admin:secret@192.168.2.87:5984"

def main():
    couch = Server(url=couch_url)
    couch.create("flat")


main()


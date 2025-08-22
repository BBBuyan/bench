from couchdb import Server 


def create_databases():
    couch_url = "http://admin:secret@192.168.2.87:5984"
    couch = Server(url=couch_url)
    couch.create("flat")

    couch.create("arr1")
    couch.create("arr2")
    couch.create("arr4")
    couch.create("arr8")

    couch.create("obj1")
    couch.create("obj2")
    couch.create("obj4")
    couch.create("obj8")


create_databases()


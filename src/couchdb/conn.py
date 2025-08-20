from couchdb import Server

url_str = "http://192.168.2.87:5984"
couch = Server(url=url_str)

flat = couch["flat"]

arr1 = couch["arr1"]
arr2 = couch["arr2"]
arr4 = couch["arr4"]
arr8 = couch["arr8"]

obj1 = couch["obj1"]
obj2 = couch["obj2"]
obj4 = couch["obj4"]
obj8 = couch["obj8"]

flat_list = [flat]
obj_list = [obj1, obj2, obj4, obj8]
arr_list = [arr1, arr2, arr4, arr8]

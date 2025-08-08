from pymongo import MongoClient
from pymongo.collection import Collection

connectionString ="mongodb://192.168.2.87:27017"

cl = MongoClient(connectionString)
db = cl["deep"]

flat: list[Collection]= [db.flat]
obj_colls: list[Collection] = [db.obj1, db.obj2, db.obj4, db.obj8]
arr_colls: list[Collection] = [db.arr1, db.arr2, db.arr4, db.arr8]

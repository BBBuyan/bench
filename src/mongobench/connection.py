from pymongo import MongoClient

cl = MongoClient("mongodb://192.168.2.87:27017")
db = cl["deep"]

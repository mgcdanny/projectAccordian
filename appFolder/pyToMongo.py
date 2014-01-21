from pymongo import MongoClient

client = MongoClient()

db = client["mydb"]

collection = db["prjc"]

post = {"test":1234}

collection.insert(post)





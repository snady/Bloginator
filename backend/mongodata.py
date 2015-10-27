import csv, pymongo, random
from pymongo import MongoClient

client = MongoClient()
db_name = "data.db"
userCollection = "users"
postCollection = "posts"

db = client[db_name]
users = db.userCollection
posts = db.postCollection

def addMember(user, password):
    if users.find_one({"username": user}) == None:
        users.insert_one({"username": user, "password": password})

def check():
    for r in users.find():
        print r["username"]

def filterUname(user):
    return users.find_one({"username": user}) == None

def checkPass(user, password):
    return users.find_one({"username": user}) == user and users.find_one({"username": user})["password"] = password
        

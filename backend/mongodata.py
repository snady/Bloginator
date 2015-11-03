import csv, pymongo, random
from pymongo import MongoClient
import datetime

conn = MongoClient()
db = conn['data']
users = db['members']

# USERS

def addMember(user, password):
    if users.find_one({"name": user}) == None:
        users.insert_one({"name": user, "password": password, "posts": []})

def check():
    for r in users.find():
        print r

def filterUname(user):
    return users.find_one({"name": user}) == None

def checkPass(user, password):
    return users.find_one({"name": user}) != None and users.find_one({"username": user})["password"] == password


addMember("myrseeer", "blue")


# POSTS/COMMENTS

def showPosts():
    for r in posts.find():
        print r

def addPost(user, titl, txt, idd):
    users.update_one({'name': user}, {'$push': {'posts': {'title': titl, 'text': txt, 'created':str(datetime.datetime.now()), 'id':idd, 'comments':[{}]}}}, upsert = False)

def findPost(idd):
    return users.find_one({'id': idd})
    
def removePost(user, idd):
    users.update_one({'name': user}, {'$pull': {'posts': {'id': idd}}})

def makeID():
    num = random.randint(100,999)
    for x in posts.find():
        if x['id'] == num:
            makeID()
        else:
            return num
    return num

def addComment(user, post, info):
    users.update_one({'id': post}, {'$push': {'comments': {'user': user, 'info': info}}}, upsert = False)
        

#addPost("myrseeer", "shi", "h", 2)
#removePost("myrseeer", 1)

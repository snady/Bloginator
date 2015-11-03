import csv, pymongo, random
from pymongo import MongoClient

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

def addPost(user, titl, txt):
    users.update_one({'name': user}, {'$push': {'posts': {'title': titl, 'text': txt, 'comments':[{}]}}}, upsert = False)
    #users.update({'name': user}, {'posts': post, 'title': title, 'user': user, 'id': makeID(), 'comments': []})

def findPost(id):
    return posts.find_one({'id': id})
    
def removePost(pi):
    posts.delete_one({'id': pi})

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
        

addPost("myrseeer", "hi", "my past")

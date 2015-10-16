import os, sqlite3, csv, random

db_name = "postData.db"

def start():

     if (not os.path.exists(db_name)):

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        q = """create table posts (content text, title text, user_id integer, post_id integer);"""
        c.execute(q)

        q = """insert into posts values ("Hello world", "first", 200, 100);"""
        c.execute(q)

        conn.commit()

def addPost(post, title, user):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    id = makeID()

    q = """insert into posts values ("%s", "%s", "%i", "%i")"""
    q = q%(post, title, user, id)

    c.execute(q)

    conn.commit()

def makeID():

     conn = sqlite3.connect(db_name)
     c = conn.cursor()

     q = """select post_id from posts"""
     num = random.randint(100,999)

     for x in c.execute(q):
          if x == num:
               makeID()
          else:
               return num

def removePost(pi):
     
     conn = sqlite3.connect(db_name)
     c = conn.cursor()

     q = """delete row from posts where post_id = %i"""
     q = q%(pi)

     c.execute(q)

     conn.commit()

start()

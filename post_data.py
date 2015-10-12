import os, sqlite3, csv, random

db_name = "postData.db"

def start():

     if (not os.path.exists(db_name)):

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        q = """create table posts (content text, user_id integer, post_id integ\
er);"""
        c.execute(q)

        q = """insert into posts values ("Hello world", 200, 1);"""
        c.execute(q)

        conn.commit()

def addPost():

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    q = """insert into posts values ("%s", "%i", "%i")"""

    c.execute(q)

    conn.commit()

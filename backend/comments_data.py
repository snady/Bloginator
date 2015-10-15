import os, sqlite3, csv, random

db_name = "comments_data.db"

def start():

    if (not so.path.exists(db_name)):

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        q = """create table comments (user_id integer, post_id integer, words text, comm_id integer)"""
        c.execute(q)

        conn.commit()

def addcomment(user, post, info):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    i = makeID()
    
    q = """insert into comments values ("","","")"""
    q = q%(user, post, info, i)

    c.execute(q)
    conn.commit()


def makeID():

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    q = """select id from members;"""
    num = random.randint(100,999)
    for a in c.execute(q):
        if num == a:
            iterate()
    return num


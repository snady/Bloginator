import os, sqlite3, csv, random

db_name = "comments_data.db"
pdb_name = "postData.db"
mdb_name = "membersData.db"

def start():

    if (not os.path.exists(db_name)):

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        q = """create table comments (user_id integer, post_id integer, words text, comm_id integer)"""
        c.execute(q)

        q = """insert into comments values (700, 100, "nice post", 123)"""
        
        conn.commit()

def addcomment(user, post, info):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    i = makeID()
    
    q = """insert into comments values ("%i","%i","%s", "%i")"""
    q = q%(user, post, info, i)

    c.execute(q)
    conn.commit()


def makeID():

    conn = sqlite3.connect(mdb_name)
    c = conn.cursor()

    q = """select id from members;"""
    num = random.randint(100,999)
    for a in c.execute(q):
        if num == a:
            iterate()
    return num

def findPost(num):

    ret = []
    
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    q = """select words from comments where post_id = %i;"""
    
    q = q%(int(num))

    print q

    for a in c.execute(q):
        ret.append(a[0])

    return ret
    
    
start()

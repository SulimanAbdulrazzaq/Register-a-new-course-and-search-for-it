import sqlite3


def create_table():
    conn = sqlite3.connect("courses.db")
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE IF NOT EXISTS courses( 
                id TEXT PRIMARY KEY,
                name TEXT,
                duration TEXT,
                format TEXT,
                language TEXT,
                price INTEGER     
    )''')
    conn.commit()
    conn.close()
def insert(id,name,duration,format,language,price):
    conn = sqlite3.connect("courses.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO courses (id,name,duration,format,language,price) VALUES(?,?,?,?,?,?)",(id,name,duration,format,language,price))
    conn.commit()
    conn.close()
def search(query):
    conn = sqlite3.connect("courses.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses WHERE id = ?",(query,))
    row = cur.fetchone()
    conn.close()
    return row

def fetchids():
    conn = sqlite3.connect("courses.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM courses")
    ids = cur.fetchall()
    conn.close()
    return [i[0] for i in ids]
def id_exists(id):
    conn = sqlite3.connect("courses.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM courses WHERE id=?",(id,))
    result = cur.fetchone()
    return result[0]>0
create_table()
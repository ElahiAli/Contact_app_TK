import sqlite3

#user table

def connect_user():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username text NOT NULL,password INTEGER NOT NULL)")
    conn.commit()
    conn.close()

def insert_user(username,password):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUEs (NULL,?,?)", (username,password))
    conn.commit()
    conn.close()



def search_user(username,password):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    rows = cur.fetchall()
    conn.close()
    return rows



#table contacts

def connect():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY,username text  NOT NULL,name text  NOT NULL,lastname text  NOT NULL,phonenumber INTEGER  NOT NULL,FOREIGN KEY(username) REFERENCES users(username) )")
    conn.commit()
    conn.close()


def insert(username,name,lastname,phonenumber):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO contact VALUEs (NULL,?,?,?,?)", (username,name,lastname,phonenumber))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(username="",name="",lastname="",phonenumber=""):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact WHERE username=? AND name=? OR lastname=? OR phonenumber=?",(username,name,lastname,phonenumber))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contact WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,username,name,lastname,phonenumber):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("UPDATE contact SET username=?,name=?,lastname=?,phonenumber=? WHERE id=?",(username,name,lastname,phonenumber,id))
    conn.commit()
    conn.close()


connect_user()
connect()



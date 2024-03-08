import sqlite3
conn = sqlite3.connect('Quizbowl.db')
cr = conn.cursor()

cr.execute("SELECT name FROM sqlite_master WHERE  type='table';")
print("Table names from database file:\n",cr.fetchall(),"\n")


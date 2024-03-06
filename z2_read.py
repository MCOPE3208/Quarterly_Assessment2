import sqlite3
conn = sqlite3.connect('Quizbowl.db')
cr = conn.cursor()

cr.execute("SELECT name FROM sqlite_master WHERE  type='table';")
print("Table names from database file:\n",cr.fetchall(),"\n")

cr.execute("PRAGMA table_info({});".format("Taxation"))
columns = cr.fetchall()

if columns:
    column_names = [column[1] for column in columns]
    print(f"Column Names: {', '.join(column_names)}","\n")
else:
    print(f"No columns found in the table {"Taxation"}.")

cr.execute("SELECT * FROM Taxation")
print("Questions from Taxation table:\n",cr.fetchall(),"\n")
import sqlite3
conn = sqlite3.connect('Quizbowl.db')
cr = conn.cursor()

cr.execute("SELECT name FROM sqlite_master WHERE  type='table';")
print(cr.fetchall())

cr.execute("PRAGMA table_info({});".format("Taxation"))
columns = cr.fetchall()

if columns:
    column_names = [column[1] for column in columns]
    print(f"Column Names: {', '.join(column_names)}")
else:
    print(f"No columns found in the table {"Taxation"}.")

cr.execute("SELECT * FROM Taxation")
print(cr.fetchall())
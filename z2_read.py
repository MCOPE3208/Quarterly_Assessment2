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

#to view the questions in a specific table put the name in after the word FROM in the next line of code
cr.execute("SELECT * FROM BusinessAppdev")
print("Questions from table:\n",cr.fetchall(),"\n")
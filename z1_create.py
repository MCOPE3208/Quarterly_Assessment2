import sqlite3
conn = sqlite3.connect('Quizbowl.db')
cr = conn.cursor()

cr.execute("""
           CREATE TABLE IF NOT EXISTS QuestAns (
           id INTEGER PRIMARY KEY,
           question TEXT,
           answer TEXT)
           """)

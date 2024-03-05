import sqlite3
conn = sqlite3.connect('Quizbowl.db')
cr = conn.cursor()

# Create the 'Taxation' table if it doesn't exist
cr.execute('''
    CREATE TABLE IF NOT EXISTS Taxation (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct_answer INTEGER
    );
''')

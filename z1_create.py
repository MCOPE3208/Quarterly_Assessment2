import sqlite3
conn = sqlite3.connect('Quizbowl.db')
cr = conn.cursor()

#Create 'Taxation' table 
cr.execute('''
    CREATE TABLE IF NOT EXISTS Taxation (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct_answer TEXT
    );
''')
def add_taxQ(question, option1, option2, option3, option4, correct_answer):
    cr.execute("""
        INSERT INTO Taxation (question, option1, option2, option3, option4, correct_answer)
        VALUES (?,?,?,?,?,?)""",(question, option1, option2, option3, option4, correct_answer)
    ) 
    conn.commit()
    print("Question added :)")

#this is the template to add more questions to tax 
    
#add_taxQ("What is the deadline for filing individual federal income tax returns?", "A) March 15th", "B) April 1st", "C) April 15th", "D) May 1st", "C")


#Create 'Finance' table 
cr.execute('''
    CREATE TABLE IF NOT EXISTS Finance (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct_answer TEXT
    );
''')

def add_finQ(question, option1, option2, option3, option4, correct_answer):
    cr.execute("""
        INSERT INTO Finance (question, option1, option2, option3, option4, correct_answer)
        VALUES (?,?,?,?,?,?)""",(question, option1, option2, option3, option4, correct_answer)
    ) 
    conn.commit()
    print("Question added :)")   

#this is the template to add more questions to finance 

#add_finQ("What is the time value of money?", "A) The current value of money", "B) The future value of money", "C) The idea that money available today is worth more than the same amount in the future", "D) The concept that money will always have the same value", "C")

    
#Create 'Cost Accounting' table 
cr.execute('''
    CREATE TABLE IF NOT EXISTS CostAccounting (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct_answer TEXT
    );
''')

def add_costQ(question, option1, option2, option3, option4, correct_answer):
    cr.execute("""
        INSERT INTO CostAccounting (question, option1, option2, option3, option4, correct_answer)
        VALUES (?,?,?,?,?,?)""",(question, option1, option2, option3, option4, correct_answer)
    ) 
    conn.commit()
    print("Question added :)") 

#this is the template to add more questions to Cost Accounting 

#add_costQ("What is the definition of direct costs in cost accounting?", "A) Costs that can be traced directly to a specific product or service", "B) Overhead costs", "C) Indirect labor costs", "D) Fixed costs", "A")


#Create 'Financial Accounting' table 
cr.execute('''
    CREATE TABLE IF NOT EXISTS FinancialAccounting (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct_answer TEXT
    );
''')

def add_finanQ(question, option1, option2, option3, option4, correct_answer):
    cr.execute("""
        INSERT INTO FinancialAccounting (question, option1, option2, option3, option4, correct_answer)
        VALUES (?,?,?,?,?,?)""",(question, option1, option2, option3, option4, correct_answer)
    ) 
    conn.commit()
    print("Question added :)")

#this is the template to add more questions to Financial Accounting 

#add_finanQ("What is the purpose of the income statement in financial accounting?", "A) To show the financial position of a company at a specific point in time.", "B) To report the changes in a company's financial position over a period of time.", "C) To detail a company's assets, liabilities, and equity.", "D) To calculate the return on investment for shareholders.", "B")

    
#Create 'Business Analytics' table 
cr.execute('''
    CREATE TABLE IF NOT EXISTS BusinessAnalytics (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct_answer TEXT
    );
''')

def add_busanaQ(question, option1, option2, option3, option4, correct_answer):
    cr.execute("""
        INSERT INTO BusinessAnalytics (question, option1, option2, option3, option4, correct_answer)
        VALUES (?,?,?,?,?,?)""",(question, option1, option2, option3, option4, correct_answer)
    ) 
    conn.commit()
    print("Question added :)")

#this is the template to add more questions to Business Analytics 

#add_busanaQ("What is descriptive analytics?", "A) Predicting future outcomes based on historical data.", "B) Analyzing current data to understand what has happened.", "C) Identifying patterns and trends in data.", "D) Prescribing actions based on data insights.", "B")

    
cr.execute('''
    CREATE TABLE IF NOT EXISTS BusinessAppDev (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct_answer TEXT
    );
''')

def add_appdevQ(question, option1, option2, option3, option4, correct_answer):
    cr.execute("""
        INSERT INTO BusinessAppDev (question, option1, option2, option3, option4, correct_answer)
        VALUES (?,?,?,?,?,?)""",(question, option1, option2, option3, option4, correct_answer)
    ) 
    conn.commit()
    print("Question added :)")

#this is the template to add more questions to Business App Development 

#add_appdevQ("What does the 'print' function do in Python?", "A) Takes user input", "B) Displays output to the console", "C) Performs mathematical calculations", "D) Defines a variable", "B")
    
    
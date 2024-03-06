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

add_taxQ("What is the deadline for filing individual federal income tax returns?", "A) March 15th", "B) April 1st", "C) April 15th", "D) May 1st", "C")
add_taxQ("What is the purpose of Form W-4 in the context of federal income taxes?", "A) Reporting income", "B) Calculating tax owed", "C) Indicating withholding preferences", "D) Claiming tax credits", "C")
add_taxQ("What is the standard deduction for a single taxpayer in the 2022 tax year?", "A) $10,000", "B) $12,550", "C) $15,000", "D) $20,000", "B")
add_taxQ("Explain the difference between a tax credit and a tax deduction.", "A) Deductions reduce taxable income; credits directly reduce taxes owed.", "B) Deductions directly reduce taxes owed; credits reduce taxable income.", "C) Both deductions and credits reduce taxable income.", "D) Deductions and credits have the same impact on taxes.", "A")
add_taxQ("What is the Social Security tax rate for employees in 2022?", "A) 4.2%", "B) 6.2%", "C) 8.0%", "D) 10.0%", "B")
add_taxQ("What is the Alternative Minimum Tax (AMT), and who is it designed to affect?", "A) A tax on minimum income; affects all taxpayers.", "B) A tax on alternative income; affects low-income individuals.", "C) A parallel tax system; affects high-income individuals and corporations.", "D) A tax credit for alternative energy; affects all taxpayers.", "C")
add_taxQ("How are capital gains taxed at the federal level?", "A) Flat rate regardless of holding period.", "B) Taxed at a higher rate for short-term gains.", "C) Taxed at a higher rate for long-term gains.", "D) Exempt from federal taxes.", "B")
add_taxQ("What is the purpose of IRS Form 1099?", "A) Report income for employees.", "B) Calculate self-employment tax.", "C) Report various types of income.", "D) Claim tax deductions.", "C")
add_taxQ("Explain the concept of 'head of household' filing status.", "A) Unmarried, providing less than half of financial support.", "B) Married with dependents.", "C) Unmarried, providing more than half of financial support for a qualifying dependent.", "D) Single with no dependents.", "C")
add_taxQ("What is the Gift Tax, and how does it relate to federal taxation?", "A) Tax on all gifts, regardless of amount.", "B) Tax on gifts above a certain value; exclusions apply.", "C) Tax on gifts received by individuals.", "D) Tax on gifts, but only for high-income individuals.", "B")
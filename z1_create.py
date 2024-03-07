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

#this is the template to add more questions to tax as well as a list for all the questions that have already been added.

#add_taxQ("What is the deadline for filing individual federal income tax returns?", "A) March 15th", "B) April 1st", "C) April 15th", "D) May 1st", "C")
#add_taxQ("What is the purpose of Form W-4 in the context of federal income taxes?", "A) Reporting income", "B) Calculating tax owed", "C) Indicating withholding preferences", "D) Claiming tax credits", "C")
#add_taxQ("What is the standard deduction for a single taxpayer in the 2022 tax year?", "A) $10,000", "B) $12,550", "C) $15,000", "D) $20,000", "B")
#add_taxQ("Explain the difference between a tax credit and a tax deduction.", "A) Deductions reduce taxable income; credits directly reduce taxes owed.", "B) Deductions directly reduce taxes owed; credits reduce taxable income.", "C) Both deductions and credits reduce taxable income.", "D) Deductions and credits have the same impact on taxes.", "A")
#add_taxQ("What is the Social Security tax rate for employees in 2022?", "A) 4.2%", "B) 6.2%", "C) 8.0%", "D) 10.0%", "B")
#add_taxQ("What is the Alternative Minimum Tax (AMT), and who is it designed to affect?", "A) A tax on minimum income; affects all taxpayers.", "B) A tax on alternative income; affects low-income individuals.", "C) A parallel tax system; affects high-income individuals and corporations.", "D) A tax credit for alternative energy; affects all taxpayers.", "C")
#add_taxQ("How are capital gains taxed at the federal level?", "A) Flat rate regardless of holding period.", "B) Taxed at a higher rate for short-term gains.", "C) Taxed at a higher rate for long-term gains.", "D) Exempt from federal taxes.", "B")
#add_taxQ("What is the purpose of IRS Form 1099?", "A) Report income for employees.", "B) Calculate self-employment tax.", "C) Report various types of income.", "D) Claim tax deductions.", "C")
#add_taxQ("Explain the concept of 'head of household' filing status.", "A) Unmarried, providing less than half of financial support.", "B) Married with dependents.", "C) Unmarried, providing more than half of financial support for a qualifying dependent.", "D) Single with no dependents.", "C")
#add_taxQ("What is the Gift Tax, and how does it relate to federal taxation?", "A) Tax on all gifts, regardless of amount.", "B) Tax on gifts above a certain value; exclusions apply.", "C) Tax on gifts received by individuals.", "D) Tax on gifts, but only for high-income individuals.", "B")
    
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

#this is the template to add more questions to finance as well as a list for all the questions that have already been added.

#add_finQ("What is the time value of money?", "A) The current value of money", "B) The future value of money", "C) The idea that money available today is worth more than the same amount in the future", "D) The concept that money will always have the same value", "C")
#add_finQ("What does ROI stand for?", "A) Return on Investment", "B) Risk of Inflation", "C) Revenue of Interest", "D) Rate of Income", "A")
#add_finQ("What is diversification in investing?", "A) Concentrating investments in a single asset", "B) Spreading investments across different assets to reduce risk", "C) Timing the market for maximum profit", "D) Avoiding investments altogether", "B")
#add_finQ("What is a 401(k)?", "A) A type of loan", "B) A retirement savings plan sponsored by employers", "C) A credit card", "D) A real estate investment", "B")
#add_finQ("What is the purpose of a credit score?", "A) To track your spending habits", "B) To determine your eligibility for loans and credit", "C) To calculate your tax liability", "D) To assess your net worth", "B")
#add_finQ("What is the Federal Reserve?", "A) A government agency that collects taxes", "B) The central banking system of the United States", "C) A stock exchange", "D) A financial advisory firm", "B")
#add_finQ("What is compound interest?", "A) Interest calculated only on the principal amount", "B) Interest calculated on the total amount, including previously earned interest", "C) A one-time interest payment", "D) Interest paid in advance", "B")
#add_finQ("What is a stock dividend?", "A) A cash payment to shareholders", "B) A debt instrument", "C) Additional shares of a company distributed to existing shareholders", "D) A government bond", "C")
#add_finQ("What does the term 'bull market' refer to?", "A) A market with declining prices", "B) A market with stagnant prices", "C) A market characterized by rising prices and optimism", "D) A market with no buyers", "C")
#add_finQ("What is the purpose of a budget?", "A) To restrict spending", "B) To allocate resources and manage finances", "C) To track past expenses", "D) To maximize debt", "B")
    
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

#this is the template to add more questions to Cost Accounting as well as a list for all the questions that have already been added.

#add_costQ("What is the definition of direct costs in cost accounting?", "A) Costs that can be traced directly to a specific product or service", "B) Overhead costs", "C) Indirect labor costs", "D) Fixed costs", "A")
#add_costQ("What is the purpose of a cost allocation in accounting?", "A) To reduce overall costs", "B) To assign indirect costs to specific cost objects", "C) To calculate fixed costs", "D) To increase variable costs", "B")
#add_costQ("What is contribution margin?", "A) The difference between total sales and total expenses", "B) The ratio of variable costs to fixed costs", "C) The difference between variable costs and fixed costs", "D) The ratio of net income to total revenue", "C")
#add_costQ("What is the formula for calculating the break-even point?", "A) Fixed Costs / Contribution Margin", "B) Variable Costs / Contribution Margin", "C) Total Revenue - Total Costs", "D) Fixed Costs / (Selling Price per Unit - Variable Costs per Unit)", "D")
#add_costQ("What is the difference between absorption costing and variable costing?", "A) Absorption costing includes only variable manufacturing costs.", "B) Variable costing includes only variable manufacturing costs.", "C) Absorption costing includes all manufacturing costs.", "D) Variable costing includes all manufacturing costs.", "C")
#add_costQ("What is the significance of the cost of goods sold (COGS) in financial statements?", "A) Represents the total costs incurred by a business", "B) Represents the cost of manufacturing goods that were sold during a specific period", "C) Represents the total revenue earned by a business", "D) Represents the net income of a business", "B")
#add_costQ("What is the difference between direct labor costs and direct material costs?", "A) Direct labor costs include the cost of raw materials.", "B) Direct material costs include the cost of labor.", "C) Direct labor costs are associated with employees who work directly on the product.", "D) Direct material costs are associated with employees who work directly on the product.", "C")
#add_costQ("What is a standard cost in cost accounting?", "A) The actual cost incurred for a product or service.", "B) The budgeted cost for a product or service.", "C) The historical cost of producing a product or service.", "D) The selling price of a product or service.", "B")
#add_costQ("What is the purpose of variance analysis in cost accounting?", "A) To identify the reasons for deviations from the budgeted costs.", "B) To increase the overall costs of production.", "C) To reduce the total costs of production.", "D) To calculate fixed costs.", "A")
#add_costQ("What is the difference between variable costs and fixed costs?", "A) Variable costs remain constant per unit, while fixed costs vary with production volume.", "B) Variable costs vary with production volume, while fixed costs remain constant per unit.", "C) Both variable and fixed costs vary with production volume.", "D) Both variable and fixed costs remain constant per unit.", "B")
    
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

add_finanQ("What is the purpose of the income statement in financial accounting?", "A) To show the financial position of a company at a specific point in time.", "B) To report the changes in a company's financial position over a period of time.", "C) To detail a company's assets, liabilities, and equity.", "D) To calculate the return on investment for shareholders.", "B")
add_finanQ("What is the accounting equation?", "A) Assets = Liabilities - Equity", "B) Assets + Liabilities = Equity", "C) Assets = Liabilities + Equity", "D) Assets - Liabilities = Equity", "C")
add_finanQ("What is the purpose of the balance sheet in financial accounting?", "A) To show the revenues and expenses of a company.", "B) To report the cash flows of a company.", "C) To provide a snapshot of a company's financial position at a specific point in time.", "D) To calculate the net income of a company.", "C")
add_finanQ("What is depreciation?", "A) An increase in the value of an asset.", "B) The process of allocating the cost of an asset over its useful life.", "C) A decrease in the value of an asset.", "D) The cost of purchasing a new asset.", "B")
add_finanQ("How does the matching principle in accounting relate to expenses?", "A) Expenses are recognized when incurred, regardless of when the related revenue is recognized.", "B) Expenses are recognized only when the related revenue is recognized.", "C) Expenses are recognized at the end of the accounting period.", "D) Expenses are recognized only if the company is profitable.", "A")
add_finanQ("What is the purpose of the statement of cash flows?", "A) To show the revenues and expenses of a company.", "B) To report the changes in a company's financial position over a period of time.", "C) To provide details on a company's cash inflows and outflows.", "D) To calculate the return on investment for shareholders.", "C")
add_finanQ("What is the difference between accrued revenue and accrued expenses?", "A) Accrued revenue is money owed by the company, while accrued expenses are amounts the company owes.", "B) Accrued revenue is recognized when earned, while accrued expenses are recognized when paid.", "C) Accrued revenue is recognized when paid, while accrued expenses are recognized when incurred.", "D) Accrued revenue is money owed to the company, while accrued expenses are amounts the company owes.", "A")
add_finanQ("What is the purpose of the statement of retained earnings?", "A) To provide details on a company's cash inflows and outflows.", "B) To show the changes in a company's equity over a period of time.", "C) To report the cost of goods sold.", "D) To calculate the return on investment for shareholders.", "B")
add_finanQ("What is goodwill in financial accounting?", "A) The value of a company's tangible assets.", "B) The excess of the purchase price over the fair value of net assets acquired in a business combination.", "C) The total revenues earned by a company.", "D) The cost of goods sold.", "B")
add_finanQ("What is the role of an auditor in financial accounting?", "A) To prepare financial statements for a company.", "B) To verify the accuracy and completeness of a company's financial statements.", "C) To calculate a company's tax liability.", "D) To manage a company's internal control systems.", "B")
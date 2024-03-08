import sqlite3
import random

# ANSI escape codes for colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def fetch_random_question(cursor, table_name, used_question_ids):
    # Fetch a random question from the specified table that has not been used before
    query = f"SELECT * FROM {table_name} WHERE id NOT IN ({','.join(map(str, used_question_ids))}) ORDER BY RANDOM() LIMIT 1"
    cursor.execute(query)
    question_data = cursor.fetchone()

    if question_data:
        question_id, question, option1, option2, option3, option4, correct_answer = question_data
        used_question_ids.add(question_id)
        return {
            "id": question_id,
            "question": question,
            "options": [option1, option2, option3, option4],
            "correct_answer": correct_answer
        }
    else:
        return None

def display_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def choose_table():
    print("Choose a table:")
    print("1. Taxation")
    print("2. Finance")
    print("3. Cost Accounting")
    print("4. Financial Accounting")
    print("5. Business Analytics")
    print("6. Business App Development")
    # Add more tables as needed

    table_choice = input("Enter the number of the table: ")
    if table_choice == "1":
        return "Taxation"
    if table_choice == "2":
        return "Finance"
    if table_choice == "3":
        return "CostAccounting"
    if table_choice == "4":
        return "FinancialAccounting"
    if table_choice == "5":
        return "BusinessAnalytics"
    if table_choice == "6":
        return "BusinessAppDev"
    # Add more choices for other tables


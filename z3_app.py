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


import sqlite3
from datetime import datetime

DB_PATH = "memory/memory.db"


# ------------------------------------
# Create Database
# ------------------------------------
def create_database():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        customer_name TEXT,

        query TEXT,

        intent TEXT,

        response TEXT,

        timestamp TEXT

    )
    """)

    conn.commit()
    conn.close()


# ------------------------------------
# Save Conversation
# ------------------------------------
def save_conversation(customer_name, query, intent, response):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations
        (customer_name, query, intent, response, timestamp)

        VALUES (?, ?, ?, ?, ?)
        """,
        (
            customer_name,
            query,
            intent,
            response,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()
    conn.close()


# ------------------------------------
# Get Previous Issue
# ------------------------------------
def get_previous_issue(customer_name):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT query

        FROM conversations

        WHERE customer_name = ?

        ORDER BY id DESC

        LIMIT 1
        """,
        (customer_name,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return "No previous support issue found."


# ------------------------------------
# Get Full Conversation History
# ------------------------------------
def get_conversation_history(customer_name):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            query,
            intent,
            response,
            timestamp

        FROM conversations

        WHERE customer_name = ?

        ORDER BY id ASC
        """,
        (customer_name,)
    )

    rows = cursor.fetchall()

    conn.close()

    if not rows:
        return "No previous conversation found."

    history = ""

    for i, row in enumerate(rows, start=1):

        history += f"""
Conversation {i}

Time: {row[3]}

Department: {row[1]}

Customer:
{row[0]}

Response:
{row[2]}

------------------------------------
"""

    return history
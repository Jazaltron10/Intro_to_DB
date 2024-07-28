import mysql.connector
from mysql.connector import Error, errorcode
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

try:
    # Establish connection to MySQL server
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database='alx_book_store'  # Connect directly to the database
    )

    # Check if connection was successful
    if not db.is_connected():
        raise Error("Failed to establish connection to the database.")

    print("Connection established...")
    cursor = db.cursor()

    # # Execute SQL commands from the SQL file
    # with open('task_6.sql', 'r') as file:
    #     sql_script = file.read()

    # # Split the script into individual commands
    # sql_commands = sql_script.split(';')

    # for command in sql_commands:
    #     if command.strip():
    #         cursor.execute(command)
    #         # Fetch all results to clear the cursor
    #         if cursor.with_rows:
    #             results = cursor.fetchall()
    #             for result in results:
    #                 print(result)

    # Commit the transaction to persist changes
    db.commit()
except Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(f"Error: {err}")
finally:
    if db.is_connected():
        cursor.close()
        db.close()
        print("Connection closed.")

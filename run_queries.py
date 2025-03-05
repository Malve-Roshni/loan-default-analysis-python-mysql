import pymysql
from config import db_config

# Establish MySQL connection
conn = pymysql.connect(**db_config)
cursor = conn.cursor()

# Read and execute SQL file
with open("SQL_scripts/create_table.sql", "r") as sql_file:
    sql_commands = sql_file.read().split(";")  # Split queries by ';'

    for command in sql_commands:
        if command.strip():  # Avoid empty statements
            cursor.execute(command)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("SQL queries executed successfully.")

import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',         # e.g., 'localhost' or '127.0.0.1'
    user='root',     # your MySQL username
    password='password', # your MySQL password
    database='bank'  # your database name
)
cursor=connection.cursor()
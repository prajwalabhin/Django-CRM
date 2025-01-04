import mysql.connector

# Connect to MySQL

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='user@1729',
    auth_plugin='mysql_native_password'
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database only if it doesn't exist
cursorObject.execute("CREATE DATABASE IF NOT EXISTS cricbuzz")

print("Database 'cricbuzz' is ready!")

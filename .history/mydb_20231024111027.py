import mysql.connector

# Establish a connection to the MySQL server
database = mysql.connector.connect(
    host='localhost',  # 'HOST' should be 'host'
    user='root',       # 'USER' should be 'user'
    password='9866@Bhargav$'
)

# Create a cursor object to interact with the database
cursorObject = database.cursor()

# Create a database named 'CRM'
cursorObject.execute("CREATE DATABASE CRM")

# Commit the changes and close the cursor and connection
database.commit()
cursorObject.close()
database.close()

print("Database 'CRM' created successfully.")
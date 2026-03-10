import mysql.connector

# Connect to MySQL without specifying a database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="----------"  # <-- replace with your MySQL root password
)
cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS sentinel_pay")
print("Database 'sentinel_pay' created successfully!")

cursor.close()
conn.close()
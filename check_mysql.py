import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="-------",  # replace with your MySQL root password
    database="sentinel_pay"
)

# Query the table
df = pd.read_sql("SELECT * FROM clean_transactions", conn)
print(df)

conn.close()
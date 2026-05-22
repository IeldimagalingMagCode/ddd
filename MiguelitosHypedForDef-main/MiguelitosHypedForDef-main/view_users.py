import mysql.connector

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sicilian7opening",
    database="pos_system"
)

# Query users table
cur = db.cursor()
cur.execute("SELECT user_id, username, role FROM users")

print("\n=== USERS IN DATABASE ===\n")
for row in cur.fetchall():
    print(f"ID: {row[0]}, Username: {row[1]}, Role: {row[2]}")

cur.close()
db.close()

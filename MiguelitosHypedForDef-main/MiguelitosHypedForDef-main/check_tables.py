import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sicilian7opening",
    database="pos_system"
)

cur = db.cursor()
cur.execute("SHOW TABLES")

print("\n=== TABLES IN pos_system DATABASE ===\n")
tables = cur.fetchall()
if tables:
    for table in tables:
        print(f"  - {table[0]}")
else:
    print("  No tables found!")

cur.close()
db.close()

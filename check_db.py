import sqlite3

conn = sqlite3.connect("internships.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("SELECT * FROM applications")

rows = cursor.fetchall()

print(f"\nFound {len(rows)} application(s)\n")

for row in rows:
    print(dict(row))

conn.close()
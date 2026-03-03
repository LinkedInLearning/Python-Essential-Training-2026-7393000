import sqlite3

conn = sqlite3.connect("example.db") 
cursor = conn.cursor()
cursor.execute("DELETE FROM members WHERE id = 4")
cursor.execute("UPDATE members SET age = 31 WHERE name = 'Bernard'")

conn.commit()

# rows = cursor.execute("SELECT * FROM members ")
# rows = cursor.execute("SELECT name, age FROM members ")
# rows = cursor.execute("SELECT * FROM members WHERE age > 30 ")
rows = cursor.execute("SELECT * FROM members WHERE age > 30 ORDER BY age DESC")
for row in rows:
    print(row)

conn.close()

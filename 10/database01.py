import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS members")
cursor.execute("CREATE TABLE members (id INT PRIMARY KEY, name TEXT, pronun TEXT, age INT)")

conn.commit()
conn.close()
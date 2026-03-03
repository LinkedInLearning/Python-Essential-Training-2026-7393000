import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM members")
cursor.execute("INSERT INTO members VALUES(1,'Aaron','アーロン',35)")
cursor.execute("INSERT INTO members VALUES(2,'Abe','エイブ',44)")
cursor.execute("INSERT INTO members VALUES(3,'Anthony','アンソニー',26)")
cursor.execute("INSERT INTO members VALUES(4,'Barney','バーニー',18)")
cursor.execute("INSERT INTO members VALUES(5,'Bernard','バーナード',30)")

conn.commit()

rows = cursor.execute("SELECT * FROM members")

for row in rows:
    print(row)

conn.close()
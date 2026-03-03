from peewee import *
from tables import Members, db

# DB接続
db.connect()

member = Members.get(Members.id == 4)
member.delete_instance()

member = Members.get(Members.name == "Bernard")
member.age = 31
member.save()

query = Members.select() 
for mem in query:
    print(mem.id, mem.name, mem.pronun, mem.age)

query = Members.select(Members.name, Members.age).where(Members.age > 30).order_by(Members.age.desc())
for mem in query:
    print(mem.name, mem.age)

db.close()
from peewee import *
from tables import Members, db

# DB接続
db.connect()
#複数レコードの一括登録
members=[{'name':'Aaron', 'pronun':'アーロン', 'age':35},
        {'name':'Abe', 'pronun':'エイブ', 'age':44},
        {'name':'Anthony', 'pronun':'アンソニー', 'age':26},
        {'name':'Barney', 'pronun':'バーニー', 'age':18},
        {'name':'Bernard', 'pronun':'バーナード', 'age':30},
        ]
# レコードの削除後、辞書のリストをinsert_manyで登録する
with db.atomic():   #トランザクション処理
    Members.delete().execute() #テーブルのデータを削除
    Members.insert_many(members).execute()

#一括読み込み - 登録データの確認
query = Members.select() 
for mem in query:
    print(mem.id, mem.name, mem.pronun, mem.age)

db.close()
from peewee import *

db = SqliteDatabase('sample.db')

class Members(Model): #Modelクラスを継承    idは自動的に追加される
    name = CharField() #field定義 文字列型（実際にはText型が使われている）
    pronun = TextField(null=True) #文字列型(null許可)
    age = IntegerField() #整数型
    """
    class Metaは、モデルの設定属性を格納するための特別な内部クラス
    モデルに関するメタ情報を定義するために使用
    """
    class Meta:
        database = db   #モデルが使用するデータベースを指定

#Membersテーブルの作成
db.connect()
db.drop_tables([Members]) if Members.table_exists() else None
db.create_tables([Members])
db.close()
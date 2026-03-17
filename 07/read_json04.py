import json             #jsonモジュールをインポート
try:
    f = open("07/test.json","r")
except FileNotFoundError as e: 
    print(f"ファイル{e.filename}が見つかりません")
else:
    data = json.load(f)     #loadで読み込む
    print(data)             #辞書として取得
    print(data["11012"])     
    print(data["11012"]["social"])
    f.close()
finally:
    print("処理を終了しました")

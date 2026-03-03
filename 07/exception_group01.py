# ExceptionGroup Python3.11以降で導入された機能で、複数の例外を一つにまとめて扱うことができる。
# asyncioなどの非同期処理で特に有用。
import json
def read_json():
    exceptions = []
    try:
        f1 = open("test.json","r")
        data = json.load(f1)
        print(data)
        print(data["11012"])
        print(data["11012"]["computer"])
        f1.close()
        # f2 = open("sample.json","r")
        # data = json.load(f2)
        # print(data)
        # f2.close()
    except FileNotFoundError:
        exceptions.append(FileNotFoundError("ファイルが見つかりません"))
    except KeyError:
        exceptions.append(KeyError("指定されたキーが存在しません"))    
    except:
        exceptions.append(Exception("その他の例外が発生しました"))
    # 複数の例外をグループ化して、メッセージを付与
    if exceptions:
        raise ExceptionGroup("処理中にエラーが発生しました", exceptions)

try:
    read_json()
except ExceptionGroup as eg:
    print(f"msg: {eg}")
    # グループ内の各例外を表示
    for e in eg.exceptions:
        print(f"error: {e}")
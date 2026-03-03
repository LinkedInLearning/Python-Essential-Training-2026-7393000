import json

try:
    with open('config.json', 'r') as file:
        config = json.load(file)
except FileNotFoundError:
    print("設定ファイルが見つかりません。デフォルト設定を使用します。")
    config = {"port": "3000", "debug": False}

print("現在の設定:", config)
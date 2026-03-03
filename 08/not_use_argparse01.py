import argparse #argparseをインポート

parser = argparse.ArgumentParser(description='ファイルをコピーするプログラムです')  #Parserを作る

#parser.add_argumentで受け取る引数を追加していく
#自プログラム名の次から順に引数を指定する
parser.add_argument('arg1', help='入力ファイル名')  #位置引数
parser.add_argument('arg2', help='出力ファイル名')  #位置引数
parser.add_argument('-a', '--arg3', help='オプション引数')    # オプション引数
'''
引数名は通常用と省略用の２つ設定でき、通常型は"--"、省略形は"-"で設定する
必須引数とは違い、オプション引数は引数名を指定しないとエラーになる
'''
args = parser.parse_args() #引数を解析

print('arg1='+args.arg1)
print('arg2='+args.arg2)
if args.arg3:
    print('arg3='+args.arg3)

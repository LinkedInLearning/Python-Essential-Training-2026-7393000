import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="第一引数の平方を計算します",type=int)   #位置引数

parser.add_argument("-v", "--verbose", action="store_true",help="より説明調で出力します")    #オプション引数
'''
引数名は通常用と省略用の２つ設定でき、通常型は"--"、省略形は"-"で設定する
actionキーワードを指定し、値として "store_true" を設定している。
これは、オプションが指定された場合に値として True を args.verbose に設定するということを意味する。
オプションの指定がない場合の値は False となる。
'''
args = parser.parse_args()
if args.verbose:
    print(f"引数 {args.square} の平方は {args.square**2} です。")
else:
    print(args.square**2)
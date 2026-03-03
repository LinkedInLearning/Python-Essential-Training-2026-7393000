import sys
from pathlib import Path

def show_error():
    print("読み込むファイルを指定してください")
    print("ex.)get_args02.py filename.txt")

def show_file(fname):
    f = open(fname,"r")
    line = f.readline() 
    while line:
        print(line,end="")
        line = f.readline()
    f.close

def main(fname):
    p = Path(fname)
    if p.exists() and p.is_file():
        show_file(fname)
    else:
        show_error()

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        show_error()
        sys.exit()
    else:
        main(args[1])

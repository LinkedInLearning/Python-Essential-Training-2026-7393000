from pathlib import Path

for name in Path("08/").iterdir():
    if name.is_file():
        print(f"ファイル名:{name} {name.stat().st_size}バイト")

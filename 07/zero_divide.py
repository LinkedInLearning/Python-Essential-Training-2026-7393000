try:
    a = 5 / 0
    print(f"5 / 0= {a}")
except ZeroDivisionError:
    print("0除算例外")
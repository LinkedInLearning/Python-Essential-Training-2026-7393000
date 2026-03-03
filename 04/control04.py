#Python3.10以降のmatch文の例
direct = "left"
match direct:
    case "forward":
        print("Go forward")
    case "backward":
        print("Go backward")
    case "left":
        print("Go left")
    case "right":
        print("Go right")
    case _:
        print("don't move")

val = 1
match val:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Not one, two, or three")

math = 89
match math:
    case x if x >= 90:
        print("excellent!")
    case x if x >= 80:
        print("very good!")
    case x if x >= 60:
        print("good!")
    case _:
        print("bad!")
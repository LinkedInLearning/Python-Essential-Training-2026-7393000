from random import randint

def main():
    counter = 0
    while counter < 10:
        number = randint(1,6)
        print(f"{counter+1}回目は{number}。")
        counter += 1

if __name__ == '__main__':
    main()
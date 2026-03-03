from random import randint
import logging
logging.basicConfig(level=logging.DEBUG,format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.basicConfig(filename="use_loggingLog.txt", level=logging.DEBUG,format=" %(asctime)s - %(levelname)s - %(message)s")

def main():
    counter = 0
    while counter < 10:
        number = randint(1,13)
        print(f"{counter+1}回目は{number}。")
        logging.debug(f"counter={counter}, number={number}")
        counter += 1

if __name__ == '__main__':
    logging.debug("start program")
    main()
    logging.debug("end program")
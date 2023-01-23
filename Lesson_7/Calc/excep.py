from logg import logging


def check_num(n):

    while True:

        if n.isdigit() or (n[:1] == '-' and n[1:].isdigit()):
            n = float(n)
            return n
        else:
            logging.warning(f'Incorrect data entered: {n}')
            print("Error. Try again.")
            n = input("Input the number: ")


def check_num_div(n):

    while True:
        if n.isdigit() or (n[:1] == '-' and n[1:].isdigit()) and n != "0":
            n = float(n)
            return n
        else:
            logging.warning(f'Incorrect data entered: {n}')
            print("Error. Try again.")
            n = input("Input the number: ")


def check_num_sqrt(n):

    while True:
        if n.isdigit() or (n[:1] == '-' and n[1:].isdigit()) and float(n) >= 0:
            n = float(n)
            return n
        else:
            logging.warning(f'Incorrect data entered: {n}')
            print("Error. Try again. Number must be >= 0")
            n = input("Input the number: ")

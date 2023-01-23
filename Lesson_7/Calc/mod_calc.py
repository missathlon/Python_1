import excep as ex
from logg import logging


def init(a, b):
    global x
    global y
    x = a
    y = b


def init_1(a):
    global x
    x = a


def do_complex(a, b):
    n = complex(a, b)
    return n


def do_complex_div(a, b):
    while True:
        if (a == 0 and b == 0) or (a == (-b)):
            logging.warning(f'Incorrect data entered: {a} = {b}')
            print("Error. Try again.")
            a = float(input("Enter 2 real part: "))
            b = float(input("Enter 2 imaginary number: "))
        else:
            n = complex(a, b)
            return n


def sum():
    logging.info(f'{x} + {y} = {x + y}')
    return x+y


def sub():
    logging.info(f'{x} - {y} = {x - y}')
    return x-y


def mult():
    logging.info(f'{x} * {y} = {x * y}')
    return x*y


def pow():
    logging.info(f'{x} ^ {y} = {x ** y}')
    return x**y


def sqrt():
    result = x**(1/2)
    result_minus = -result
    logging.info(f'sqrt: {x} = {result}, {result_minus}')
    return result, result_minus


def div():
    logging.info(f'{x} / {y} = {x / y}')
    return x/y


def exact():
    logging.info(f'{x} // {y} = {x // y}')
    return x//y


def rem():
    logging.info(f'{x} % {y} = {x % y}')
    return x % y

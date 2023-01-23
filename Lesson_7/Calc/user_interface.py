from logg import logging
import mod_calc as mod
import excep as ex


def menu():
    while True:
        num_type = input("Enter type of number\n"
                         "1 - rational numbers\n"
                         "2 - complex numbers\n"
                         "3 - exit\n")
        match num_type:
            case "1":
                menu_rational()
            case "2":
                menu_complex()
            case "3":
                logging.info("Stop program")
                break
            case _:
                logging.warning("Main menu, wrong item selected.")
                print("Error. Try again.")


def menu_rational():
    logging.info("Rational menu started")
    while True:
        to_do = input("Operations:\n"
                      "1 - sum\n"
                      "2 - subtraction\n"
                      "3 - multiplication\n"
                      "4 - division\n"
                      "5 - power\n"
                      "6 - square root\n"
                      "0 - previous menu\n")
        match to_do:
            case "1":
                # sum()
                mod.init(ex.check_num(input("Input 1st number: ")),
                         ex.check_num(input("Input 2nd number: ")))
                print(mod.sum())
            case "2":
                # sub()
                mod.init(ex.check_num(input("Input 1st number: ")),
                         ex.check_num(input("Input 2nd number: ")))
                print(mod.sub())
            case "3":
                # mult
                mod.init(ex.check_num(input("Input 1st number: ")),
                         ex.check_num(input("Input 2nd number: ")))
                print(mod.mult())
            case "4":
                menu_div()
            case "5":
                # pow
                mod.init(ex.check_num(input("Input 1st number: ")),
                         ex.check_num(input("Input 2nd number: ")))
                print(mod.pow())
            case "6":
                # sqrt
                mod.init_1(ex.check_num_sqrt(input("Input number: ")))
                print(mod.sqrt())
            case "0":
                menu()
            case _:
                logging.warning("Operation menu, wrong item selected.")
                print("Error. Try again.")


def menu_div():
    logging.info("Division menu started")
    while True:
        to_do_div = input("Division type:\n"
                          "1 - / - simple division\n"
                          "2 - // - exact division\n"
                          "3 - % - remainder of division\n"
                          "0 - previous menu\n")
        match to_do_div:
            case "1":
                # div()
                mod.init(ex.check_num(input("Input 1st number: ")),
                         ex.check_num_div(input("Input 2nd number: ")))
                print(mod.div())
            case "2":
                # exact()
                mod.init(ex.check_num(input("Input 1st number: ")),
                         ex.check_num_div(input("Input 2nd number: ")))
                print(mod.exact())
            case "3":
                # rem
                mod.init(ex.check_num(input("Input 1st number: ")),
                         ex.check_num_div(input("Input 2nd number: ")))
                print(mod.rem())
            case "0":
                menu_rational()
            case _:
                logging.warning("Operation menu, wrong item selected.")
                print("Error. Try again.")


def menu_complex():
    logging.info("Complex menu started")
    while True:
        to_do = input("Operations:\n"
                      "1 - sum\n"
                      "2 - subtraction\n"
                      "3 - multiplication\n"
                      "4 - division\n"
                      "5 - power\n"
                      "6 - square root\n"
                      "0 - previous menu\n")
        match to_do:
            case "1":
                # sum()
                mod.init(mod.do_complex(ex.check_num(input("Enter 1 real part: ")),
                         ex.check_num(input("Enter 1 imaginary number: "))),
                         mod.do_complex(ex.check_num(input("Enter 2 real part: ")),
                         ex.check_num(input("Enter 2 imaginary number: "))))
                print(mod.sum())
            case "2":
                # sub()
                mod.init(mod.do_complex(ex.check_num(input("Enter 1 real part: ")),
                         ex.check_num(input("Enter 1 imaginary number: "))),
                         mod.do_complex(ex.check_num(input("Enter 2 real part: ")),
                         ex.check_num(input("Enter 2 imaginary number: "))))
                print(mod.sub())
            case "3":
                # mult
                mod.init(mod.do_complex(ex.check_num(input("Enter 1 real part: ")),
                         ex.check_num(input("Enter 1 imaginary number: "))),
                         mod.do_complex(ex.check_num(input("Enter 2 real part: ")),
                         ex.check_num(input("Enter 2 imaginary number: "))))
                print(mod.mult())
            case "4":
                # div()
                mod.init(mod.do_complex(ex.check_num(input("Enter 1 real part: ")),
                         ex.check_num(input("Enter 1 imaginary number: "))),
                         mod.do_complex_div(ex.check_num(input("Enter 2 real part: ")),
                         ex.check_num(input("Enter 2 imaginary number: "))))
                print(mod.div())
            case "5":
                # pow
                mod.init(mod.do_complex(ex.check_num(input("Enter 1 real part: ")),
                         ex.check_num(input("Enter 1 imaginary number: "))),
                         mod.do_complex(ex.check_num(input("Enter 2 real part: ")),
                         ex.check_num(input("Enter 2 imaginary number: "))))
                print(mod.pow())
            case "6":
                # sqrt
                mod.init(mod.do_complex(ex.check_num(input("Enter 1 real part: ")),
                         ex.check_num(input("Enter 1 imaginary number: "))),
                         mod.do_complex(ex.check_num(input("Enter 2 real part: ")),
                         ex.check_num(input("Enter 2 imaginary number: "))))
                print(mod.sqrt())
            case "0":
                menu()
            case _:
                logging.warning("Operation menu, wrong item selected.")
                print("Error. Try again.")

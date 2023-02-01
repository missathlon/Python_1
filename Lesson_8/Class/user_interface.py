import controller as c
import export as init
import exception as ex
from logg import logging
import export


def menu():
    while True:
        c.read_all()
        num_type = input("Выберите опцию:\n"
                         "1 - Показать всех\n"
                         "2 - Поиск\n"
                         "3 - Добавить\n"
                         "4 - Изменить\n"
                         "5 - Удалить\n"
                         "6 - Экспорт/Импорт\n"
                         "0 - Выход\n")
        match num_type:
            case "1":
                c.show_all()
            case "2":
                c.find_entry(
                    input("Что ищем? Пажалуйста, введите имя/фамилию/факультет/форму обучения: "), c.read_all())
            case "3":
                c.add_info(menu_add())
            case "4":
                c.show_all()
                id_change = input(f"Введите id: ")
                if c.find_entry(id_change, c.read_all()) and (answer := edit_menu()):
                    c.edit_entry(answer, id_change)
            case "5":
                c.del_info(input("Введите фамилию: "))
            case "6":
                import_export_menu()
            case "0":
                logging.info("Stop program.\n")
                print("Пока-пока!\n")
                break
            case _:
                logging.warning(f"Main menu, wrong item selected.")
                print("Ошибка ввода. Попробуйте снова.")


def menu_add():
    logging.info("Start add menu")
    add_dict = {"id": "1", "name": "", "surname": "",
                "faculty": "", "form of education": "", "course": ""}
    for i in add_dict:
        if i != "id":
            add_dict[i] = ex.check_new_data(i)
    logging.info('Stop edd menu')
    return add_dict


def edit_menu():
    add_dict = {"1": "name", "2": "surname", "3": "faculty",
                "4": "form of education", "5": "course"}
    logging.info("Start edit menu")
    while True:
        print("\nChanging:")
        change = input("1 - name\n"
                       "2 - surname\n"
                       "3 - faculty\n"
                       "4 - form of education\n"
                       "5 - course\n"
                       "0 - exit\n")

        match change:
            case "1" | "2" | "3" | "4" | "5":
                type_date = add_dict[change]
                return type_date, ex.check_new_data(type_date)
            case "0":
                logging.info('Exited the edit menu')
                return 0
            case _:
                logging.warning(f"Edit menu, wrong item selected.")
                print("Что-то пошло не так. Попробуйте снова. ")


def import_export_menu():
    logging.info('Start import/export menu')
    while True:
        print("\nImport\\Export:")
        change = input("1 - import file\n"
                       "2 - export file\n"
                       "0 - exit\n")
        match change:
            case "1":
                c.file_import(input(f"Enter the database name: "))
                return
            case "2":
                export_format_menu()
            case "0":
                logging.info('Exited the import/export menu')
                break
            case _:
                logging.warning(f"Import/export menu, wrong item selected.")
                print("Информация не найдена. Повторите ввод.")


def export_format_menu():
    logging.info('Start export menu')
    while True:
        logging.info('Start choose a format menu')
        format_type = input(f"Choose a format:\n"
                            f"1 - CSV\n"
                            f"2 - JSON\n"
                            f"3 - XML\n"
                            f"0 - exit\n")
        match format_type:
            case "1":
                export.save_csv(input("Enter the name of the file: "))
                return
            case "2":
                export.save_json(input("Enter the name of the file: "))
                return
            case "3":
                export.save_xml(input("Enter the name of the file: "))
                return
            case "4":
                logging.info('Exited the choose a format menu')
                return
            case _:
                logging.warning(f"Choose a format menu, wrong item selected.")
                print("Информация не найдена. Повторите ввод.")

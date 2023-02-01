import csv
from os import path
from collections import deque

from logg import logging
import exception as ex
all_data = {}
last_id = 0
stud = "students.csv"
lookup_position = None


def read_all():
    global all_data, last_id

    logging.info(f"Show all. Database File - {stud}")
    print(stud)
    if path.exists(stud):
        with open(stud, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            all_data = [i for i in csv_reader]
            last_id = all_data[-1]["id"]
            return all_data
    else:
        logging.warning(
            "The file is not found")
        print("Файл не найден")


def get_block_range(filename, lookupValue):
    if path.exists(stud):
        with open(stud, "r", encoding="utf-8") as file:
            for num, line in enumerate(file, 1):
                return num


def show_all():
    with open("students.csv", encoding='utf-8') as stud:
        file_reader = csv.reader(stud, delimiter=",")
        for row in file_reader:
            print(f'{", ".join(row)}')


def find_entry(data_find, all_info):
    logging.info(f"Search: {data_find}")
    student_found = [" ".join(i.values())
                     for i in all_info if data_find in i.values()]
    if student_found:
        logging.info(f"Search result: {student_found}")
        print(*student_found, sep="\n", end="\n\n")
        return [n[0] for n in student_found]
    else:
        logging.warning(f"No data found: {data_find}")
        print("Информация не найдена.\n")
        return 0


def add_info(data):
    global last_id
    logging.info(f"Adding a new entry: {data}")

    if all(data.values()) and ex.matching_add(data, all_data):
        last_id = int(last_id) + 1
        data["id"] = last_id

        with open(stud, "a", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "name", "surname",
                          "faculty", "form of education", "course"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)
            logging.warning(f"Data added to the student list: {data.values()}")
            print("Информация добавлена")
    else:
        logging.warning("The data is already in the list")
        print("Информация уже есть в списке")


def edit_entry(data_change, id_change):
    global all_data
    key, value = data_change

    logging.info(f"Data changes: {data_change}")
    if find_entry(id_change, all_data):
        for i, v in enumerate(all_data):
            if v["id"] == id_change:
                logging.info(f"Current value: {v[key]}")
                v[key] = value
                logging.info(f"New value: {v[key]}")
                all_data[i] = v

        with open(stud, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "name", "surname",
                          "faculty", "form of education", "course"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_data)
            logging.info("Data changed")
            print("Информация изменена.\n")
    else:
        logging.warning(f"No data found: {data_change}")
        print("Id не найден.\n")

def del_info(data_del):
    global all_data

    logging.info(f"Deleting an entry: {data_del}")
    id_cand = find_entry(data_del, all_data)
    if id_cand:
        id_del = input(f"Введите id: ")
        logging.info(f"Id selected: {id_del}")

        if id_del in id_cand:
            all_data = [k for k in all_data if k["id"] != id_del]
            with open(stud, "w", encoding="utf-8", newline="") as file:
                fieldnames = ["id", "name", "surname",
                          "faculty", "form of education", "course"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_data)
                logging.info(f"Data deleted")
                print("Информация успешно удалена\n")
        else:
            logging.warning(f"No data found: {data_del}")
            print("Id not found.\n")
    else:
        logging.warning(f"No data found: {data_del}")


def file_import(name):
    global stud

    logging.info(f"Changing the database file: {name}")
    if path.exists(name):
        stud = name
        print(stud)
    else:
        logging.warning(f"The database was not found: {name}")
        print("The database was not found.\n")

# как найти определить номер строки/столбца, в которых нахоится инфа



# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby, starmap
from os import path


def code_rle(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text):
        with open(text) as file_1, \
                open(code_text, "w") as file_2:
            for i in file_1:
                file_2.write(
                    "".join([f"{len(list(k))}{g}" for g, k in groupby(i)]))
    else:
        print("The file doesn't exist")


def decode_rle(file):
    if path.exists(file):
        with open(file) as my_file:
            n = ""
            for k in my_file:
                set_list = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        set_list.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x*y, set_list)))
    else:
        print("The file doesn't exist")


code_rle(input("Enter the name of the file with the text: "),
         input("Enter the file name to record: "))
decode_rle(input("Enter the name of the file to decode: "))

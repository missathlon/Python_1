

def matching_add(new_entry: dict, all_info):
    value = list(new_entry.values())[1:]
    all_values = [list(k.values())[1:] for k in all_info]
    return value not in all_values


def if_text(letters):
    while True:
        if letters.isalpha():
            return letters
        else:
            print("Что-то пошло не так.")
            letters = input("Пожалуйста, попробуйте еще раз: ")


def check_new_data(num):
    answer = input(f"Enter a {num}: ")
    while True:
        if num in "name surname faculty form of education":
            if answer.isalpha():
                break
            else:
                answer = input("Информация введена неверно!\n"
                               "Используйте только буквы\n"
                               f"Попробуйте снова: {num}: ")
        if num == "course":
            if answer.isdigit() and 0 < int(answer) < 5:
                break
        answer = input("Информация введена неверно!\n"
                       "Используйте цифры от 1 до 4 для указания курса\n"
                       f"Попробуйте снова {num}: ")
    return answer

# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def do_vocabulary(some_str):
    lst = some_str.split()
    names = {}
    for i in sorted(lst):
        letter = i[0]
        if letter not in names:
            names[letter] = [i]
        else:
            names[letter] += [i]
    return names


print(do_vocabulary(input("Input names: ")))

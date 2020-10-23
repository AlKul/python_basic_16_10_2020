'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''
def my_zip(a, b):
    """
    My own zip(). Возвращает список пар
    """
    c = []
    for i in range(min(len(a), len(b))):
        c.append((a[i], b[i]))
    return c
keys = ("Name", "Surname", "BirthDate", "City", "email", "Phone")
list = ()
def my_input(in_name = "Empty", in_surname  = 0, in_BY =0, in_city = 0, in_email = 0, in_phone = 0):
    values = (in_name, in_surname, in_BY, in_city, in_email, in_phone)
    #string = dict(zip(keys, values))
    string = dict(my_zip(keys, values))
    #list.append(string)
    for key in keys:
        if string[key]:
            print(f"{key}: {string[key]}", end = "  |  ")
    print()
    #print(string)

my_input(in_name="Alex", in_city="Unknown", in_BY="1111 BC")
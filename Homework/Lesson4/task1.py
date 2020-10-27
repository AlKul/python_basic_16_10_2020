'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

script_name, hours, price, bonus = argv

def salary():
    salary = (float(hours)*float(price)) + float(bonus)
    print("Hours: ", hours)
    print("Price: ", price)
    print("Bonus: ", bonus)
    print()
    return salary

print(salary())
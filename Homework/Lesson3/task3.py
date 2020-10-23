'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(num1, num2,num3):
    list = [num1, num2, num3]
    m = min(list)
    list.remove(m)
    return sum(list)

print(my_func(1, 2, 3))
print(my_func(2, 2, 3))
print(my_func(3, 3, 3))
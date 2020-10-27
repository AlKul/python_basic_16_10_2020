'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
'''
from functools import reduce
def prod(prev, curr):
    return prev * curr

list = [el for el in range(100, 1000+1, 2)]
print(list)

print(reduce(prod, list))
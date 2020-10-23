'''
 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def my_division(num, denum):
    if denum == 0:
        print("A-a! You're not allowed to divide by zero!")
        return
    else:
        return num/denum

print(my_division(2,3))
print(my_division(2,4))
print(my_division(2,0))
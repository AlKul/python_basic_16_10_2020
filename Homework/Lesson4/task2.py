'''
Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
'''

from random import randint

n = int(input("Enter the length of the array: "))

a = float(input("Enter the boarders\n min: "))
b = float(input(" max: "))
array = [randint(a, b) for i in range(n)]
print("Your array is as follows:\n",array, "\n")



res2 = [array[i] for i in range(n) if array[i-1] < array[i]]
print(res2)
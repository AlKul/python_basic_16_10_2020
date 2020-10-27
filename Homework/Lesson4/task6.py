'''
 Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
'''

#import itertools
from itertools import count, cycle
for el in count(3):
    if el > 10:
        print()
        break
    else:
        print(el, end = '  ' )

n = 0
a = 'Какой-то список, а не строка'
a = a.split()
for num, el in enumerate(cycle(a), 1):
    if n>=10:
        break
    else:
        print(num, ") ",el)
        n+=1
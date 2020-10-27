'''
Реализовать генератор с помощью функции с ключевым словом yield,создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
    начиная с 1! и до n!.
'''

def fact(n):
    if n>1:
        return n*fact(n-1)
    else:
        return 1

def generator(n):
    for el in range(1, n+1):
        yield fact(el)
#generator = (fact(el) for el in )

g = generator(6)
print(g)
#print(g(12))
for el in g:
    print(el)
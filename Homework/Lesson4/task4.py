'''
Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
'''

def generate_random_array(length, min, max):
    from random import randint
    global array
    array = [randint(min, max) for i in range(length)]
    print("Your array is as follows:\n", array, "\n")
    return


#from random import randint

n = int(input("Enter the length of the array: "))

a = float(input("Enter the boarders\n min: "))
b = float(input(" max: "))

generate_random_array(n , a, b)

res = [el for el in array if array.count(el) == 1]
print(res)
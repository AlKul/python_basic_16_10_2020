'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
'''

my_list = [7, 5, 3, 3, 2]
my_list.sort(reverse=True) #just initial sort(just in case)
print("Your list:\n", my_list)
while 1:
    a = input("Enter any number (to stop enter anything else):")
    if a.isnumeric() == False:
        break
    my_list.append(int(a))
    for i in range((len(my_list) - 1),0, -1):
        if my_list[i] > my_list[i-1]:
            tmp = my_list[i]
            my_list[i] = my_list[i - 1]
            my_list[i] = tmp
    my_list.sort(reverse=True)
    print(my_list)

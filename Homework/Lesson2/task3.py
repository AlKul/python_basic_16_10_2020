'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
season = -1
month = int(input("Your month: "))
list = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]

for item in list:
    if month in item:
        season = list.index(item)
print("List solution:")
if season == 0:
    print("Winter")
elif season == 1:
    print("Spring")
elif season == 2:
    print("Summer")
elif season == 3:
    print("Autumn")
else :
    print("Oops...not in this universe")

my_dict = {(12, 1, 2):"Winter" , (3, 4, 5):"Spring", (6, 7, 8):"Summer", (9, 10, 11):"Autumn"}
print("\nDictionary solution:")
for item in my_dict.keys():
    if month in item:
        print(my_dict.get(item))

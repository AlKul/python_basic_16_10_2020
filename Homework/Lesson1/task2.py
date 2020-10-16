"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

print("Your input:")
seconds = int(input())

hh = int(seconds/3600)
mm = int(int(seconds%3600) /60)
ss = int (seconds%60)


print(f"{hh}:{mm}:{ss}")
"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
print("Enter n:")
n = input()

nn = n*2
nnn= n*3

sum = int(n) + int(nn) + int(nnn)
print(sum)
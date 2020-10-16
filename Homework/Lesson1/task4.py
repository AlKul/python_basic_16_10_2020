"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.

"""
print("Enter  number:")
input_number = input()
a = int(input_number)
max = a%10
while a > 0:
    a= int(a/10)
    b = a%10
    if max < b:
        max = b

print(max)
'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

out_f = open("output.txt", "w")

print("Enter lines, press enter with an empty string to stop: ")
while 1:
    str = input() + "\n"
    if str == "\n":
        break
    out_f.write(str)

out_f.close()
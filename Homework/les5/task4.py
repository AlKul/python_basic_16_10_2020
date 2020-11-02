'''
Создать (не программно) текстовый файл со следующим содержимым:

One — 1

Two — 2

Three — 3

Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

try:
    with open("Data/eng_numerals.txt") as in_f:
        dict = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
        f_out = open("Data/rus_numerals.txt", "w")

        for string in in_f:
            string = string.split(" ")
            try:
                f_out.write(dict[string[0]] + " ")
            except KeyError:
                f_out.write("\n")
                continue
            f_out.write(string[1]+ " " +string[2])


        f_out.close()
except IOError:
    print("Wrong filename")
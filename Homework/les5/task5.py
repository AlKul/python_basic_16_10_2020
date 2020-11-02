'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

f_out = open("Data/output5.txt", "w+")
f_out.write("123 2134124 5413535 626 234 234 42")
f_out.close()

with open("Data/output5.txt") as f_in:
    string = f_in.read().split(" ")
    sum = 0.
    for num in string:
        try:
            sum += int(num)
        except ValueError:
            print("Not a number")
            break
    print(sum)
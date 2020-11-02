'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

try:
    with open("Data/data.txt") as in_f:
        count = 0
        sum = 0.
        content = in_f.readlines()
        for line in content:
            line = line.split(" ")
            if float(line[1]) < 20000:
                print(line[0])
            count += 1
            sum += float(line[1])
        print("\nAverage sallary:", sum/count)
except IOError:
    print("Wrong filename")
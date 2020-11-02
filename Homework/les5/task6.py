'''
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
'''

with open("Data/subj.txt") as f_in:
    dict = {}

    while 1:
        hours = 0.
        string = f_in.readline()
        if not string:
            break
        string = string.split(" ")

        #string = string.split(" ")
        subj = string[0].split(":")[0]


        for substr in string:

            try:
                subsubstr = substr.split("(")

                hours += int(subsubstr[0])
            except:

                continue
        dict[subj] = hours
    print(dict)


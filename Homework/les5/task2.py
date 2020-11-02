'''
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

try:
    with open("outpt.txt") as in_f: # I named it "output" just to use a file from the previous task
        count = 0
        for num, line in enumerate(in_f, 1):
            print(num, ": ", len(line.split(" ")), sep = "")
            count = num
        print("There were", count, "strings in the chosen file")
except IOError:
    print("Seems like there ain't no file with such name")
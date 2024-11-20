path1 = 'C:/Users/Mahyar/Desktop/demo1.txt'
f = open(path1, 'r',encoding='utf-8-sig')
readfile = f.read()
# print(readfile)
# test = "1\n100\n207\n9.9\n19\n"
# print(test)
# list_data = []
# for line in f:
#     list_data.append(float(line.strip()))
# f.close()

# print(list_data)

# readfile = f.read().splitlines()
# print(readfile)
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.read())

# from datetime import datetime
# path2 = 'C:/Users/Mahyar/Desktop/demo2.txt'
# f2 = open(path2, 'w', encoding='utf-8-sig')
# f2.write('Salam\n')
# f2.write('2\n')
# f2.write(str(datetime.now()))
# f2.close()

# data = ["Ali", "Mohsen", "Sara"]
# path3 = 'C:/Users/Mahyar/Desktop/demo3.txt'
# f3 = open(path3, 'w')
# for name in data:
#     f3.write(name + '\n')

# path4 = 'C:/Users/Mahyar/Desktop/demo4.txt'
# f4 = open(path4, 'a')
# f4.write("Hello\n")
# f4.close()

import csv
# path5 = 'C:/Users/Mahyar/Desktop/demo5.csv'
# with open(path5, newline='') as f5:
#     reader = csv.reader(f5)
#     for row in reader:
#         username = row[0]
#         code = row[1]

# path6 = 'C:/Users/Mahyar/Desktop/demo6.csv'
# data = [['mahyar','nazari','7328'],["Jafar","Jafari","1313"],["Ahmad","Asghari","1428"]]
#
# with open(path6, 'w', newline='') as f6:
#     writer = csv.writer(f6)
#     writer.writerows(data)

from statistics import mean
path7 = 'C:/Users/Mahyar/Desktop/demo7.csv'
dict_grade = {}
with open(path7, newline='') as f5:
    reader = csv.reader(f5)
    for row in reader:
        name = row[0]
        scores = row[1:]
        list_scores_int = []
        for score in scores:
            list_scores_int.append(int(score))

        avg = mean(list_scores_int)
        dict_grade[name] = avg

data = list(dict_grade.items())
path8 = 'C:/Users/Mahyar/Desktop/grade.csv'
with open(path8, 'w', newline='') as f8:
    writer = csv.writer(f8)
    writer.writerows(data)
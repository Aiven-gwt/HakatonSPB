import pandas as pd
import re

#\}(.*?)\{

f1 = open('data2.txt', 'r', encoding="UTF-8")
file = f1.read()

a = re.sub('}*{', '\n', file)
a = a.replace('\n\n', '\n')
#a = a.replace('\n\n', '\n')

f2 = open('data3.txt', 'w', encoding="UTF-8")
f2.write(a)

f1.close()
f2.close()

# f2 = open('data3.txt', 'r', encoding="UTF-8")
# file = f2.read()


# f = open('C:/Users/v_bia/PycharmProjects/HakatonSPB/data2.txt', 'r', encoding='UTF-8')
# start = '}'
# end = '{'
# startFound = False
#
# for l in f:
#     str = l.strip()
#     if not str:
#         continue
#
#     if end in str:
#         break
#
#     if startFound:
#         print(str)
#
#     if start in str:
#         startFound = True
#
#
#     f.close()
# f1 = open('data2.txt', 'r', encoding="UTF-8")
# file = f1.read()
# a = re.sub('}*{', '\t', file)
# b = a.replace('}', ' ')
# c = b.replace('\n', '\t')
# a = re.split('\t', c)
#
# a1 = []
# for i in a:
#     a1.append(i.strip())
# #a1 = list(set(a))
# print(a1)
#
# #del a[1::2]
#
#
# def fill_file(var):
#     j = var[:2]
#     f = open(f'C:/Users/v_bia/PycharmProjects/HakatonSPB/learning/{j}.txt', 'w')
#     f.write(var)
#     f.close()
#
#
# for i in a1:
#     fill_file(i)
# f1.close()





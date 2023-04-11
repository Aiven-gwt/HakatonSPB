import os
import docx
import re


def tt(filename):
    doc = docx.Document(filename)
    return '\n'.join([p.text for p in doc.paragraphs])


def analiz(filename):
    f = open(filename, 'r', encoding="UTF-8")
    f2 = open('data2.txt', 'w', encoding="UTF-8")
    for i in f:
        str_start_index = i.find('{')
        str_end_index = i.rfind('{')
        if str_end_index != -1 and str_start_index != -1 and i[str_start_index + 1] == i[str_end_index + 1]:
            f2.write(i[str_start_index: str_end_index + 4])
        # if i[str_start_index + 1] == i[str_end_index + 1]:

    f.close()
    f2.close()


paths = []
folder = os.getcwd()
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('docx') and not file.startswith('~'):
            paths.append(os.path.join(root, file))

txt = map(tt, paths)

myfile = open("data.txt", "w", encoding="utf-8")
for i in txt:
    myfile.write(i)
myfile.close()

analiz('data.txt')

f1 = open('data2.txt', 'r', encoding="UTF-8")
file = f1.read()

a = re.sub('}*{', '\t', file)
a = a.replace('\n', ' ')
f2 = open('data3.txt', 'w', encoding="UTF-8")
f2.write(a)
f1.close()
f2.close()
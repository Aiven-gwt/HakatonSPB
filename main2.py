import pandas as pd
import re

f1 = open('data2.txt', 'r', encoding="UTF-8")
# f2 = open('data3.txt', 'r')
#pd.read_table('ch05_05.txt', sep='\{.[0-9]}[а-яА-Я0-9 ]*[^{]', header=None, engine='python')
lines = f1.readlines()

for line in lines:
    ex = re.match(r'\{.[0-9]}[а-яА-Я0-9 ]*[^{]', line, flags=0)
f1.close()

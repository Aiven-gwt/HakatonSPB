import re
# \{1\}(\w.*?)\{1\}
f = open('data2.txt', 'r', encoding="UTF-8")
file = f.read()

a = re.findall(r'\{39\}(\w.*?)\{39\}', file)
f1 = open(f'C:/Users/v_bia/PycharmProjects/HakatonSPB/learning/39.txt', 'w', encoding="UTF-8")

for i in a:
    f1.write(i)
f.close()
f1.close()
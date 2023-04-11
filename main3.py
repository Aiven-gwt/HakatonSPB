
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


analiz('data.txt')

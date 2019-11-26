import random
#  чисто пример файла, где генерируются значения для графика, которые помещаются в файл sample.txt
data_x = [x for x in range(0, 50, 5)]
print(data_x)
f = open("sample.txt", "w")
for element in data_x:
    f.write(str(element)+','+str(random.randint(1, 5))+'\n')  #  запихуем значения типа 0,4


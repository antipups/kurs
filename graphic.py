import matplotlib.pyplot as plt
import numpy as np

rng = np.arange(50)  # массив на 50
rnd = np.random.randint(0, 10, size=(3, rng.size))
yrs = 1950 + rng

fig, ax = plt.subplots(figsize=(5, 3))  # распаковка кортежа, содержащего фигуру и объект осей в fig и ax. figsize - ширина и высота в дюймах
ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])  # само построение, вкидываем иксы и игрики
ax.set_title('Combined debt growth over time')  # название
ax.legend(loc='upper left')  # локализация пояснения, что в графике каким цветом написано
ax.set_ylabel('Total debt')  # подпись по игрику
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])  # откуда начинаем показывать график, до какого значения показываем
fig.tight_layout()
fig.savefig('yourfilename.png')  # так можно сохранять
plt.show()








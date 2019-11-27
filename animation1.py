import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open('sample.txt', 'r').read()  # берем значения из файла, в который они записываются из другой функции
    dataArray = pullData.split('\n')  # далее достаем данные
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xar.append(int(x))  # засовываем в список иксов
            yar.append(int(y))  # засовываем в список игриков

    ax1.clear()  # очищаем, чтобы каждый раз, когда обновляется, картинка рисовалась с нуля, а не поверх старой
    ax1.plot(xar, yar)
ani = animation.FuncAnimation(fig, animate, interval=5000)  # строим, график. Интервал 5 секунд
plt.show()
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import functional


def draw():
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    def animate(i):
        with open('sample.txt', 'r') as f:
            pullData = f.read()             # берем значения из файла, в который они записываются из другой функции
        dataArray = pullData.split('\n')    # далее достаем данные
        xar = []
        yar = []
        color = str()
        for eachLine in dataArray:
            if len(eachLine) > 2:
                x, y, color = eachLine.split(',')
                xar.append(int(x))  # засовываем в список иксов
                yar.append(int(y))  # засовываем в список игриков

        ax1.clear()  # очищаем, чтобы каждый раз, когда обновляется, картинка рисовалась с нуля, а не поверх старой
        ax1.plot(xar, yar, color)

    ani = animation.FuncAnimation(fig, animate, interval=1000)  # строим, график. Интервал 5 секунд
    plt.show()


if __name__ == '__main__':
    draw()

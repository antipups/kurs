import matplotlib.pyplot as plt
import matplotlib.animation as animation


def draw():
    fig = plt.figure()
    plt.get_current_fig_manager().window.wm_geometry('+320+20')     # расположение окна
    ax1 = fig.add_subplot(1, 1, 1)

    def animate(i):
        with open('multi_time.txt', 'r') as f:
            pullData = f.read()
        dataArray = pullData.split('\n')    # далее достаем данные
        xar = list()
        yar = list()
        for eachLine in dataArray:
            if len(eachLine) > 2:
                x, y = eachLine.split(',')
                xar.append(int(x))  # засовываем в список иксов
                yar.append(int(y))  # засовываем в список игриков
        ax1.clear()
        ax1.plot(xar, yar, '-ok', markersize=14)

        with open('time.txt', 'r') as f:
            pullData = f.read()

        dataArray = pullData.split('\n')  # далее достаем данные
        xar.clear()
        yar.clear()
        for eachLine in dataArray:
            if len(eachLine) > 2:
                x, y = eachLine.split(',')
                xar.append(int(x))  # засовываем в список иксов
                yar.append(int(y))  # засовываем в список игриков
        ax1.plot(xar, yar, '-or', markersize=14)

    ani = animation.FuncAnimation(fig, animate, interval=1000)  # строим, график. Интервал 5 секунд
    plt.show()


if __name__ == '__main__':
    draw()

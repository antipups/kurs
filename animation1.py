import matplotlib.pyplot as plt
import matplotlib.animation as animation


def draw():
    fig = plt.figure()      # создание самой фигуры (в графике это точка)
    plt.get_current_fig_manager().window.wm_geometry('+320+20')     # расположение окна
    ax1 = fig.add_subplot(1, 1, 1)  # добавление фигуры на график

    def animate(i):     # функция меняющая играфик
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
    ani = animation.FuncAnimation(fig, animate, interval=5000)  # строим, график. Интервал 5 секунд
    plt.show()


if __name__ == '__main__':
    draw()
    # тест

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def draw():
    fig = plt.figure()
    plt.get_current_fig_manager().window.wm_geometry('+320+20')     # расположение окна
    ax1 = fig.add_subplot(1, 1, 1)

    def animate(i):
        ax1.clear()
        for name_of_file in ( 'multi_time.txt', 'time.txt', 'user.txt'):
            with open(name_of_file, 'r') as f:
                pullData = f.read()
            dataArray = pullData.split('\n')    # далее достаем данные
            xar = list()
            yar = list()
            if name_of_file == 'user.txt':  # одноленточная черная
                color = '-ob'
            elif name_of_file == 'multi_time.txt':  # многоленточная бот, красная
                color = '-or'
            else:   # многоленточная синяя
                color = '-ok'
            for eachLine in dataArray:
                if len(eachLine) > 2:
                    x, y = eachLine.split(',')
                    xar.append(int(x))  # засовываем в список иксов
                    yar.append(int(y))  # засовываем в список игриков
            ax1.plot(xar, yar, color)

    ani = animation.FuncAnimation(fig, animate, interval=1000)  # строим, график. Интервал 5 секунд
    plt.show()


if __name__ == '__main__':
    draw()

from for_one_tape import mt_for_one_tape
from for_multi_tape import mt_for_multi_tape
import time


def generate():
    """
            Генератор.
        Генерирует всё время новые значения, по типу было abc стало abcabc, и так до бесконечности.
    """
    word = ''  # начальное слово
    while True:
        time.sleep(.001)    # задержка чтоб было легче дышать машине.
        # run(word + ''.join(reversed(word)), True, False)  # заносим сгенерированное слово в функцию решения задачи
        run(word + ''.join(reversed(word)), True, True)  # заносим сгенерированное слово в функцию решения задачи
        word += 'abc'


def run(word, bot=True, multitape=True):     # word - само слово, bot - генератор, multitape - многоленточность
    """
            Функция запуска.
        То есть функция, которая кладет сгенерированное, слово в мт, и обрабатывает всё.
    """
    if multitape is True:
        mt = mt_for_multi_tape()
        namefile = 'multi_time.txt'
    else:
        mt = mt_for_one_tape()
        namefile = 'time.txt'
    mt.heart(word + '_', bot=bot)
    if bot is True:     # значения сформированные генератором пишем в файл для графика
        with open(namefile, 'a') as f:
            f.write('\n' + str(len(word)) + ',' + str(mt.amount_of_steps) + '\n')
    if mt.result_word == '0':
        return 'Введенное слово - ' + word + ';\nНЕ удовлетворяет языку.', [1, 0, 0, 1]
    else:
        return 'Введенное слово - ' + word + ';\nУДОВЛЕТВОРЯЕТ языку.', [0, .75, 0, 1]


if __name__ == '__main__':
    pass
    # тест

from mt_for_check_words_plus_ribbon import mt_for_check_words_plus_ribbon


def generate():
    """
            Генератор работает так, на вход в функцию plus подается слово,
        и далее как обычная система сложения в столбик, мы смотрим на полсдений
        элемент входного слова, и увеличиваем его на 1, то есть если была буква
        a мы меняем её на b и выходим, тоже самое с b, но с c, мы меняем её на a
        и просматриваем элемент находящий левее, и увеличиваем его.
        Пример:
            aba -> abb      # т.к. последняя a, мы её меняем на b
            abb -> abc      # т.к. последняя b, мы меняем её на c
            abc -> aca      # т.к. последняя c, мы меняем её на a, и также затрагиваем букву левее
            ...
            ccc -> aaaa     # т.к. все буквы c, мы меняем каждую на a и потом добавляем a в начало строки
    """
    def plus(word):     # генератор слов
        if word[-1] == 'a':                 # cba -> cbb
            return word[:-1] + 'b'
        elif word[-1] == 'b':               # cbb -> cbc
            return word[:-1] + 'c'
        elif word[-1] == 'c':
            word = word[:-1] + 'a'          # cbc -> cba*
            i = 2   # индекс элемента которого меняем
            while True:
                try:
                    if word[-i] == 'a':
                        word = list(word)
                        word[-i] = 'b'
                        return ''.join(word)
                    elif word[-i] == 'b':
                        word = list(word)
                        word[-i] = 'c'
                        return ''.join(word)
                    elif word[-i] == 'c':
                        word = list(word)
                        word[-i] = 'a'
                        i += 1  # переходим на след. букву, если ещё раз выпала c: bcfcCa - > bcfCaa
                except IndexError:  # если слово полностью обновляется (ccc) добавляем новый элемент в начало (aaaa)
                    word = ''.join(word)
                    return 'a' + word
    word = 'a'  # начальное слово
    while True:
        word = plus(word)   # генерируем новое слово на основе старого
        run(word + ''.join(reversed(word)), True, True)  # заносим сгенерированное слово в функцию решения задачи


def run(word, bot=True, multitape=True):     # word - само слово, bot - генератор, multitape - многоленточность
    """
            При входе слово обрамляется шаблоном (L по бокам), ставится стартовая ячейка,
        уведомляется генератор это или нет, и многоленточность или нет.
            После того как слово прошло через машины, на выходе мы получаем кол-во шагов,
        потраченное на получение результата, и ответ, да или нет. Записываем результаты
        а именно кол-во шагов, и длину слова в файл, оттуда график считывает значения для
        графиков, всего их 3, многоленточный, одноленточный, и пользовательский, и рисует
        соответственно график зависимости.
    """
    mt = mt_for_check_words_plus_ribbon()
    mt.heart('L' + word + 'L', cursor=1, bot=bot, multitape=multitape)
    if bot is False:                            # если не бот, на графике помечаем синим цветом
        if multitape is True:
            name_of_file = 'user.txt'   # если пользователь запустил на многоленточной
        else:
            name_of_file = 'time.txt'   # если пользователь запустил на одноленточной
    else:                     # если бот на мульти ленточной
        name_of_file = 'multi_time.txt'
    with open(name_of_file, 'a') as f:
        f.write('\n' + str(len(word)) + ',' + str(mt.amount_of_steps) + '\n')
    if mt.result_word == '0':
        return 'Слово не подходит', [1, 0, 0, 1]
    else:
        return 'Слово подходит', [0, .75, 0, 1]


if __name__ == '__main__':
    pass

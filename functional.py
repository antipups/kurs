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
        run('-ob', word + ''.join(reversed(word)))  # заносим сгенерированное слово в функцию решения задачи


"""
        При входе, слово попадает в первую машину в которой узнает сколько сиволов в одном слове,
    если кол-во символов нечетное, выдает 0, выходим, если четное то идем дальше, в след.
    две мт, которые достают отдельно 2 слова, на разных лентах в разных потоках, после завершения
    работы этих машин, эти два слова подаются в последнюю машину, которая уже сверяет реверс это
    или нет.
"""


def run(color, word, bot=True):     # word - само слово, color - какой цвет линии будет использоватся
    # print('Входящее слово - ' + word)
    mt = mt_for_check_words_plus_ribbon()
    mt.heart('L' + word + 'L', cursor=1, bot=bot)
    with open('sample.txt', 'a') as f:
        f.write('\n' + str(len(word)) + ',' + str(mt.amount_of_steps) + ',' + color + '\n')
    if mt.second_ribbon == '0':
        return 'Слово не подходит', [1, 0, 0, 1]
    else:
        return 'Слово подходит', [0, .75, 0, 1]


if __name__ == '__main__':
    pass

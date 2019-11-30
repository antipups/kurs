import threading
from mt_for_check_words import mt_for_check_words
from mt_for_find_amount_litter_in_one_word import mt_for_find_amount_litter_in_one_word
from mt_for_find_first_word import mt_for_find_first_word
from mt_for_find_second_word import mt_for_find_second_word


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


def run(color, word):     # word - само слово, color - какой цвет линии будет использоватся
    amount_of_steps = 0
    # print('Входящее слово - ' + word)
    current_mt = mt_for_find_amount_litter_in_one_word()
    current_mt.heart(word='L' + '00!' + word + 'L', cursor=3)
    amount_of_steps += current_mt.amount_of_steps
    amount_of_characters = current_mt.result_word
    if amount_of_characters == '0':
        return 'Слово не подходит', [1, 0, 0, 1]
    else:
        first_mt = mt_for_find_first_word()
        second_mt = mt_for_find_second_word()
        t1 = threading.Thread(target=first_mt.heart, args=('L' + amount_of_characters + '!' + word + 'L', 3))
        # создаем поток машины на первой ленте
        t2 = threading.Thread(target=second_mt.heart, args=('L' + amount_of_characters + '!' + word + 'L', 3))
        # создаем поток машины на второй ленте
        t1.start()
        t2.start()
        t2.join()   # ставим некий wait, пока потоки не отработают основной поток стоит
        first_word = first_mt.result_word
        second_word = second_mt.result_word
        amount_of_steps += first_mt.amount_of_steps + second_mt.amount_of_steps
        # print('Первое слово - ' + first_word)
        # print('Второе слово - ' + second_word)
        current_mt = mt_for_check_words()
        current_mt.heart(word='L' + first_word + '*' + second_word + 'L', cursor=1)
        amount_of_steps += current_mt.amount_of_steps
        # print('Задача - ' + current_mt.result_word)
        # time.sleep(1)
        with open('sample.txt', 'a') as f:
            f.write('\n' + str(len(word)) + ',' + str(amount_of_steps) + ',' + color + '\n')
        if current_mt.result_word == '0':
            return 'Слово не подходит', [1, 0, 0, 1]
        else:
            return 'Слово подходит', [0, .75, 0, 1]


if __name__ == '__main__':
    pass

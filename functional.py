import threading
import time
from mt_for_check_words import mt_for_check_words
from mt_for_find_amount_litter_in_one_word import mt_for_find_amount_litter_in_one_word
from mt_for_find_first_word import mt_for_find_first_word
from mt_for_find_second_word import mt_for_find_second_word


"""
    Здесь вся композиция машин, распоточивание и прочее.
"""


def run(word):
    # print('Входящее слово - ' + word)
    current_mt = mt_for_find_amount_litter_in_one_word()
    current_mt.heart(word='L' + '00!' + word + 'L', cursor=3)
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
        print('Первое слово - ' + first_word)
        print('Второе слово - ' + second_word)
        current_mt = mt_for_check_words()
        current_mt.heart(word='L' + first_word + '*' + second_word + 'L', cursor=1)
        print('Задача - ' + current_mt.result_word)
        return 'Слово подходит', [0, .75, 0, 1]


if __name__ == '__main__':
    run('abccbaabccbaabccba')        # сделать проверку на ввод

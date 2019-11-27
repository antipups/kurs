from mt_for_check_words import mt_for_check_words
from mt_for_find_amount_litter_in_one_word import mt_for_find_amount_litter_in_one_word
from mt_for_find_first_word import mt_for_find_first_word
from mt_for_find_second_word import mt_for_find_second_word


"""
    Здесь вся композиция машин, распоточивание и прочее.
"""


def run(word):
    print('Входящее слово - ' + word)
    amount_of_characters = mt_for_find_amount_litter_in_one_word().heart(word='L' + '00!' + word + 'L', cursor=3)
    if amount_of_characters == '0':
        print('Ввел хуйню')
    else:
        first_word = mt_for_find_first_word().heart(word='L' + amount_of_characters + '!' + word + 'L', cursor=3)
        second_word = mt_for_find_second_word().heart(word='L' + amount_of_characters + '!' + word + 'L', cursor=3)
        print('Первое слово - ' + first_word)
        print('Второе слово - ' + second_word)
        print('Задача - ' + mt_for_check_words().heart(word='L' + first_word + '*' + second_word + 'L', cursor=1))
        print('Вышло')


if __name__ == '__main__':
    run('abccbaabccbaabccba')        # сделать проверку на ввод

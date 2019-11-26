from mt_for_find_amount_litter_in_one_word import mt_for_find_amount_litter_in_one_word
from mt_for_find_first_word import mt_for_find_first_word
from mt_for_find_second_word import mt_for_find_second_word


"""
    Здесь вся композиция машин, распоточивание и прочее.
"""


def run(word):
    print('Входящее слово -' + word)
    amount_of_characters = mt_for_find_amount_litter_in_one_word().heart(word='L' + '00!' + word + 'L', cursor=3)
    if amount_of_characters == '0':
        print('Ввел хуйню')
    else:
        print('Первое слово - ' + mt_for_find_first_word().heart(word='L' + amount_of_characters + '!' + word + 'L', cursor=3))
        print('Второе слово - ' + mt_for_find_second_word().heart(word='L' + amount_of_characters + '!' + word + 'L', cursor=3))
        print('Вышло')


if __name__ == '__main__':
    run('abccba')        # сделать проверку на ввод

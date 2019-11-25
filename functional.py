from mt_for_find_amount_litter_in_one_word import mt_for_find_amount_litter_in_one_word
from mt_for_find_first_word import mt_for_find_first_word


def run(word):
    amount_of_characters = mt_for_find_amount_litter_in_one_word().heart(word='L' + '00!' + word + 'L', cursor=3)
    if not amount_of_characters:
        print('sex')


if __name__ == '__main__':
    # run('abcc')
    word = ['L', 'L', 'L', 'L', 'a', 'b', 'L', 'L', 'L']

    print(''.join(word))
from mt import mt
from mt_for_find_amount_litter_in_one_word import mt_for_find_amount_litter_in_one_word
from mt_for_find_first_word import mt_for_find_first_word


"""
    Машина тьюринга которая получает результаты первой мт(выводит кол-во букв в одном слово),
    вырезает и выводит ВТОРОЕ слово из слова веденным пользователем.
"""


class mt_for_find_second_word(mt):

    def first_condition(self):
        if self.letter in self.tuple_alfabet:
            self.letter = '*'
            self.direction = '<'
            self.number_of_state = self.second_condition
        elif self.letter in self.all_new_letter:
            self.direction = '>'

    def second_condition(self):
        self.direction = '<'
        if self.letter == '!':
            self.number_of_state = self.third_condition

    def third_condition(self):
        self.direction = '<'
        if self.letter == '0':
            self.letter = '9'
            self.number_of_state = self.sixth_condition
        elif self.letter == '1':
            self.letter = '0'
            self.number_of_state = self.fourth_condition
        elif self.letter in self.all_new_letter[3:-1]:
            self.letter = str(int(self.letter) - 1)
            self.direction = '>'
            self.number_of_state = self.first_condition

    def fourth_condition(self):
        self.direction = '>'
        if self.letter == '0':
            self.letter = 'L'
            self.number_of_state = self.fifth_condition
        elif self.letter == '1':
            self.number_of_state = self.first_condition
        elif self.letter in self.all_new_letter[3:-1]:
            self.letter = str(int(self.letter) - 1)
            self.number_of_state = self.first_condition

    def fifth_condition(self):
        if self.letter in self.tuple_alfabet:
            self.direction = 'stop'
        elif self.letter in self.all_new_letter:
            self.letter = 'L'
            self.direction = '>'

    def sixth_condition(self):
        self.direction = '>'
        if self.letter in self.all_new_letter[2:-1]:
            self.letter = str(int(self.letter) - 1)
            self.number_of_state = self.first_condition


if __name__ == '__main__':
    pass
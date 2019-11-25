from mt import mt
from mt_for_find_amount_litter_in_one_word import mt_for_find_amount_litter_in_one_word


class mt_for_find_first_word(mt):

    all_new_letter = ('!', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*')

    def first_condition(self):
        self.direction = '>'
        if self.letter == 'L':
            self.direction = '<'
            self.number_of_state = self.second_condition

    def second_condition(self):
        self.direction = '<'
        if self.letter in self.tuple_alfabet:
            self.letter = '*'
            self.number_of_state = self.third_condition

    def third_condition(self):
        self.direction = '<'
        if self.letter == '!':
            self.number_of_state = self.fourth_condition

    def fourth_condition(self):
        if self.letter == '0':
            self.letter = '9'
            self.direction = '<'
            self.number_of_state = self.fifth_condition
        elif self.letter == '1':
            self.letter = '0'
            self.direction = '<'
            self.number_of_state = self.seventh_condition
        elif self.letter in self.all_new_letter[3:-1]:
            self.letter = str(int(self.letter) - 1)
            self.direction = '>'
            self.number_of_state = self.first_condition

    def fifth_condition(self):
        self.direction = '>'
        if self.letter in self.all_new_letter[2:-1]:
            self.letter = str(int(self.letter) - 1)
            self.number_of_state = self.first_condition
        elif self.letter == '0':
            self.letter = 'L'
            self.number_of_state = self.sixth_condition

    def sixth_condition(self):
        self.direction = '>'
        if self.letter in ('!', '0', '9'):
            self.letter = 'L'
        elif self.letter == '*':
            self.letter = 'L'
        elif self.letter == 'L':
            self.letter = 'L'
            self.direction = 'stop'

    def seventh_condition(self):
        self.direction = '>'
        if self.letter == '0':
            self.letter = 'L'
            self.number_of_state = self.sixth_condition
        elif self.letter == self.all_new_letter[2:]:
            self.number_of_state = self.first_condition


if __name__ == '__main__':
    word = 'abcccc'
    amount_of_characters = mt_for_find_amount_litter_in_one_word().heart(word='L' + '00!' + word + 'L', cursor=3)
    if not amount_of_characters:
        print('Ввел хуйню')
    else:
        print(mt_for_find_first_word().heart(word='L' + amount_of_characters + '!' + word + 'L', cursor=3))
        print('Вышло')
from mt import mt


class mt_for_find_amount_litter_in_one_word(mt):

    all_new_letter = ('!', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*')

    def first_condition(self):
        if self.letter in mt.tuple_alfabet:
            self.number_of_state = self.second_condition
            self.direction = '<'
            self.letter = '*'
        elif self.letter == 'L':
            self.number_of_state = self.fifth_condition
            self.direction = 'stop'
        else:
            return

    def second_condition(self):
        self.direction = '<'
        if self.letter == self.all_new_letter[0]:
            self.number_of_state = self.third_condition
        else:
            return

    def third_condition(self):
        if self.letter in self.all_new_letter[1:-2]:
            self.letter = str(int(self.letter) + 1)     # получаем цифру на которой стоит и прибавляем 1 если это не 9
            self.direction = '>'
            self.number_of_state = self.first_condition
        else:
            self.letter = '0'
            self.direction = '<'
            self.number_of_state = self.third_condition

    def fourth_condition(self):
        self.letter = 'L'
        self.direction = '>'
        if self.letter == self.all_new_letter[-1]:
            self.number_of_state = self.fourth_condition
        else:
            self.number_of_state = self.tenth_condition

    def fifth_condition(self):
        print('sex')
        self.direction = '<'
        if self.letter == self.all_new_letter[0]:
            self.number_of_state = self.sixth_condition
        else:
            self.number_of_state = self.fifth_condition

    def sixth_condition(self):
        if self.letter in ('1', '3', '5', '7', '9',):
            self.number_of_state = self.seventh_condition
            self.direction = '>'
        elif self.letter in ('2', '4', '6', '8'):
            self.number_of_state = self.eighth_condition
            self.direction = '>'
        else:
            self.number_of_state = self.ninth_condition
            self.direction = '<'

    def seventh_condition(self):
        self.direction = '>'
        if self.letter == self.all_new_letter[-1]:
            self.letter = '0'
            self.number_of_state = self.fourth_condition

    def eighth_condition(self):
        self.direction = '>'
        if self.letter == self.all_new_letter[-1]:
            self.letter = '1'
            self.number_of_state = self.fourth_condition

    def ninth_condition(self):
        self.direction = '>'
        if self.letter == self.all_new_letter[2:-1]:
            self.number_of_state = self.eighth_condition
        else:
            self.number_of_state = self.seventh_condition

    def tenth_condition(self):
        if self.letter == self.all_new_letter[0]:
            self.direction = '>'
            self.number_of_state = self.eleventh_condition
        else:
            self.direction = '<'

    def eleventh_condition(self):
        self.direction = '<'
        if self.letter == self.all_new_letter[1]:
            self.number_of_state = self.eighteenth_condition
        else:
            self.number_of_state = self.twelfth_condition

    def twelfth_condition(self):
        if self.letter in self.all_new_letter[:-1]:
            self.direction = '<'
        else:
            self.direction = '>'
            self.number_of_state = self.thirteenth_condition

    def thirteenth_condition(self):
        self.direction = '>'
        even, uneven = ('0', '2', '4', '6', '8'), ('1', '3', '5', '7', '9')
        if self.letter in even:
            self.number_of_state = self.fourteenth_condition
            if self.letter == even[1]:
                self.letter = '1'
            elif self.letter == even[2]:
                self.letter = '2'
            elif self.letter == even[3]:
                self.letter = '3'
            elif self.letter == even[4]:
                self.letter = '4'
        else:
            self.number_of_state = self.fifteenth_condition
            if self.letter == uneven[0]:
                self.letter = '0'
            elif self.letter == uneven[1]:
                self.letter = '1'
            elif self.letter == uneven[2]:
                self.letter = '2'
            elif self.letter == uneven[3]:
                self.letter = '3'
            elif self.letter == uneven[4]:
                self.letter = '4'

    def fourteenth_condition(self):
        even = ('2', '4', '6', '8')
        self.number_of_state = self.sixteenth_condition
        self.direction = '>'
        if self.letter in even:
            if self.letter == even[0]:
                self.letter = '1'
            elif self.letter == even[1]:
                self.letter = '2'
            elif self.letter == even[2]:
                self.letter = '3'
            elif self.letter == even[3]:
                self.letter = '4'

    def fifteenth_condition(self):
        even = ('0', '2', '4', '6', '8')
        self.number_of_state = self.sixteenth_condition
        self.direction = '>'
        if self.letter in even:
            if self.letter == even[0]:
                self.letter = '5'
            elif self.letter == even[1]:
                self.letter = '6'
            elif self.letter == even[2]:
                self.letter = '7'
            elif self.letter == even[3]:
                self.letter = '8'
            elif self.letter == even[4]:
                self.letter = '9'

    def sixteenth_condition(self):
        if self.letter == self.all_new_letter[0]:
            self.direction = '>'
            self.letter = '*'
        else:
            self.letter = 'L'
            self.direction = '<'
            self.number_of_state = self.seventeenth_condition

    def seventeenth_condition(self):
        if self.number_of_state in self.all_new_letter[1:]:
            self.direction = '<'
            if self.letter == '*':
                self.letter = 'L'
        else:
            self.direction = 'stop'

    def eighteenth_condition(self):
        if self.number_of_state in self.all_new_letter[:-1]:
            self.direction = '<'
            self.letter = 'L'
        else:
            self.direction = '>'
            self.number_of_state = self.nineteenth_condition

    def nineteenth_condition(self):
        if self.letter == '0':
            self.direction = 'stop'
        else:
            self.direction = '>'



if __name__ == '__main__':
    mt = mt_for_find_amount_litter_in_one_word()
    print(mt.heart(word='L' + '00!abca' + 'L', cursor=3))
    # even = ('2', '4', '6', '8')
    # for i in enumerate(even):
    #     print(i)
    pass

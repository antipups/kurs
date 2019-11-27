from mt import mt


"""
    Машина тьюринга которая подсчитывает кол-во символов в одном слове, на выходе,
    естественно, получаем кол-во букв в одном слове, если конечно это слово по длине удовлетворяет условию,
    то есть кол-во букв в веденном от юзера слове четное кол-во, иначе выводит ничего, и длина списка = 0
    что и является первой проверкой на корректность ввода правильного слова.
    
    Как работает:
            Двигается вправо и считает кол-во символов попутно помечая прочитанные буквы звездой,
        после, стирает все буквы и пишет четное это число или нет, если оно нечетное
        (что не удовлетворяет условию) затираем всё и оставляем ноль, если же четное, делим кол-во
        букв на 2, и получаем число которое означает кол-во букв в одном слове.
"""


class mt_for_find_amount_litter_in_one_word(mt):

    def first_condition(self):
        """
            Нашли букву, пометили.
        """
        if self.letter in mt.tuple_alfabet:
            self.letter = '*'
            self.direction = '<'
            self.number_of_state = self.second_condition
        elif self.letter in self.all_new_letter:
            self.direction = '>'
        elif self.letter == 'L':
            self.direction = '<'     # для теста, считает но оставляет звёзды и не делит, для нормы венуть на <
            self.number_of_state = self.fifth_condition

    def second_condition(self):
        """
            Идем до воскл. знака
        """
        self.direction = '<'
        if self.letter == '!':
            self.number_of_state = self.third_condition
        elif self.letter == '*':
            self.number_of_state = self.second_condition

    def third_condition(self):
        """
            Увеличиваем цифру возле воскл. знака, или же если она 9,
            то ставим 0 двигаем головку влево и увеличиваем там цифру на 1,
            далее всё заного
        """
        if self.letter in self.all_new_letter[1:-2]:
            self.letter = str(int(self.letter) + 1)     # получаем цифру на которой стоит и прибавляем 1 если это не 9
            self.direction = '>'
            self.number_of_state = self.first_condition
        elif self.letter == '9':
            self.letter = '0'
            self.direction = '<'

    def fourth_condition(self):
        """
            Затираем звёздочки
        """
        self.direction = '>'
        if self.letter == 'L':
            self.number_of_state = self.tenth_condition
        self.letter = 'L'

    def fifth_condition(self):
        """
            Доходим до воскл. знака.
        """
        self.direction = '<'
        if self.letter == '!':
            self.number_of_state = self.sixth_condition

    def sixth_condition(self):
        """
            В зависимости от того какое это число переходим в некст состояние
            0 -> q9
            нечетное -> q7
            чётное -> q8
        """
        self.direction = '>'
        if self.letter in ('1', '3', '5', '7', '9',):
            self.number_of_state = self.seventh_condition
        elif self.letter in ('2', '4', '6', '8'):
            self.number_of_state = self.eighth_condition
        elif self.letter == '0':
            self.direction = '<'
            self.number_of_state = self.ninth_condition

    def seventh_condition(self):
        """
            Нечетное число, значит пользователь по длине ввел плохое слово.
        """
        self.direction = '>'
        if self.letter == self.all_new_letter[-1]:
            self.letter = '0'
            self.number_of_state = self.fourth_condition

    def eighth_condition(self):
        """
            Четное число, значит продолжаем работу.
        """
        self.direction = '>'
        if self.letter == self.all_new_letter[-1]:
            self.letter = '1'
            self.number_of_state = self.fourth_condition

    def ninth_condition(self):
        """
            Если десяток, 0 то нечетное, если же он есть
            то четное.
        """
        self.direction = '>'
        if self.letter == self.all_new_letter[2:-1]:
            self.number_of_state = self.eighth_condition
        elif self.letter == '0':
            self.number_of_state = self.seventh_condition

    def tenth_condition(self):
        """
            Идем до воскл. и смотри на цифру возле него.
        """
        self.direction = '<'
        if self.letter == '!':
            self.direction = '>'
            self.number_of_state = self.eleventh_condition

    def eleventh_condition(self):
        """
            Смотрим на число:
                0 - нечетное -> q18
                1 - четное -> q12
        """
        self.direction = '<'
        if self.letter == '0':
            self.number_of_state = self.eighteenth_condition
        elif self.letter == '1':
            self.number_of_state = self.twelfth_condition

    def twelfth_condition(self):
        """
            Двигаемся к числу, а именно в самое начало слова.
        """
        self.direction = '<'
        if self.letter == 'L':
            self.direction = '>'
            self.number_of_state = self.thirteenth_condition

    def thirteenth_condition(self):
        """
            Делит десяток, и в зависимости от него двигается либо в
            14-ое состояние либо в 15-ое, в 15-ое если не четный (30, 50)
        """
        self.direction = '>'
        if self.letter in ('0', '2', '4', '6', '8'):
            if self.letter == '0':
                self.letter = '0'
            elif self.letter == '2':
                self.letter = '1'
            elif self.letter == '4':
                self.letter = '2'
            elif self.letter == '6':
                self.letter = '3'
            elif self.letter == '8':
                self.letter = '4'
            self.number_of_state = self.fourteenth_condition
        elif self.letter in ('1', '3', '5', '7', '9'):
            if self.letter == '1':
                self.letter = '0'
            elif self.letter == '3':
                self.letter = '1'
            elif self.letter == '5':
                self.letter = '2'
            elif self.letter == '7':
                self.letter = '3'
            elif self.letter == '9':
                self.letter = '4'
            self.number_of_state = self.fifteenth_condition

    def fourteenth_condition(self):
        """
            Делит четное число пополам.
        """
        self.direction = '>'
        self.number_of_state = self.sixteenth_condition
        if self.letter in ('2', '4', '6', '8'):
            if self.letter == '2':
                self.letter = '1'
            elif self.letter == '4':
                self.letter = '2'
            elif self.letter == '6':
                self.letter = '3'
            elif self.letter == '8':
                self.letter = '4'

    def fifteenth_condition(self):
        """
            Делит нечетное пополам.
        """
        self.direction = '>'
        self.number_of_state = self.sixteenth_condition
        if self.letter in ('0', '2', '4', '6', '8'):
            if self.letter == '0':
                self.letter = '5'
            elif self.letter == '2':
                self.letter = '6'
            elif self.letter == '4':
                self.letter = '7'
            elif self.letter == '6':
                self.letter = '8'
            elif self.letter == '8':
                self.letter = '9'

    def sixteenth_condition(self):
        """
            Затирает всё остальное кроме числа.
        """
        if self.letter == '!':
            self.letter = '*'
            self.direction = '>'
        elif self.letter in self.all_new_letter[1:3]:
            self.letter = 'L'
            self.direction = '<'
            self.number_of_state = self.seventeenth_condition

    def seventeenth_condition(self):
        """
            Затирает всё остальное кроме числа..
        """
        if self.letter in self.all_new_letter[1:]:
            if self.letter == '*':
                self.letter = 'L'
            self.direction = '<'
        elif self.letter == 'L':
            self.direction = 'stop'

    def eighteenth_condition(self):
        """
            Если кол-во букв нечётное, то оставляем 0.
        """
        if self.letter in self.all_new_letter[:-1]:
            self.letter = 'L'
            self.direction = '<'
        else:
            self.direction = '>'
            self.number_of_state = self.nineteenth_condition

    def nineteenth_condition(self):
        """
            Если кол-во букв нечётное, затираем всё кроме 0.
        """
        self.direction = '>'
        if self.letter == '0':
            self.direction = 'stop'


if __name__ == '__main__':
    pass

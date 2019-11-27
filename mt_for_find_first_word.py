from mt import mt


"""
    Машина тьюринга которая получает результаты первой мт(выводит кол-во букв в одном слово),
    вырезает и выводит ПЕРВОЕ слово из слова веденным пользователем.
    
    Как работает:
            Доходит до конца строки, затирает литеру, возвращается в начало,
        вычитает единицу, и начинает заного, когда число == 0, затирает число
        и выводит слово.
"""


class mt_for_find_first_word(mt):

    def first_condition(self):
        """
            Двигаемся до конца слова, когда достигнут конец переходим во второе состояние.
        """
        self.direction = '>'
        if self.letter == 'L':
            self.direction = '<'
            self.number_of_state = self.second_condition

    def second_condition(self):
        """
            Метим букву, изменяя её на звёздочку
        """
        self.direction = '<'
        if self.letter in self.tuple_alfabet:
            self.letter = '*'
            self.number_of_state = self.third_condition

    def third_condition(self):
        """
            Доходим до воскл. знака
        """
        self.direction = '<'
        if self.letter == '!':
            self.number_of_state = self.fourth_condition

    def fourth_condition(self):
        """
            Уменьшаем цифру на один которая вохле запятой
        """
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
        """
            Уменьшаем цифру на один которая вначале
        """
        self.direction = '>'
        if self.letter in self.all_new_letter[2:-1]:
            self.letter = str(int(self.letter) - 1)
            self.number_of_state = self.first_condition
        elif self.letter == '0':
            self.letter = 'L'
            self.number_of_state = self.sixth_condition

    def sixth_condition(self):
        """
            Затираем цифры, воскл знак, доходим до звезды, её стираем и выходим
        """
        self.direction = '>'
        if self.letter in ('!', '0', '9'):
            self.letter = 'L'
        elif self.letter == '*':
            self.letter = 'L'
        elif self.letter == 'L':
            self.letter = 'L'
            self.direction = 'stop'

    def seventh_condition(self):
        """
            Для нормальной работы с десятками, или же после того
            как цифра возле воскл знака стала 0, проверяем 0 это
            или 10-20-30...
        """
        self.direction = '>'
        if self.letter == '0':
            self.letter = 'L'
            self.number_of_state = self.sixth_condition
        elif self.letter == self.all_new_letter[2:]:
            self.number_of_state = self.first_condition


if __name__ == '__main__':
    pass

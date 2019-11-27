from mt import mt


"""
    Машина тьюринга которая получает результаты первой мт(выводит кол-во букв в одном слово),
    вырезает и выводит ВТОРОЕ слово из слова веденным пользователем.
    
    Как работает:
            Начинает с воскл. знака, идет вправо и затирает первый символ a b или c, после
        идет влево и после достижения первой любой от 0 до 9 цифры, уменьшает её на 1,
        и начинает работу заного, идет вправо затирает первый символ, влево и т.д.
        до тех пор пока счетчик не достигнет 0.
"""


class mt_for_find_second_word(mt):

    def first_condition(self):
        """
            Производим поиск литеры принадлежащей алфавиту, если находим,
            заменяем звездой и переходим во второе состояние.
        """
        if self.letter in self.tuple_alfabet:
            self.letter = '*'
            self.direction = '<'
            self.number_of_state = self.second_condition
        elif self.letter in self.all_new_letter:
            self.direction = '>'

    def second_condition(self):
        """
            Двигаемся к воскл. знаку, после его достижения переходим в третье состояние.
        """
        self.direction = '<'
        if self.letter == '!':
            self.number_of_state = self.third_condition

    def third_condition(self):
        """
            Вычитаем число. если это 2-9 то просто делаем -1 и начинаем всё по новой,
            если же 1 то тоже делаем -1 но переходим в состояние четыре, если же это
            0, заменяем его 9ой и идем в шестое состояние.
        """
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
        """
            Смотрим на число, если оно 0, то переходим в состояние пять, если нет
            то делаем со всеми числами -1 кроме единицы, и переходи во первое состояние.
        """
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
        """
            Смотрим на литеру, если эта литера принадлежит алфавиту, останавливаем мт,
            иначе затираем и идем дальше.
        """
        if self.letter in self.tuple_alfabet:
            self.direction = 'stop'
        elif self.letter in self.all_new_letter:
            self.letter = 'L'
            self.direction = '>'

    def sixth_condition(self):
        """
            Работает с десятками, то есть если кол-во букв больше 9 то
            десяток расчитывается в этом состоянии, а именно тоже происходит вычитание 1
            и переход в первое состояние.
        """
        self.direction = '>'
        if self.letter in self.all_new_letter[2:-1]:
            self.letter = str(int(self.letter) - 1)
            self.number_of_state = self.first_condition


if __name__ == '__main__':
    pass

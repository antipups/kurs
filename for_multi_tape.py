class mt_for_multi_tape():
    result_word = str()  # результирующее слово
    amount_of_steps = 0  # кол-во шагов для достижения целей
    tuple_alfabet = ('a', 'b', 'c')  # кортеж с литерами принадлежащим алфавиту

    state = None  # состояние, first_condition , second,
    # тем самым меняя указатели на функции

    direction_of_first_ribbon = '>'     # направление, в которое двигаемся на первой ленте, может быть >, <, stop
    direction_of_second_ribbon = '>'    # направление, в которое двигаемся на второй ленте
    letter_on_first_ribbon, letter_on_second_ribbon = str(), str()  # буква, которую мы сейчас рассматриваем
    cursor_on_first_ribbon, cursor_on_second_ribbon = 1, 0  # курсор , то что бегает по строке
    word_on_second_ribbon = ['_']

    """
        Машина тьюринга которая получает результаты второй(выдает первое слово) и третьей(выдает второе слово) мт,
        сравнивает эти слова, если они реверсивным выводит 1, если нет выводит 0.

        Как работает:
            Идет по первой ленте вправо, после каждых двух символов записывая единицу на вторую ленту.
        После, если кол-во нечетное, всё затирает, если чётное, то переводит все единицы снизу на буквы
        второй половины слова, то есть затирая одну букву на первой ленте, ставим её на вторую.
        После это манипуляции на первой ленте останется обычное слово, на второй реверсированное,
        сравниваем побуквенно попутно затирая, если всё прошло удачно ставим 1 выходим, иначе всё затираем
        ставим 0 и выходим.
    """

    def first_condition(self):
        """
            Если элемент есть в алфавите (а, b, c) то переходим в состояние 2;
            Если находим пустоту то переходим в состаяние 4.
        """
        if self.letter_on_first_ribbon in self.tuple_alfabet:
            self.direction_of_first_ribbon, self.direction_of_second_ribbon = '>', '.'
            self.state = self.second_condition
        elif self.letter_on_first_ribbon == '_':
            self.direction_of_first_ribbon, self.direction_of_second_ribbon = '<', '<'
            self.state = self.fourth_condition

    def second_condition(self):
        """
            Если не лямбда то добавляем на вторую ленту 1, и идем в первое состояние;
            Если лямбда то переходим в состояние 3.
        """
        if self.letter_on_first_ribbon in self.tuple_alfabet:
            self.letter_on_second_ribbon = '1'
            self.word_on_second_ribbon.append('_')      # так как поставили новый символ, закрыли его лямбдой
            self.direction_of_first_ribbon, self.direction_of_second_ribbon = '>', '>'
            self.state = self.first_condition
        elif self.letter_on_first_ribbon == '_':
            self.letter_on_first_ribbon, self.letter_on_second_ribbon = '_', '_'
            self.direction_of_first_ribbon, self.direction_of_second_ribbon = '<', '<'
            self.state = self.third_condition

    def third_condition(self):
        """
            Стираем всё на первой и на второй ленте и выводим 0.
        """
        if self.letter_on_first_ribbon != '_':  # если ещё не пуста, делаем её пустой
            self.letter_on_first_ribbon = '_'
        elif self.letter_on_first_ribbon == '_':    # если уже пуста, перестаем её чистить стопаем прогу и выводим 0
            self.letter_on_first_ribbon = '0'
            self.direction_of_first_ribbon = 'stop'

        if self.letter_on_second_ribbon != '_':     # если ещё не пуста, делаем её пустой
            self.letter_on_second_ribbon = '_'
        elif self.letter_on_second_ribbon == '_':   # если уже пуста, перестаем её чистить
            self.direction_of_second_ribbon = '.'

    def fourth_condition(self):
        """
            Двигаемся влево на обеих лентах, пока видим единицы на второй ленте
            записываем буквы с первой ленты на вторую, попутно на первой ленте затирая
            записанную только что букву. Когда закончились все единицы на второй ленте
            переходим в состояние 5.
        """
        self.direction_of_first_ribbon, self.direction_of_second_ribbon = '<', '<'
        if self.letter_on_second_ribbon == '_':
            self.direction_of_first_ribbon, self.direction_of_second_ribbon = '.', '>'  # точка - стоим на месте
            self.state = self.fifth_condition
            return
        elif self.letter_on_first_ribbon == 'a':
            self.letter_on_second_ribbon = 'a'
        elif self.letter_on_first_ribbon == 'b':
            self.letter_on_second_ribbon = 'b'
        elif self.letter_on_first_ribbon == 'c':
            self.letter_on_second_ribbon = 'c'
        self.letter_on_first_ribbon = '_'

    def fifth_condition(self):
        """
            Идем на первой ленте влево, на второй вправо, попутно сравнивая символы, если
            они равны, двигаем так до лямбд и ставим 1, если нет, то переходим в состояние 6.
        """
        self.direction_of_first_ribbon, self.direction_of_second_ribbon = '<', '>'
        if self.letter_on_first_ribbon == self.letter_on_second_ribbon == '_':
            self.letter_on_first_ribbon = '1'
            self.direction_of_first_ribbon = 'stop'
        elif self.letter_on_first_ribbon == self.letter_on_second_ribbon:
            self.letter_on_first_ribbon, self.letter_on_second_ribbon = '_', '_'
        else:
            self.letter_on_first_ribbon, self.letter_on_second_ribbon = '_', '_'
            self.state = self.sixth_condition

    def sixth_condition(self):
        """
            Затираем всё на лентах и ставим 0.
        """
        if self.letter_on_first_ribbon == '_':
            self.letter_on_first_ribbon = '0'
            self.direction_of_first_ribbon = 'stop'
            return
        self.letter_on_first_ribbon, self.letter_on_second_ribbon = '_', '_'
        self.direction_of_first_ribbon, self.direction_of_second_ribbon = '<', '>'

    def heart(self, word_on_first_ribbon, bot):
        """
            Логика такова, берем символы с первой и второй ленты, а именно с мест на которых стоят курсоры,
            после идем в состояние, где происходит замена или нет состояния/ самой буквы/ направления,
            выходим из состояния, и присваиваем новые значения переменным, а именно, старые буквы
            на старых местах меняем на новые, смотрим на направление и меняем курсор если оно изменилось.
        """

        self.state = self.first_condition   # привязываем первое состояние к номеру состояния,
                                            # или же на каком состоянии мы стартуем
        word_on_first_ribbon = list(word_on_first_ribbon)
        while True:
            self.amount_of_steps += 1

            self.letter_on_first_ribbon = word_on_first_ribbon[self.cursor_on_first_ribbon]
            self.letter_on_second_ribbon = self.word_on_second_ribbon[self.cursor_on_second_ribbon]

            self.state()

            word_on_first_ribbon[self.cursor_on_first_ribbon] = self.letter_on_first_ribbon
            self.word_on_second_ribbon[self.cursor_on_second_ribbon] = self.letter_on_second_ribbon

            if self.direction_of_second_ribbon == '>':  # двигаемся на второй ленте
                self.cursor_on_second_ribbon += 1
            elif self.direction_of_second_ribbon == '<':
                self.cursor_on_second_ribbon -= 1

            if self.direction_of_first_ribbon == '>':   # двигаемся на первой
                self.cursor_on_first_ribbon += 1
            elif self.direction_of_first_ribbon == '<':
                self.cursor_on_first_ribbon -= 1
            elif self.direction_of_first_ribbon == 'stop':
                self.result_word = ''.join(word_on_first_ribbon).replace('_', '')
                return


if __name__ == '__main__':
    mt = mt_for_multi_tape()
    mt.heart('_cbaabc_', bot=False)
    print(mt.result_word)
    pass

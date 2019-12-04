class mt_for_multi_tape():
    result_word = str()  # результирующее слово
    amount_of_steps = 0  # кол-во шагов для достижения целей
    tuple_alfabet = ('a', 'b', 'c')  # кортеж с литерами принадлежащим алфавиту

    state = None  # состояние, first_condition , second,
    # тем самым меняя указатели на функции

    direction_of_first_ribbon = '>'     # направление, в которое двигаемся на первой ленте, может быть >, <, stop
    direction_of_second_ribbon = '>'    # направление, в которое двигаемся на второй ленте
    letter_on_first_ribbon, letter_on_second_ribbon = str(), str()  # буква, которую мы сейчас рассматриваем
    cursor_on_first_ribbon, cursor_on_second_ribbon = int(), 0  # курсор , то что бегает по строке
    word_on_second_ribbon = list('_')

    """
        Машина тьюринга которая получает результаты второй(выдает первое слово) и третьей(выдает второе слово) мт,
        сравнивает эти слова, если они реверсивным выводит 1, если нет выводит 0.

        Как работает:
            
    """

    def first_condition(self):
        """
            Если элемент есть в алфавите (а, b, c) то переходим в состояние 2;
            Если находим пустоту то переходим в состаяние 4.
        """
        if self.letter_on_first_ribbon in self.tuple_alfabet:
            self.state = self.second_condition
            self.direction_of_first_ribbon = '>'
            self.direction_of_second_ribbon = 'stop'
        elif self.letter_on_first_ribbon == '_':
            self.state = self.fourth_condition
            self.direction_of_first_ribbon = '<'
            self.direction_of_second_ribbon = '<'

    def second_condition(self):
        if self.letter_on_first_ribbon in self.tuple_alfabet:
            self.letter_on_second_ribbon += '1'
            self.direction_of_first_ribbon = '>'
            self.direction_of_second_ribbon = '>'
            self.state = self.first_condition
        elif self.letter_on_first_ribbon == '_':
            self.letter_on_first_ribbon = '_'
            self.letter_on_second_ribbon = '_'
            self.direction_of_first_ribbon = '<'
            self.direction_of_second_ribbon = '<'
            self.state = self.third_condition

    def third_condition(self):
        pass

    def fourth_condition(self):
        pass

    def fifth_condition(self):
        pass

    def sixth_condition(self):
        pass

    def heart(self, word_on_first_ribbon, cursor_of_first_ribbon, bot):
        self.state = self.first_condition   # привязываем первое состояние к номеру состояния,
                                            # или же на каком состоянии мы стартуем
        self.cursor_on_first_ribbon = cursor_of_first_ribbon
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
            else:
                self.result_word = ''.join(word_on_first_ribbon).replace('_', '')
                return


if __name__ == '__main__':
    mt = mt_for_multi_tape()
    mt.heart('_abba_', cursor_of_first_ribbon=1, bot=False)
    print(mt.result_word)
    pass

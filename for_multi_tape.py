class mt_for_multi_tape:
    result_word = str()  # результирующее слово
    amount_of_steps = 0  # кол-во шагов для достижения целей
    tuple_alfabet = ('a', 'b', 'c')  # кортеж с литерами принадлежащим алфавиту

    state = None            # переключатель состояний
    number_state = str()    # номер состояния (для логов)

    direction_of_first_ribbon = '>'     # направление, в которое двигаемся на ПЕРВОЙ ленте, может быть >, <, stop, .
    direction_of_second_ribbon = '.'    # направление, в которое двигаемся на ВТОРОЕЙ ленте
    direction_of_third_ribbon = '.'     # направление, в которое двигаемся на ТРЕТЕЙ ленте
    direction_of_fourth_ribbon = '.'    # направление, в которое двигаемся на ЧЕТВЕРТОЙ ленте
    letter_on_first_ribbon, letter_on_second_ribbon, letter_on_third_ribbon, letter_on_fourth_ribbon = \
        str(), str(), str(), str(),  # буква, которую мы сейчас рассматриваем
    cursor_on_first_ribbon, cursor_on_second_ribbon, cursor_on_third_ribbon, cursor_on_fourth_ribbon =\
        0, 0, 0, 0  # курсор , то что бегает по строке

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
                Считаем кол-во всех букв, а именно: нашли букву A, записали 1 на вторую ленту,
            B - на третью, C - на четвертую, после, если нашли ещё одну A B или С ставим ещё
            одну (считаем кол-во каждой буквы в унарном коде), после завершения (когда добрались
            до пустоты) переходим в состояние 2.
        """
        self.number_state = '1'
        if self.letter_on_first_ribbon == 'a':
            self.letter_on_second_ribbon = '1'
            self.direction_of_first_ribbon, self.direction_of_second_ribbon = '>', '>'
            self.direction_of_third_ribbon, self.direction_of_fourth_ribbon = '.', '.'
        elif self.letter_on_first_ribbon == 'b':
            self.letter_on_third_ribbon = '1'
            self.direction_of_first_ribbon, self.direction_of_third_ribbon = '>', '>'
            self.direction_of_second_ribbon, self.direction_of_fourth_ribbon = '.', '.'
        elif self.letter_on_first_ribbon == 'c':
            self.letter_on_fourth_ribbon = '1'
            self.direction_of_first_ribbon, self.direction_of_fourth_ribbon = '>', '>'
            self.direction_of_second_ribbon, self.direction_of_third_ribbon = '.', '.'
        elif self.letter_on_first_ribbon == '_':
            self.direction_of_first_ribbon, self.direction_of_second_ribbon, self.direction_of_third_ribbon, self.direction_of_fourth_ribbon = \
                '.', '.', '<', '.'
            self.state = self.second_condition

    def second_condition(self):
        """
            Делаем проверку j >= 1; Если верно, то идем в состояние 3, если нет - в состояние 4.
        """
        self.number_state = '2'
        if self.letter_on_third_ribbon == '1':
            self.direction_of_third_ribbon, self.direction_of_first_ribbon, self.direction_of_second_ribbon =\
                '.', '.', '<'
            self.state = self.third_condition
        elif self.letter_on_third_ribbon == '_':
            self.direction_of_third_ribbon, self.direction_of_first_ribbon, self.direction_of_second_ribbon, self.direction_of_fourth_ribbon =\
                '.', '<', '<', '<'
            self.state = self.fourth_condition

    def third_condition(self):
        """
                Находим минимум из первой и второй ленты, после переходим в состояние 5, если на первой
            ленте меньшее, или же в состояние 6, если на второй ленте меньшее.
        """
        self.number_state = '3'
        if self.letter_on_third_ribbon == '1' and self.letter_on_second_ribbon == '1':
            self.letter_on_third_ribbon, self.letter_on_second_ribbon = 'A', 'A'
            self.direction_of_third_ribbon = '<'
        elif self.letter_on_third_ribbon == '_':
            self.direction_of_third_ribbon, self.direction_of_second_ribbon, self.direction_of_fourth_ribbon = '>', '.', '<'
            self.state = self.fifth_condition
        elif self.letter_on_second_ribbon == '_':
            self.direction_of_second_ribbon, self.direction_of_first_ribbon, self.direction_of_fourth_ribbon = '>', '.', '<'
            self.state = self.sixth_condition

    def fourth_condition(self):
        """
            Затираем все ленты и ставим 0, после чего завершаем работу программы.
        """
        self.number_state = '4'
        if self.letter_on_first_ribbon == '_':
            self.letter_on_first_ribbon = '0'
            self.direction_of_first_ribbon = 'stop'
            return
        else:

            self.letter_on_first_ribbon = '_'
            if self.letter_on_second_ribbon == '_':
                self.direction_of_second_ribbon = '.'
            else:
                self.letter_on_second_ribbon = '_'

            if self.letter_on_third_ribbon == '_':
                self.direction_of_third_ribbon = '.'
            else:
                self.letter_on_third_ribbon = '_'

            if self.letter_on_fourth_ribbon == '_':
                self.direction_of_fourth_ribbon = '.'
            else:
                self.letter_on_fourth_ribbon = '_'

    def fifth_condition(self):
        """
                Состояние сравнивает кол-во единиц на третьей и четвертой ленте, если их равно
            то переходим в состояние 7, иначе в 4.
        """
        self.number_state = '5'
        if self.letter_on_third_ribbon == 'A' and self.letter_on_fourth_ribbon == '1':
            self.letter_on_third_ribbon, self.letter_on_fourth_ribbon = '_', '_'
        elif self.letter_on_third_ribbon == '_' and self.letter_on_fourth_ribbon == '_':
            self.direction_of_third_ribbon, self.direction_of_fourth_ribbon = '.', '.'
            self.state = self.seventh_condition
        elif self.letter_on_third_ribbon == 'A' and self.letter_on_fourth_ribbon == '_':
            self.direction_of_fourth_ribbon, self.direction_of_second_ribbon, self.direction_of_first_ribbon =\
                '.', '>', '<'
            self.state = self.fourth_condition

        elif self.letter_on_third_ribbon == '_' and self.letter_on_fourth_ribbon == '1':
            self.direction_of_third_ribbon, self.direction_of_second_ribbon, self.direction_of_first_ribbon =\
                '.', '>', '<'
            self.state = self.fourth_condition

    def sixth_condition(self):
        """
                Состояние сравнивает кол-во единиц на второй и четвертой ленте, если их равно
            то переходим в состояние 7, иначе в 4.
        """
        if self.letter_on_second_ribbon == 'A' and self.letter_on_fourth_ribbon == '1':
            self.letter_on_second_ribbon, self.letter_on_fourth_ribbon = '_', '_'
        elif self.letter_on_second_ribbon == '_' and self.letter_on_fourth_ribbon == '_':
            self.direction_of_second_ribbon, self.direction_of_fourth_ribbon = '.', '.'
            self.state = self.seventh_condition
        elif self.letter_on_second_ribbon == 'A' and self.letter_on_fourth_ribbon == '_':
            self.direction_of_fourth_ribbon, self.direction_of_third_ribbon, self.direction_of_first_ribbon = \
                '.', '>', '<'
            self.state = self.fourth_condition

        elif self.letter_on_third_ribbon == '_' and self.letter_on_fourth_ribbon == '1':
            self.direction_of_second_ribbon, self.direction_of_third_ribbon, self.direction_of_first_ribbon = \
                '.', '>', '<'
            self.state = self.fourth_condition

    def seventh_condition(self):
        """
            Состояние затирает все ленты и ставит 1, после, останавливает программу.
        """
        if self.letter_on_first_ribbon == '_':
            self.letter_on_first_ribbon = '1'
            self.direction_of_first_ribbon = 'stop'
            return
        else:

            self.letter_on_first_ribbon = '_'
            if self.letter_on_second_ribbon == '_':
                self.direction_of_second_ribbon = '.'
            else:
                self.letter_on_second_ribbon = '_'

            if self.letter_on_third_ribbon == '_':
                self.direction_of_third_ribbon = '.'
            else:
                self.letter_on_third_ribbon = '_'

            if self.letter_on_fourth_ribbon == '_':
                self.direction_of_fourth_ribbon = '.'
            else:
                self.letter_on_fourth_ribbon = '_'

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
        word_on_second_ribbon = ['_']
        word_on_third_ribbon = ['_']
        word_on_fourth_ribbon = ['_']

        while True:
            self.amount_of_steps += 1

            self.letter_on_first_ribbon = word_on_first_ribbon[self.cursor_on_first_ribbon]
            self.letter_on_second_ribbon = word_on_second_ribbon[self.cursor_on_second_ribbon]
            # print(self.cursor_on_third_ribbon, word_on_third_ribbon)
            self.letter_on_third_ribbon = word_on_third_ribbon[self.cursor_on_third_ribbon]
            self.letter_on_fourth_ribbon = word_on_fourth_ribbon[self.cursor_on_fourth_ribbon]
            temp_letter = self.letter_on_first_ribbon
            temp_second_letter = self.letter_on_second_ribbon
            temp_third_letter = self.letter_on_third_ribbon
            temp_fourth_letter = self.letter_on_fourth_ribbon

            # print(self.letter_on_third_ribbon)
            self.state()

            word_on_first_ribbon[self.cursor_on_first_ribbon] = self.letter_on_first_ribbon
            word_on_second_ribbon[self.cursor_on_second_ribbon] = self.letter_on_second_ribbon
            word_on_third_ribbon[self.cursor_on_third_ribbon] = self.letter_on_third_ribbon
            word_on_fourth_ribbon[self.cursor_on_fourth_ribbon] = self.letter_on_fourth_ribbon
            print(word_on_first_ribbon, word_on_second_ribbon, word_on_third_ribbon, word_on_fourth_ribbon)
            if word_on_second_ribbon[self.cursor_on_second_ribbon] == '1':
                word_on_second_ribbon.append('_')
            if word_on_third_ribbon[self.cursor_on_third_ribbon] == '1':
                word_on_third_ribbon.append('_')
            if word_on_fourth_ribbon[self.cursor_on_fourth_ribbon] == '1':
                word_on_fourth_ribbon.append('_')

            # if bot is False:
            #     with open('multi_log.txt', 'a') as f:
            #         temp_first_word = ''.join(word_on_first_ribbon[:self.cursor_on_first_ribbon]) + '(' + temp_letter.upper() + ')' + ''.join(word_on_first_ribbon[1 + self.cursor_on_first_ribbon:])
            #         if self.cursor_on_second_ribbon != -1:
            #             temp_second_word = ''.join(word_on_second_ribbon[:self.cursor_on_second_ribbon]) + '(' + temp_second_letter.upper() + ')' + ''.join(word_on_second_ribbon[1 + self.cursor_on_second_ribbon:])
            #         f.write('\n\n' + str(self.amount_of_steps) + '\tq' + self.number_state + '\t' + temp_first_word + '\n\t' + temp_second_word)

            if self.direction_of_second_ribbon == '>':  # двигаемся на ВТОРОЙ ленте
                self.cursor_on_second_ribbon += 1
            elif self.direction_of_second_ribbon == '<':
                self.cursor_on_second_ribbon -= 1

            if self.direction_of_third_ribbon == '>':  # двигаемся на ТРЕТЬЕЙ ленте
                self.cursor_on_third_ribbon += 1
            elif self.direction_of_third_ribbon == '<':
                self.cursor_on_third_ribbon -= 1

            if self.direction_of_fourth_ribbon == '>':  # двигаемся на ЧЕТВЕРТОЙ ленте
                self.cursor_on_fourth_ribbon += 1
            elif self.direction_of_fourth_ribbon == '<':
                self.cursor_on_fourth_ribbon -= 1

            if self.direction_of_first_ribbon == '>':   # двигаемся на ПЕРВОЙ ленте
                self.cursor_on_first_ribbon += 1
            elif self.direction_of_first_ribbon == '<':
                self.cursor_on_first_ribbon -= 1
            elif self.direction_of_first_ribbon == 'stop':
                print(word_on_first_ribbon)
                self.result_word = ''.join(word_on_first_ribbon).replace('_', '')
                return


if __name__ == '__main__':
    mt = mt_for_multi_tape()
    mt.heart('abbaaacbcc_', bot=False)
    print(mt.result_word)
    pass

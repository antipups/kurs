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
            self.direction_of_first_ribbon, self.direction_of_second_ribbon = '<', '>'
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
            self.direction_of_first_ribbon, self.direction_of_third_ribbon = '<', '>'
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
                Вначале считаем кол-во символов a, b, c. После, проводим манипуляции с этим кол-вом,
            записывали кол-во этих литер на вторую, третью, и четвертую ленту соответственно.
                За всё это отвечало первое состояние, оно смотрело на символ и в зависимости от того
            какой он записывало на вторую (если а), третью (если б), четвертую (если с).
                После, переходим во второе состояние, где делаем проверку j >= 1, если всё сработало
            переходим в третье состояние, если нет, в четвертое, которое всё затирает и ставит 0.
                В третьем состоянии мы ищем минимум, путем переделывания символов 1 на A, после дохода
            на одной из лент до лямбды, переходим в пятое или шестое состояние соответственно (5-ое для
            минимума на третьей, 6-ое для минимума на второй).
                В пятом / шестом состоянии сверяем кол-во символов и там и там, попутно затирая их,
            если символов по кол-ву равно, то переходим в седьмое состояние, всё стираем, и ппишем единицу.
            Иначе в четвертое.
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
            # print(word_on_first_ribbon, word_on_second_ribbon, word_on_third_ribbon, word_on_fourth_ribbon)
            if word_on_second_ribbon[self.cursor_on_second_ribbon] == '1':
                word_on_second_ribbon.append('_')
            if word_on_third_ribbon[self.cursor_on_third_ribbon] == '1':
                word_on_third_ribbon.append('_')
            if word_on_fourth_ribbon[self.cursor_on_fourth_ribbon] == '1':
                word_on_fourth_ribbon.append('_')

            if bot is False:
                with open('multi_log.txt', 'a') as f:
                    temp_first_word = ''.join(word_on_first_ribbon[:self.cursor_on_first_ribbon]) + '(' + temp_letter.upper() + ')' + ''.join(word_on_first_ribbon[1 + self.cursor_on_first_ribbon:])
                    if self.cursor_on_second_ribbon <= 0:
                        temp_second_word = ''.join(word_on_second_ribbon[:self.cursor_on_second_ribbon]) + '(' + temp_second_letter.upper() + ')'
                    else:
                        temp_second_word = ''.join(word_on_second_ribbon[:self.cursor_on_second_ribbon]) + '(' + temp_second_letter.upper() + ')' + ''.join(word_on_second_ribbon[1 + self.cursor_on_second_ribbon:])
                    if self.cursor_on_third_ribbon <= 0:
                        temp_third_word = ''.join(word_on_third_ribbon[:self.cursor_on_third_ribbon]) + '(' + temp_third_letter.upper() + ')'
                    else:
                        temp_third_word = ''.join(word_on_third_ribbon[:self.cursor_on_third_ribbon]) + '(' + temp_third_letter.upper() + ')' + ''.join(word_on_third_ribbon[1 + self.cursor_on_third_ribbon:])
                    if self.cursor_on_fourth_ribbon <= 0:
                        temp_fourth_word = ''.join(word_on_fourth_ribbon[:self.cursor_on_fourth_ribbon]) + '(' + temp_fourth_letter.upper() + ')'
                    else:
                        temp_fourth_word = ''.join(word_on_fourth_ribbon[:self.cursor_on_fourth_ribbon]) + '(' + temp_fourth_letter.upper() + ')' + ''.join(word_on_fourth_ribbon[1 + self.cursor_on_fourth_ribbon:])
                    f.write('\n\nНомер шага:' + str(self.amount_of_steps) + '\nСостояние - q' + self.number_state +
                            '\n\t1-ая лента: ' + temp_first_word +
                            '\n\t2-ая лента: ' + temp_second_word +
                            '\n\t3-ья лента: ' + temp_third_word +
                            '\n\t4-ая лента: ' + temp_fourth_word)

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
                # print(word_on_first_ribbon)
                self.result_word = ''.join(word_on_first_ribbon).replace('_', '')
                return


if __name__ == '__main__':
    mt = mt_for_multi_tape()
    mt.heart('ccaaabbbc_', bot=False)
    # print(mt.result_word)
    pass

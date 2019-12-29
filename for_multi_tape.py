class mt_for_multi_tape:
    result_word = str()  # результирующее слово
    amount_of_steps = 0  # кол-во шагов для достижения целей

    state = None            # переключатель состояний
    number_state = str()    # номер состояния (для логов)

    direction_of_first_ribbon = '>'     # направление, в которое двигаемся на ПЕРВОЙ ленте, может быть >, <, stop, .
    direction_of_second_ribbon = '.'    # направление, в которое двигаемся на ВТОРОЕЙ ленте
    direction_of_third_ribbon = '.'     # направление, в которое двигаемся на ТРЕТЕЙ ленте
    letter_on_first_ribbon, letter_on_second_ribbon, letter_on_third_ribbon = \
        str(), str(), str()  # буква, которую мы сейчас рассматриваем
    cursor_on_first_ribbon, cursor_on_second_ribbon, cursor_on_third_ribbon =\
        0, 0, 0  # курсор , то что бегает по строке

    def first_condition(self):
        """
                Состояние в котором мы находим букву A или C,
            и если нашли A идём в состояние 3, если C в состояние 4,
            иначе, если нашли букву D на нечётной позиции то всё стираем
            ибо это невозможно.
                Если мы дошли до лямбды, то переходим в состояние 5.
        """
        self.number_state = '1'
        self.direction_of_second_ribbon, self.direction_of_third_ribbon = '.', '.'  # останавливаем вторую, третью ленты
        if self.letter_on_first_ribbon == 'a':
            self.state = self.third_condition
        elif self.letter_on_first_ribbon == 'c':
            self.state = self.fourth_condition
        elif self.letter_on_first_ribbon == '_':
            self.state = self.fifth_condition
            self.direction_of_first_ribbon, self.direction_of_third_ribbon = '.', '<'
        elif self.letter_on_first_ribbon == 'd':
            self.direction_of_first_ribbon, self.direction_of_second_ribbon, self.direction_of_third_ribbon = '<', '<', '<'
            self.state = self.second_condition

    def second_condition(self):
        """
            Состояние в котором стираем всё и ставим 0.
        """
        self.number_state = '2'

        if self.letter_on_first_ribbon == self.letter_on_third_ribbon == self.letter_on_second_ribbon == '_':   # если все ленты пусты, останавливаем мт
            self.letter_on_first_ribbon = '0'
            self.direction_of_first_ribbon = 'stop'
            return

        if self.letter_on_first_ribbon != '_':  # затираем первую строку
            self.letter_on_first_ribbon = '_'
        elif self.letter_on_first_ribbon == '_':
            self.direction_of_first_ribbon = '.'

        if self.letter_on_second_ribbon != '_':  # затираем вторую строку
            self.letter_on_second_ribbon = '_'
        elif self.letter_on_second_ribbon == '_':
            self.direction_of_second_ribbon = '.'

        if self.letter_on_third_ribbon != '_':  # затираем третью строку
            self.letter_on_third_ribbon = '_'
        elif self.letter_on_third_ribbon == '_':
            self.direction_of_third_ribbon = '.'

    def third_condition(self):
        """
                На чётном месте всегда будет буква D, она и закрепляющая,
            если нашли её в этом состоянии, на вторую ленту ставим 1, тем
            самым подсчитывая кол-во AD в унарном коде.
        """
        self.number_state = '3'
        if self.letter_on_first_ribbon == 'd':
            self.state = self.first_condition
            self.letter_on_second_ribbon = '1'
            self.direction_of_second_ribbon = '>'
        elif self.letter_on_first_ribbon in ('a', 'c', '_'):
            self.direction_of_first_ribbon, self.direction_of_second_ribbon, self.direction_of_third_ribbon = '<', '<', '<'
            self.state = self.second_condition

    def fourth_condition(self):
        """
                Тоже состояние что и третье, только для комбинации CD и
            ставим единицу не на вторую ленту а на третью.
        """
        self.number_state = '4'
        if self.letter_on_first_ribbon == 'd':
            self.state = self.first_condition
            self.letter_on_third_ribbon = '1'
            self.direction_of_third_ribbon = '>'
        elif self.letter_on_first_ribbon in ('a', 'c', '_'):
            self.direction_of_first_ribbon, self.direction_of_second_ribbon, self.direction_of_third_ribbon = '<', '<', '<'
            self.state = self.second_condition

    def fifth_condition(self):
        """
                Состояние на проверку кол-во CD, а именно, то что их кол-во > 1.
            Если мы видим хоть одну единицу, идём в состояние 6, иначе в 2.
        """
        self.number_state = '5'
        if self.letter_on_third_ribbon == '1':
            self.direction_of_second_ribbon, self.direction_of_third_ribbon = '<', '.'
            self.state = self.sixth_condition
        elif self.letter_on_third_ribbon == '_':
            self.direction_of_first_ribbon, self.direction_of_second_ribbon, self.direction_of_third_ribbon = '<', '<', '.'
            self.state = self.second_condition

    def sixth_condition(self):
        """
                Состояние смотрит есть ли единица на третьей ленте, и
            если таковая там имеется, то смотрим есть ли единица на
            второй, если есть то идём в состояние 7, иначе в 2.
        """
        self.number_state = '6'
        self.direction_of_third_ribbon = '.'
        if self.letter_on_third_ribbon == '1':
            if self.letter_on_second_ribbon == '1':
                self.letter_on_second_ribbon = '_'
                self.state = self.seventh_condition
            elif self.letter_on_second_ribbon == '_':
                self.direction_of_first_ribbon, self.direction_of_second_ribbon, self.direction_of_third_ribbon = '<', '.', '<'
                self.state = self.second_condition
        elif self.letter_on_third_ribbon == '_' and self.letter_on_second_ribbon == '_':
            self.direction_of_second_ribbon, self.direction_of_first_ribbon = '.', '<'
            self.state = self.eigth_condition
        elif self.letter_on_third_ribbon == '_' and self.letter_on_second_ribbon == '1':
            self.direction_of_second_ribbon, self.direction_of_first_ribbon = '<', '<'
            self.state = self.second_condition

    def seventh_condition(self):
        """
                Состояние проверяет наличие 2-ой единицы на второй ленте, на
            одну единицу на третьей, то есть 2 единицы на второй = 1 на третьей,
            если так то всё нормально, идём в состояние 6, иначе в 2.
        """
        self.number_state = '7'
        if self.letter_on_second_ribbon == '1':
            self.letter_on_third_ribbon, self.letter_on_second_ribbon = '_', '_'
            self.direction_of_third_ribbon = '<'
            self.state = self.sixth_condition
        elif self.letter_on_second_ribbon == '_':
            self.direction_of_first_ribbon, self.direction_of_second_ribbon, self.direction_of_third_ribbon = '<', '.', '<'
            self.state = self.second_condition

    def eigth_condition(self):
        self.number_state = '8'
        if self.letter_on_first_ribbon != '_':
            self.letter_on_first_ribbon = '_'
        elif self.letter_on_first_ribbon == '_':
            self.letter_on_first_ribbon = '1'
            self.direction_of_first_ribbon = 'stop'

    def heart(self, word_on_first_ribbon, bot):
        """
                Сердце мт, здесь выполняется эмуляция самой задумки машины тьюринга,
            а именно, есть строка, или несколько строк в случае с многоленточной мт,
            по которой бегает цикл(бесконечный), напрвление которого генерируется с
            помощью состояний, и так же после передвижения идёт запись буквы, на ко-
            торой нгаходится головка. Ниже написано что за что отвечает:
                - self.state - состояние в котором мы сейчас находимся (указатель на
            функцию, first_cond., second_cond и т.д.);
                - word_of_first_ribbon, ...second_ribbon, ...third_ribbon - строки,
            или же списки (так как строки в python константы), в которых находятся
            слова, 1 символ - 1 ячейка списка.
                - self.letter_on_first, ...second, ...third - буква которую мы будем
            обрабатывать, или же буква на которой стоит головка
                - self.direction_of_first, ...second, ...third - направление движения
            головки на определенных лентах.
                - self.cursor_on_first, ...second, ...third - индекс элемента в списке,
            на котором мт сейчас находится.
                - temp_letter, ...second_letter, ...third_letter - записываем буквы для
            логов
        """

        self.state = self.first_condition   # привязываем первое состояние к номеру состояния,
                                            # или же на каком состоянии мы стартуем
        word_on_first_ribbon = list(word_on_first_ribbon)
        word_on_second_ribbon = ['_']
        word_on_third_ribbon = ['_']

        while True:
            self.amount_of_steps += 1

            self.letter_on_first_ribbon = word_on_first_ribbon[self.cursor_on_first_ribbon]
            self.letter_on_second_ribbon = word_on_second_ribbon[self.cursor_on_second_ribbon]
            self.letter_on_third_ribbon = word_on_third_ribbon[self.cursor_on_third_ribbon]

            temp_letter = self.letter_on_first_ribbon
            temp_second_letter = self.letter_on_second_ribbon
            temp_third_letter = self.letter_on_third_ribbon

            self.state()
            # print('====================', self.amount_of_steps, '====================')
            # print(word_on_first_ribbon)
            # print(word_on_second_ribbon)
            # print(word_on_third_ribbon)
            word_on_first_ribbon[self.cursor_on_first_ribbon] = self.letter_on_first_ribbon
            word_on_second_ribbon[self.cursor_on_second_ribbon] = self.letter_on_second_ribbon
            word_on_third_ribbon[self.cursor_on_third_ribbon] = self.letter_on_third_ribbon
            if word_on_second_ribbon[self.cursor_on_second_ribbon] == '1':
                word_on_second_ribbon.append('_')
            if word_on_third_ribbon[self.cursor_on_third_ribbon] == '1':
                word_on_third_ribbon.append('_')

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
                    f.write('\n\nНомер шага:' + str(self.amount_of_steps) + '\nСостояние - q' + self.number_state +
                            '\n\t1-ая лента: ' + temp_first_word +
                            '\n\t2-ая лента: ' + temp_second_word +
                            '\n\t3-ья лента: ' + temp_third_word)

            if self.direction_of_second_ribbon == '>':  # двигаемся на ВТОРОЙ ленте
                self.cursor_on_second_ribbon += 1
            elif self.direction_of_second_ribbon == '<':
                self.cursor_on_second_ribbon -= 1

            if self.direction_of_third_ribbon == '>':  # двигаемся на ТРЕТЬЕЙ ленте
                self.cursor_on_third_ribbon += 1
            elif self.direction_of_third_ribbon == '<':
                self.cursor_on_third_ribbon -= 1

            if self.direction_of_first_ribbon == '>':   # двигаемся на ПЕРВОЙ ленте
                self.cursor_on_first_ribbon += 1
            elif self.direction_of_first_ribbon == '<':
                self.cursor_on_first_ribbon -= 1
            elif self.direction_of_first_ribbon == 'stop':
                self.result_word = ''.join(word_on_first_ribbon).replace('_', '').replace('a', '').replace('b', '').replace('c', '')
                return


if __name__ == '__main__':
    mt = mt_for_multi_tape()
    mt.heart('adadadadcdcd_', bot=False)
    print(mt.result_word)
    pass
    # тест

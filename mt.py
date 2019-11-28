class mt:
    result_word = str()
    tuple_alfabet = ('a', 'b', 'c')     # кортеж с литерами принадлежащим алфавиту
    number_of_state = 1     # номер состояния, 2, 3 и т.д, позже first_condition , second,
                            # тем самым меняя указатели на функции
    direction = '>'         # направление, в которое двигаемся , может быть >, <, stop
    letter = '1'            # буква, которую мы сейчас рассматриваем
    cursor = 1              # курсор , то что бегает по строке

    all_new_letter = ('!', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*')   # дополнительный алфавит который я добавил

    def first_condition(self):
        """
            Функция состояния, условие - что делаем с символом на котором стоит,
            пример :
                if self.letter == '1':       # если заданный символ один (функция получает символ)
                    self.letter = '0'       # меняем букву, если прописано, то изменяем если не прописано то остается как было

                    self.direction = '>'    # изменяем направление движения, если прописано то изменяем, если нет, то остается как и было

                    self.number_of_state = self.second_condition            # в какое состояние переходим, 1 - функция называет first, 2 - second,
                                                                       # сколько состояний столько и методов состояний
                                                                       # если прописано, то изменяем если не прописано то остается как было

            Порядок именно такой, вначале идут то что меняется 100% и на что, допустим direction = '>' ,
            и только потом то, что меняется в зависимости от литеры.
        """
        pass

    def second_condition(self):
        pass

    def third_condition(self):
        pass

    def fourth_condition(self):
        pass

    def fifth_condition(self):
        pass

    def sixth_condition(self):
        pass

    def seventh_condition(self):
        pass

    def eighth_condition(self):
        pass

    def ninth_condition(self):
        pass

    def tenth_condition(self):
        pass

    def heart(self, word, cursor):
        """
            Сердце машины, то есть её работа, всё прописано тут, как она идет по состояниям, что возвращаем и т.д.

            Подробное описание:
                    При передачи слова в данную функцию, мы ставим текущее состояние на первое
                (меняем указатель переменной на функцию первого состояни), ставим головку в
                нужное место (курсор), далее преобразуем слово которое ввел пользователь
                из строки в список, для того чтоб можно было изменять в нем элементы, ибо
                строки в Python константны.
                    После всех приготовлений, переходим в цикл, который и будет выполнять
                всю работу по перемещению головки и захода в состояния.
                    Вначале мы берем из списка литеру на которой стоит головка(курсор),
                если не получается это сделать(ошибка) то это скорее всего из-за того что мы
                вышли за прописанные пределы (по умолчанию, слово веденное пользователем обрамляеся
                двумя L слева и справа, иногда требуется дойти до константы дальше, и для этого придумано
                выкидывание исключения, и если это произошло, просто добавляем константу L в конец списка,
                ВОЗМОЖНО кастыль:( ). После того как взяли нужную литеру переходи в состояние, на котором
                стоим, в нем проделываем нужные махинации и возвращаемся сюда. Тут, меняем литеру если её
                изменяли в состоянии, и с помозью условия и проверки переменной self.direction двигаемся
                либо, вправо влево, или останавливаемся, движения происходят увеличением или уменьшением
                переменной self.cursor. Если мт закончила свою работу, удаляем лишние L из списка,
                преобразовываем список в строку и возвращаем новое слово.
        """
        self.number_of_state = self.first_condition     # привязываем первое состояние к номеру состояния,
                                                        # или же на каком состоянии мы стартуем
        self.cursor = cursor    # с какой позиции стартовать, мт не всегда стартует с первой позиции
        word = list(word)   # преобразуем строку в список
        while True:     # бесконечный цикл, это и есть некая головка, которая будет ходить по литерам
            # print(word)
            try:
                self.letter = word[self.cursor]      # получаем литеру на которой стоит головка
            except IndexError:  # если произошел выход за строку
                word.append('L')
            self.number_of_state()      # проводим определенные операции с этой литерой
            word[self.cursor] = self.letter
            if self.direction == '>':
                self.cursor += 1
            elif self.direction == '<':
                self.cursor -= 1
            else:   # если self.direction == 'stop', останавливаем машину
                while True:     # чистим строку от лямбд
                    try:
                        word.pop(word.index('L'))   # удаляем L пока видим её
                    except ValueError:
                        break
                self.result_word = ''.join(word)   # выходим из машины, соединяем полученное на выходе слово в строку
                                                   # и возвращаем его
                return

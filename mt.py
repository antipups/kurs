class mt:
    tuple_alfabet = ('a', 'b', 'c')     # кортеж с литерами принадлежащим алфавиту
    number_of_state = 1     # номер состояния, 2, 3 и т.д, позже first_condition , second,
                            # тем самым меняя указатели на функции
    direction = '>'         # направление, в которое двигаемся , может быть >, <, stop
    letter = '1'            # буква, которую мы сейчас рассматриваем
    cursor = 1              # курсор , то что бегает по строке

    def first_condition(self):
        """
            Функция состояния, условие - что делаем с символом на котором стоит,
            пример :
                if self.letter == '1':       # если заданный символ один (функция получает символ)

                    self.number_of_state = second_condition            # в какое состояние переходим, 1 - функция называет first, 2 - second,
                                                                       # сколько состояний столько и методов состояний
                                                                       # если прописано, то изменяем если не прописано то остается как было

                    self.direction = '>'    # изменяем направление движения, если прописано то изменяем, если нет, то остается как и было
                    self.letter = '0'       # меняем букву, если прописано, то изменяем если не прописано то остается как было
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
        self.number_of_state = self.first_condition     # привязываем первое состояние к номеру состояния,
                                                        # или же на каком состоянии мы стартуем
        self.cursor = cursor    # с какой позиции стартовать, мт не всегда стартует с первой позиции
        """
            Сердце машины, то есть её работа, всё прописано тут, как она идет по состояниям, что возвращаем и т.д.
        """
        word = list(word)   # преобразуем слово
                            # из строчного вида в массив, где каждая литера отдельный элемент
                            # нужно для того, чтоб можно было редактировать элементы слова,
                            # так как строки в python константы, то эта операция необходима
        while True:     # бесконечный цикл, это и есть некая головка, которая будет ходить по литерам
            self.letter = word[self.cursor]      # получаем литеру на которой стоит головка
            self.number_of_state()      # проводим определенные операции с этой литерой
            word[self.cursor] = self.letter
            if self.direction == '>':
                self.cursor += 1
            elif self.direction == '<':
                self.cursor -= 1
            else:   # если self.direction == 'stop', останавливаем машину
                return ''.join(word[1:-1])      # выходим из машины, соединяем полученное на выходе слово в строку
                                                # и возвращаем его



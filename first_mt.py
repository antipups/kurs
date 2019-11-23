class mt:
    number_of_state = 1     # номер состояния, 2, 3 и т.д.
    direction = '>'         # направление, в которое двигаемся , может быть >, <, stop
    letter = '1'            # буква, которую мы сейчас рассматриваем
    cursor = 1              # курсор , то что бегает по строке

    def first_condition(self):   # первая операция
        """
        Функция состояния, условие - что делаем с символом на котором стоит,
        пример :
            if self.letter == '1':       # если заданный символ один (функция получает символ)

                self.number_of_state = 1            # в какое состояние переходим, 1 - функция называет first, 2 - second,
                                                    # сколько состояний столько и методов состояний
                                                    # если прописано, то изменяем если не прописано то остается как было

                self.direction = '>'    # изменяем направление движения, если прописано то изменяем, если нет, то остается как и было
                self.letter = '0'       # меняем букву, если прописано, то изменяем если не прописано то остается как было
        """
        if self.letter == '1':  # если буква - 1
            self.letter = '0'
        elif self.letter == '0':  # если буква - 0
            self.letter = '1'
        else:   # если достигнута лямбда, переходим в состояние два и возвращаем каретку наместо
            self.direction = '<'
            self.number_of_state = 2

    def second_condition(self):   # вторая операция
        if self.letter == 'L':  # если достигнута лямбда, переходим останавливаем машину
            self.direction = 'stop'

    def heart(self, word):   # машина тьюринга
        print('Изначальное слово - ' + word)
        word = list('L' + word + 'L')   # L - лямбда

        while True:
            self.letter = word[self.cursor]

            if self.number_of_state == 1:   # первое ссостояние
                self.first_condition()     # tmp - переменная бегунок, возвращаемая состоянием
            elif self.number_of_state == 2:     # второе состяние
                self.second_condition()
            word[self.cursor] = self.letter
            # print(word, tmp)
            if self.direction == '>':
                self.cursor += 1
            elif self.direction == '<':
                self.cursor -= 1
            else:   # если L
                break
        return ''.join(word[1:-1])


if __name__ == '__main__':
    print('Конечное слово - ' + mt().heart('101001'))

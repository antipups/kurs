from mt import mt


class mt_for_check_words_plus_ribbon(mt):
    """
        Машина тьюринга которая получает результаты второй(выдает первое слово) и третьей(выдает второе слово) мт,
        сравнивает эти слова, если они реверсивным выводит 1, если нет выводит 0.

        Как работает:
                Машина начинает свою работу с первой буквы слова, смотрит какая это буква,
            в зависимости от того какая это буква, переходит в состояние 2 3 или 4,
            после идет до края и исходя из состояния (2, 3 или 4), переходит в состояния
            5 6 или 7, соответсятвенно, далее, если буква соответствует состоянию, то есть
            5-ое состояние это состояние буквы а, если нашли букву а, затираем её, и отправляем в
            восьмое состояния, которое ведет каретку в начало и всё начинает заного.
            Если же буква не соответствует, к примеру ожидается a а стоит b, то состояние 5, 6 или 7
            переходит в состояние 9, затирает всю строчку и ставит 0, если же алгоритм доходит
            до конца удачно, то ставится 1.
    """

    def first_condition(self, multitape):
        """
            Смотрим какая буква, затираем, и отправляем в нужное состояние:
            a -> 2
            b -> 3
            c -> 4

            Если же, после сверки обоих слов, когда на ленте осталась
            ничего, то ставим 1 и останавливаем машину.
        """
        self.direction = '>'
        if self.letter == 'a':
            self.letter = 'L'
            self.state = self.second_condition
        elif self.letter == 'b':
            self.letter = 'L'
            self.state = self.third_condition
        elif self.letter == 'c':
            self.letter = 'L'
            self.state = self.fourth_condition
        elif self.letter == 'L':
            self.letter = '1'
            if multitape is True:
                self.second_ribbon = '1'
            self.direction = 'stop'

    def second_condition(self, multitape):
        """
            Двигаем до правого конца, после его достижения переходим в
            ПЯТОЕ состояние.
        """
        self.direction = '>'
        if self.letter == 'L':
            self.direction = '<'
            self.state = self.fifth_condition

    def third_condition(self, multitape):
        """
            Двигаем до правого конца, после его достижения переходим в
            ШЕСТОЕ состояние.
        """
        self.direction = '>'
        if self.letter == 'L':
            self.direction = '<'
            self.state = self.sixth_condition

    def fourth_condition(self, multitape):
        """
            Двигаем до правого конца, после его достижения переходим в
            СЕДЬМОЕ состояние.
        """
        self.direction = '>'
        if self.letter == 'L':
            self.direction = '<'
            self.state = self.seventh_condition

    def fifth_condition(self, multitape):
        """
            В этом состоянии сверяем букву, если это A то переходим в состояние восемь,
            иначе в состояние девять, если это лябда, ставим 0 и завершаем работу программы.
        """
        self.direction = '<'
        if self.letter == 'a':
            self.letter = 'L'
            self.state = self.eighth_condition
        elif self.letter in ('b', 'c'):
            self.letter = 'L'
            self.state = self.ninth_condition
        elif self.letter == 'L':
            self.letter = '0'
            if multitape is True:
                self.second_ribbon = '0'
            self.direction = 'stop'

    def sixth_condition(self, multitape):
        """
            В этом состоянии сверяем букву, если это В то переходим в состояние восемь,
            иначе в состояние девять, если это лябда, ставим 0 и завершаем работу программы.
        """
        self.direction = '<'
        if self.letter == 'b':
            self.letter = 'L'
            self.state = self.eighth_condition
        elif self.letter in ('a', 'c'):
            self.letter = 'L'
            self.state = self.ninth_condition
        elif self.letter == 'L':
            self.letter = '0'
            if multitape is True:
                self.second_ribbon = '0'
            self.direction = 'stop'

    def seventh_condition(self, multitape):
        """
            В этом состоянии сверяем букву, если это С то переходим в состояние восемь,
            иначе в состояние девять, если это лябда, ставим 0 и завершаем работу программы.
        """
        self.direction = '<'
        if self.letter == 'c':
            self.letter = 'L'
            self.state = self.eighth_condition
        elif self.letter in ('a', 'b'):
            self.letter = 'L'
            self.state = self.ninth_condition
        elif self.letter == 'L':
            self.letter = '0'
            if multitape is True:
                self.second_ribbon = '0'
            self.direction = 'stop'

    def eighth_condition(self, multitape):
        """
            Данное состояние возвращает головку к первой букве слова.
        """
        self.direction = '<'
        if self.letter == 'L':
            self.direction = '>'
            self.state = self.first_condition

    def ninth_condition(self, multitape):
        """
            Данное состояние затирает все буквы слева, и если в конце выводит 0.
        """
        self.direction = '<'
        if self.letter in self.tuple_alfabet:
            self.letter = 'L'
        elif self.letter == 'L':
            self.letter = '0'
            if multitape is True:
                self.second_ribbon = '0'
            self.direction = 'stop'


if __name__ == '__main__':
    pass

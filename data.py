mark = 1    # номер состояния, 2, 3 и т.д.

def first_operation(letter):    # первая операция
    global mark  # обращаемся к глоабльной переменной
    if letter == '1':   # если буква - 1
        mark = 2
        return '0'
    elif letter == '*':  # если буква - 2
        mark = 5
        return '*'




def mt(word):   # машина тьюринга
    while True:




if __name__ == '__main__':
    mt('111*11')

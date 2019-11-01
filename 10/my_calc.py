def calc():
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        zn = input('Введите оператор: ')
        if zn == '+':
            print(a+b)
        elif zn == '-':
            print(a-b)
        elif zn == ('*'):
            print(a*b)
        elif zn == ('/'):
            print(a/b)
    except ValueError:
        print('Вы ввели неккоретное значение')
    except ZeroDivisionError:
        print('Ошибка деления на ноль')
calc()


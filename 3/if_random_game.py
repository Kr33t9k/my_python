import random
a = random.randint(0, 4)
b = int(input('Введите число '))
if b == a:
    print('Победа')
else:
    print('Повторите еще раз')
    if  b < a:
        print('Ваше число меньше загаданного')
    else: 
        print('Ваше число больше загаданного')
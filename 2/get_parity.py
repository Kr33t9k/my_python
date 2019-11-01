a = int(input('Введите число\n'))
def chet(a):
    if a % 2 == 0:
        return 'Четное'
    else:
        return 'Нечетное'
print(chet(a))
import math
x = float(input('Введите вещественное число \n'))
def f(x):
    if 0.2 <= x <= 0.9:
        return math.sin(x)
    else:
        return(1)
print(f(x)) #x = 0.2: 1

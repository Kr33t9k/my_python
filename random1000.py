import random
a = [random.randint(-1000, 1000) for i in range(10)] #10 элементов просто легче проверить)
imin = a.index(min(a))
imax = a.index(max(a))
if imax < imin:
    imax, imin = imin, imax
kol = len(list(filter((lambda x: x < 0), a[imin:imax + 1])))
print(f'Список выглядит так: {a}, его максимальный элемент: {max(a)}, минимальный: {min(a)}, между ними {kol} отрицательных элементов')

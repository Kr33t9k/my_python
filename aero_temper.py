import numpy
with open('temper.stat', 'r') as file:
    lines = [float(x) for x in [line.strip() for line in file]]
print(f"Максимальное значение: {max(lines)}, Минимальное значение: {min(lines)},\nСредняя температура: {numpy.mean(lines)} Кол-во уникальных температур: {len(set(lines))}")
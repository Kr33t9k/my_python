a = '''Простой todo:
    1. Добавить задачу
    2. Вывести список задач.
    3. Выход
    '''
spisok = {'Задача': [], 'Категория': [], 'Время': []}
def one():
    task = input('Сформулируйте задачу: ')
    spisok['Задача'].append(task)
    cat = input('Добавьте категорию к задаче: ')
    spisok['Категория'].append(cat)
    time = input('Добавьте время к задаче: ')
    spisok['Время'].append(time)
def two():
    for i in range(len((spisok['Задача']))):
        print('Задача: ' + spisok['Задача'][i], end = ', ')
        print('Категория: ' + spisok['Категория'][i], end = ', ')
        print('Время: ' + spisok['Время'][i], end = '.\n')
deyst = {1: one, 2: two}
while True:
    print('\n' + a)
    c = int(input('Выберите действие '))
    if c == 3:
        break
    deyst[c]()
    print('dsadas')
    
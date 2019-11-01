text = '''Простой todo: 
    1. Добавить задачу.
    2. Вывести список задач.
    3. Выход.'''
tasks = []
def one():
    new_task = {'Задача:': input('Сформулируйте задачу: '), 'Категория:': input('Выберите категорию: '), 'Время:': input('Добавьте время: ')}
    tasks.append(new_task)
def two():
    for element in tasks:
        for key, value in element.items():
            print(key, value, end = ', ')
        print('\n')
do = {1: one, 2: two}
while True:
    print(text)
    b = int(input('\n' + 'Выберите действие: '))
    if b == 3:
        break
    do[b]()
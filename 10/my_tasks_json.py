import json
import os.path
text = '''Простой todo: 
    1. Добавить задачу.
    2. Вывести список задач.
    3. Выход.'''

filename = 'tasks.json'

def read(filename):
    with open(filename, 'r') as fread:
        global load 
        load = json.load(fread)

if os.path.isfile(filename):
    read(filename)
else:
    load = []

def one():
    new_task = {'Задача:': input('Сформулируйте задачу: '), 'Категория:': input('Выберите категорию: '), 'Время:': input('Добавьте время: ')}
    print('\n')
    load.append(new_task)

def two():
    if load:
        for element in load:
            for key, value in element.items():
                print(key, value, end = ', ')
            print('\n')
    else:
        print('Вы еще не добавили ни одной задачи.\n')

def three():
    with open(filename, 'w') as jz_file:
        json.dump(load, jz_file)
    print('Данные записаны в файл')

do = {1: one, 2: two, 3: three}

while True:
    try:
        print(text)
        b = int(input('\n' + 'Выберите действие: '))
        do[b]()
        if b == 3:
            break
    except Exception as e:
        print(f'Произошла ошибка: {e}')
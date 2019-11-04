import json
import os.path
text = '''Простой todo: 
    1. Добавить задачу.
    2. Вывести список задач.
    3. Выход.'''

filename = 'tasks.json'

new_tasks = []

def one2(): #Если json файл уже существует в директории
    new_task = {'Задача:': input('Сформулируйте задачу: '), 'Категория:': input('Выберите категорию: '), 'Время:': input('Добавьте время: ')}
    new_tasks.append(new_task)

def one1(): #Создание json файла и запись первой задачи в него. В конце даем указание использовать функцию выше
    tasks = []
    new_task = {'Задача:': input('Сформулируйте задачу: '), 'Категория:': input('Выберите категорию: '), 'Время:': input('Добавьте время: ')}
    tasks.append(new_task)
    with open(filename, 'w') as jz_file:
        json.dump(tasks, jz_file)
    do.update({1: one2})

def two():
    with open(filename, 'r') as jo_file:
        global load 
        load = json.load(jo_file) #Достать список задач из json файла
        if len(new_tasks) != 0: #Если есть новые задачи, добавить их в список выше
            load += new_tasks
        for element in load:
            for key, value in element.items():
                print(key, value, end = ', ')
            print('\n')

def three():
    with open(filename, 'w') as jz_file: #Запись новых задач при выходе, а не после каждого добавления
        json.dump(load, jz_file)
    print('Данные записаны в файл')

if os.path.isfile(filename): #Выбор первой функции в зависимости от наличия json файла в директории
    do = {1: one2, 2: two, 3: three}
else:
    do = {1: one1, 2: two, 3: three}

while True:
    try:
        print(text)
        b = int(input('\n' + 'Выберите действие: '))
        do[b]()
        if b == 3:
            break
    except FileNotFoundError:
        print('Вы еще не добавили ни одной задачи')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

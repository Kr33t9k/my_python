import csv
lst = [('Георгий', 'Невский проспект', '22'), ('Иван', 'пр. Ветеранов', '21')]
filename = input('Введите имя файла: ')
def csv_writer(filename, lst):
    try:
        with open(filename, 'w', newline = '') as file:
            header = [('name', 'adress', 'age')]
            write = csv.writer(file)
            write.writerows(header)
            for i in lst:
                write = csv.writer(file)
                write.writerows(lst)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
csv_writer(filename, lst)
import csv
file = input('Введите имя файла')
def csv_reader(file):
    people = []
    try:
        with open(file, 'r') as csv_file:
            read = csv.reader(csv_file) #открытие файла
            header = csv_file.readline().strip().split(',') #присвоение первой строчки файла header'у
            eline = dict.fromkeys(header) #сделать шаблонный словарь с ключами header и значениями None
            for line in read:
                for i in eline.keys():
                    eline[i] = line[list(eline.keys()).index(i)] #Изменить значения в шаблонном словаре на нужные
                people.append(eline) 
            return people
    except Exception as e:
        print(f'Возникла ошибка: {e}')
print(csv_reader(file))

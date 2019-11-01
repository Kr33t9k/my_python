def numt():
    o = 0
    while o == 0:
        try:
            a = open(input('введите названия исходного файла: ') + '.txt', 'r')
        except FileNotFoundError as nofile:
            print("Проверяем наличие файла в директории")
            print(nofile)
            Exception = True
            continue
        o = 1
    b = input('Введите название выходного файла: ') + '.txt'
    with open(b, 'w') as file2:
        i = 1        
        for stroka in a.read().split('\n'):
            file2.write(str(i) + ' ' + stroka + '\n')
            i += 1
    a.close()
numt()
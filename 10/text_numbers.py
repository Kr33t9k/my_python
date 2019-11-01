def numt():
    try:
        a = open(input('введите названия исходного файла: ') + '.txt', 'r')
        b = input('Введите название выходного файла: ') + '.txt'
        with open(b, 'w') as file2:
            i = 1        
            for stroka in a.read().split('\n'):
                file2.write(str(i) + ' ' + stroka + '\n')
                i += 1
        a.close()
        b.close()
    except FileNotFoundError as nofile:
        print("Проверяю наличие файла в директории")
        print(nofile)
numt()
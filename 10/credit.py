file = 'opendata.csv'
import csv
def nz(file):
    try:
        kredits = []
        reg_sum = {}
        with open(file, 'r', encoding = 'cp1251') as csv_file:
            read = csv.reader(csv_file)
            for row in read:
                if 'потребительские кредиты' in row[0] and row[2].startswith('2017') and row[1] != 'Россия':
                    reg_sum.setdefault(row[1], 0)
                    reg_sum[row[1]] += int(row[3]) 
            kredits.append(reg_sum)
            maxr = max(kredits[0].items(), key = lambda dict: dict[1])
            print(f'Регион с максимальным количеством заявок на потребительские кредиты: {maxr[0]} - {maxr[1]}')
    except Exception as e:
        print(e)
nz(file)
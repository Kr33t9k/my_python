a = input('Введите число: ')
s = 0
for i in a:
    if int(i) % 2 == 1:
        s += int(i) ** 2
print(s)     


'''
Дано число, введенное с клавиатуры. 
Определить сумму квадратов нечетных цифр в числе.
'''
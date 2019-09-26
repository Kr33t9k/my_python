names = ['John', 'Paul', 'George', 'Ringo']
for i in reversed(names):
    if i != 'John' and i != 'Paul':
        names.remove(i)
print(names)


'''Отфильтровать список имен так, чтобы в нем остался только элемент 'John' или 'Paul'.

names = ['John', 'Paul', 'George', 'Ringo']


В результате выполнения фильтрации список names будет содержать: 
['John', 'Paul']
'''

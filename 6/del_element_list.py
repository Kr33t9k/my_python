names = ['Rakhman', 'John', 'Paul', 'George', 'Ringo']
print(list(filter((lambda x: x == 'Paul' or x == 'John'), names)))


'''Отфильтровать список имен так, чтобы в нем остался только элемент 'John' или 'Paul'.

names = ['John', 'Paul', 'George', 'Ringo']


В результате выполнения фильтрации список names будет содержать: 
['John', 'Paul']
'''

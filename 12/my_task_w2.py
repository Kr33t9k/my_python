import json
import os.path
import tkinter

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
    new_task = {'Задача:': task_e.get(), 'Категория:': cat_e.get(), 'Время:': time_e.get()}
    load.append(new_task)
    task_e.delete(0, 'end')
    cat_e.delete(0, 'end')
    time_e.delete(0, 'end')

def two():
    if load:
        text.delete(1.0, 'end')
        for element in load:
            print(element.items())
            for key, value in element.items():
                text.insert('end', key + ' ' + value + '; ')
            text.insert('end', '\n\n')
    else:
        text.insert('end', 'Вы еще не добавили ни одной задачи.')

def three():
    with open(filename, 'w') as jz_file:
        json.dump(load, jz_file)
        window.destroy()

do = {1: one, 2: two, 3: three}

window = tkinter.Tk()
window.title('Менеджер задач')

task_l = tkinter.Label(window, text = 'Задача:')
task_l.grid(row = 0, column = 0, sticky = 'N', padx=15, pady = 5)

task_e = tkinter.Entry(window)
task_e.grid(row = 0, column = 1, sticky = 'N', padx=15, pady = 5)

cat_l = tkinter.Label(window, text = 'Категория:')
cat_l.grid(row = 1, column = 0, sticky = 'N', padx=20, pady = 5)

cat_e = tkinter.Entry(window)
cat_e.grid(row = 1, column = 1, sticky = 'N', padx=20, pady = 5)

time_l = tkinter.Label(window, text = 'Время:')
time_l.grid(row = 2, column = 0, sticky = 'N', padx=20, pady = 5)

time_e = tkinter.Entry(window)
time_e.grid(row = 2, column = 1, sticky = 'N', padx=20, pady = 5)

text = tkinter.Text(width=80, height = 20)
text.grid(row = 0, column = 3, rowspan = 50, columnspan = 5, padx=20, pady = 10)

write_button = tkinter.Button(window, text = 'Добавить задачу', background = 'yellow', command = do[1])
write_button.grid(row = 3, column = 1)

list_button = tkinter.Button(window, text = 'Список задач', background = 'yellow', command = do[2])
list_button.grid(row = 4, column = 1)

exit_button = tkinter.Button(window, text = 'Выход', background = 'yellow', command = do[3])
exit_button.grid(row = 5, column = 1)

window.mainloop()
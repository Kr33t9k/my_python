import tkinter
import random
animals = {'dog': 'Собака', 'cat': 'Кошка', 'pig': 'Свинья'}
window = tkinter.Tk()
label = tkinter.Label(window, text = 'Случайное слово: ').pack()
slovo = tkinter.StringVar()
slovo.set(random.choice(list(animals.keys())))
label = tkinter.Label(window, text = slovo.get()).pack()
label = tkinter.Label(window, text = 'Укажите перевод слова ниже:').pack()
entry = tkinter.Entry(window)
entry.pack()
label = tkinter.Label(window)
label.pack()
def click():
    entry_slovo = tkinter.StringVar() 
    entry_slovo = entry.get().title()
    if entry_slovo == animals[slovo.get()]:
        label.config(text = 'Вы угадали.')
    else:
        label.config(text = 'Вы не угадали.')
button = tkinter.Button(window, text = 'Проверить.', command = click)
button.pack()
exitt = tkinter.Button(window, text = 'Выход.', command = window.destroy)
exitt.pack()
window.mainloop()
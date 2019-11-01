import string
with open('moby.txt', 'r') as file:
    with open('moby_clean.txt', 'w') as file1:
        text = file.read()
        trantab = str.maketrans('', '', string.punctuation)
        text = text.translate(trantab).lower()
        for word in text.split(' '):
            if word != '': #Почему-то вместо точек появлялась пустая строка
                file1.write(str(word) + '\n')
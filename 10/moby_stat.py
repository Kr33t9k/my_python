def hyst(text):
    word_count = {}
    for word in text:
        word_count.setdefault(word, 0)
        word_count[word] += 1
    return word_count

with open('moby_clean.txt', 'r') as file:
    dict = hyst(file.read().split())
    dict = sorted(dict.items(), key = lambda dict: dict[1])
    max_count = dict[len(dict) - 5::]
    min_count = dict[0:5]

print('Чаще всего в этом тексте встречаются слова: ')
for i in max_count:
    print(f'{i[0]}: {i[1]} раз(а),', end = ' ')

print('\nРеже всего в этом тексте встречаются слова: ')
for i in min_count:
    print(f'{i[0]}: {i[1]} раз(а),', end = ' ')
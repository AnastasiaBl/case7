import random

with open('text.txt', 'r', encoding='ISO-8859-1') as f_in:
    text = f_in.read()
sym = "+-:;=@#$%^&*()~№<>{}[]"

for i in sym:
    if i in text:
        text = text.replace(i, '')

spaces = [' .', ' ,', ' !', ' ?', '  ']
for i in range(len(spaces)):
    if spaces[i] in text:
        sign = spaces[i]
        text = text.replace(sign, sign[1])

if '\n' in text:
    text = text.replace('\n', ' ')

words = text.split()
start = []
capital = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
for i in range(len(words)):
    word = words[i]
    for char in capital:
        if char in word:
            start.append(word)

dict_1 = {}
for j in words:
    lenght = len(j)
    for i in start:
        if i in j:
            list_of_words = []
            for k in range(1, lenght):
                list_of_words.append(j[k])
            dict_1.update({i: list_of_words})

g = len(start)
e = random.randint(0, g)
print(start[e], end='')
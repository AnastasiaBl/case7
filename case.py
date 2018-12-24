import random

with open('text.txt') as f_in:
    text = f_in.read()
sym = "+-:;=@#$%^&*()~№<>{}[]"

for i in sym:
    if i in text:
        text = text.replace(i, '')

spaces = [' .', ' ,', ' !', ' ?', '  ']
for i in range (len(spaces)):
    if spaces[i] in text:
        sign=spaces[i]
        text = text.replace(sign, sign[1])

if '\n' in text:
    text = text.replace('\n', ' ')

words = text.split()
start = []
capital = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
for i in range (len(words)):
    word = words[i]
    for char in capital:
        if char in word:
            start.append(word)
print(start)
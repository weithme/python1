# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?

import re
txt = 'Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту'

# a
words = re.split(r'\W+', txt)
set1 = set(words)
for i in set1:
    print(f'{i}: {words.count(i)}')

# b
letters = re.findall(r"[A-Za-z]", txt, flags=re.IGNORECASE)
set2 = set(letters)
for i in set2:
    print(f'{i}: {letters.count(i)}')
    
    
# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра

txt1 = 'Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах.'
txt2 = 'найти Все слова. Без учета регистра'

txt1 = txt1.lower()
txt2 = txt2.lower()

words1 = re.split(r'\W+', txt1)
words2 = re.split(r'\W+', txt2)

set1 = set(words1)
set2 = set(words2)

result = set1.intersection(set2)
print(result)
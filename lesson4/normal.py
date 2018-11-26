# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
# import random

import random
with open('qwerty.txt', 'w') as f:
    cnt = 2500
    for i in range(0,cnt):
        f.write(str(random.randint(0,9)))
        
with open('qwerty.txt', 'r') as f:
    s = f.read() 
    max_str = [1, s[0]] # кол-во элементов, элемент
    cnt = len(s)
    m = 1    
    for i in range(1,cnt):
        if i!=cnt-1 and s[i+1]==s[i]:
            m += 1
        else:
            if m>max_str[0]:
                max_str[0] = m
                max_str[1] = s[i]
            m=1
    length = max_str[0]
    index = s.index(max_str[1]*length)
    if index==0:
        print(f'{s[:index+length]} <---- {s[index+length:]}')
    elif index+length<cnt:
        print(f'{s[:index]} ----> {s[index:index+length]} <---- {s[index+length:]}')
    else:
        print(f'{s[:index]} ----> {s[index:]}')
    print(f'\n{s[index:index+length]}')


# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте, остальные элементы тоже рандомные. Пользователь вводит размер

import random
import pprint
n = int(input('Укажите размер матрицы: '))
mtr = [[random.randint(1, max) for i in range(n)] for j in range(n)]
mtr[random.randrange(n)][random.randrange(n)] = 0
pprint.pprint(mtr)

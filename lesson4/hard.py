# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли хотя бы один просвет по каждому из трех измерений? 
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.

import random
from pprint import pprint
# 0 - прозрачный, 1 - нет
n = 3
cube = [[[random.randrange(2) for x in range(n)] for y in range(n)] for z in range(n)] 
pprint(cube)

for i in range(n):
    for j in range(n):
        if sum(cube[i][j]) == 0:
            print(f'x:{i}, y:{j}')
        if sum(cube[i][:][j]) == 0:
            print(f'x:{i}, z:{j}')
        if sum(cube[:][i][j]) == 0:
            print(f'y:{i}, z:{j}')

            
# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.
#
#

from pprint import pprint
m = 10
dct = {}
with open('pwd.txt', 'r') as f:
    for line in f:
        arr = line.split(';')
        if len(arr) == 2:
            pwd = arr[1].strip()
        else:
            continue
            
        if pwd in dct.keys():
            dct[pwd] += 1
        else: 
            dct[pwd] = 1
        
sort_val = sorted(dct.values())

result = [[k,dct[k]] for k in dct if dct[k] in sort_val[-1:]]

i=0
while len(result) < m:
    res = [[k,dct[k]] for k in dct if dct[k] in sort_val[-1-i:-i] ] 
    result += res
    i+=1

pprint(result)


# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами

# 5
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 3
# 1 2 3 
# 8 9 4
# 7 6 5

#n = 7 # число столбцов
n = int(input('Введите число: '))
N = n**2
dct = {}
layers = (n+1)//2 # число слоев
k=n%2 #0

if k == 0:
    dct = {-1:[N-3,N-2],
           0:[N, N-1]} 
    N-=4
else:    
    dct[0] = [N]
        
for layer in range(1,layers):
    for i in range(-layer+k,layer):
        dct[i] = [N-(i+layer)] + dct[i] + [N - 3*2*layer + (i+layer-1+k)]
    dct[-layer-1+k] = [N-4*(2*layer+1-k) + 1 - k + i for i in range(0, 2*(layer+1)-k)] # top
    dct[layer]  = [N-2*layer - i for i in range(0, 2*(layer+1)-k)] # bottom
    N -= 4*(2*layer+1-k)
        
L = len(str(n**2)) + 1 # число символов +1 в числе в самом центре

for line in sorted(dct.keys()):
    for i in dct[line]:
        print(f'{i}', end = ' '*(L-len(str(i))))
    print()

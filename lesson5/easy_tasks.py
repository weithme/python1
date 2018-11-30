# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

# создаем папки
for i in range(1, 10):
    dirname = 'dir_{}'.format(i)
    try:
        os.mkdir(dirname)
    except Exception as e:
        print(e)

# удаляем папки
for i in range(1, 10):
    dirname = 'dir_{}'.format(i)
    try:
        os.rmdir(dirname)
    except Exception as e:
        print(e)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

dirs = [x for x in os.listdir() if os.path.isdir(x)]
for name in dirs:
    print(name)

    
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os, sys, shutil

fpath_original = sys.argv[0]
f = os.path.splitext(fpath_original)
fpath_copy = '{}_copy{}'.format(f[0], f[1])

shutil.copy(fpath_original, fpath_copy)

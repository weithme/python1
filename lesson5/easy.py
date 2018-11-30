# функции для задания Normal
# 1. Перейти в папку
# 2. Просмотреть указанной папки
# 3. Удалить папку
# 4. Создать папку

import os

def createDir(path):
    dirname = input('Укажите имя новой директории: ')
    try:
        result = os.path.join(path, dirname)
        os.mkdir(result)
        print(result)
    except Exception as e:
        print(e)

def removeDir(path):
    dirname = input('Укажите имя директории для удаления: ')
    try:
        result = os.path.join(path, dirname)
        os.rmdir(dirname)
        print(result)
    except Exception as e:
            print(e)

def showDirs(path):
    print(os.listdir(path))
    dirs = [x for x in os.listdir(path) if os.path.isdir(x)]
    #for name in dirs:
    #    print(name)
    print(path)

def changeDir(path):
    try:
        dirname = input('Укажите имя директории: ')
        result = os.path.join(path, dirname)
        print(result)
        return result
    except Exception as e:
            print(e)

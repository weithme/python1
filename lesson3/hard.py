# HARD

#Задание-1

#Написать консольное меню вида:

#1. Добавить
#2. Удалить
#3. Распечатать
#4. Посчитать
#5. Выйти

#Надо чтобы
#а) Можно было удобно менять порядок меню и\или добавлять\удалять пункты меню
#б) Каждое действие (добавить, удалить и тд) должно быть функцией
#в) У пользователя надо спросить номер команды
#г) Программа не должна завершаться пока не введется команда Выйти
#д) Проверять на ввод ошибочных данных, там где они могут появиться

def addItem(lst):
    newitem = input('Укажите имя нового пункта меню ')
    lst.append(newitem)
    print(f'Добавлен пункт меню "{len(lst)}. {newitem}"')
    return

def removeItem(lst, main_cnt):
    n = input(f'Укажите номер пункта меню для удаления (номера 1-{main_cnt} не удаляются) ')
    if n.isdigit():
        n = int(n)-1
        if n>=main_cnt and n<len(lst):
            delitem = lst.pop(n)
            print(f'Удален пункт меню "{n+1}. {delitem}"')
            return True
        else: 
            print(f'Пункт меню не удален')
            return False
    else: 
        print(f'Пункт меню не удален')
        return False    

def switchItems(lst, main_cnt):
    txt = input(f'Укажите через пробел два номера пунктов меню для перемешения (номера 1-{main_cnt} не перемещаются) ')
    txt_arr = txt.split()
    if len(txt_arr)>1: 
        n=txt_arr[0]
        m=txt_arr[1]
        if n.isdigit() and m.isdigit() and m!=n:
            n = int(n)-1
            m = int(m)-1
            if n>=main_cnt and n<len(lst) and m>=main_cnt and m<len(lst):
                tmp = lst[m]
                lst[m] = lst[n]
                lst[n] = tmp
                print(f'Перемещены пункты меню "{n}. {lst[m]}" и "{m}. {lst[n]}"')
                return
            else: 
                print(f'Пункты меню "{n}. {nItem}" и "{m}. {mItem}" не перемещены')
                return 
        else: 
            print(f'Неправильно указаны пункты меню "{txt}"')
            return False
    else:
        print(f'Неправильно указаны пункты меню "{txt}"')
        return

    

    
def askCommand(lst):
    return input(f'>>Выберите пункт меню (введите номер 1-{len(lst)}) ')
   
    
def calculate(lst):
    return len(lst)


def getItem(select, lst):
    return lst[select-1]  

    
def showMenuLst(lst):
    print('\n---Меню---')
    for i in enumerate(lst):
        print(f'{i[0]+1}. {i[1]}')
    print('----------')
        
lst = ['Добавить', 'Удалить', 'Переместить', 'Распечатать', 'Посчитать', 'Выйти']
main_cnt = len(lst)
select = ''
item = ''

showMenuLst(lst)

while item != 'Выйти':    
    select = ''
    item = ''
    while not select in range(0,len(lst)+1):
        select = ''
        while not select.isdigit():
            select=askCommand(lst)
        select = int(select)
    item = getItem(select,lst)      
    
    print(f'Выбран пункт меню "{select}. {item}"')    
    
    if item == 'Добавить':
        addItem(lst)
        
    elif item == 'Удалить':
        removeItem(lst,main_cnt)
        
    elif item == 'Распечатать':
        showMenuLst(lst)
        
    elif item == 'Посчитать':
        print(f'Пунктов в меню: {calculate(lst)} шт')
        
    elif item == 'Переместить':
        switchItems(lst,main_cnt)

print('Программа завершена')
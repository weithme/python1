# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    arr = str(number).split('.')
    first_str = arr[0]
    end_str = arr[1]
    fl = 0
    if len(end_str) >= ndigits:
        end_str = end_str[:ndigits+1]
        if int(end_str[ndigits]) >= 5:
            fl = 1
    end_int = int(end_str[:-1]) + fl
    first_int = int(first_str) + end_int//(10**ndigits)
    end_int = end_int%(10**ndigits)
    return float(f'{first_int}.{end_int}')

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    sum1=sum2=0
    for i in enumerate(str(ticket_number)):
        if i[0]<3: sum1 += int(i[1])
        else: sum2 += int(i[1])
    if sum1==sum2:
        return 'happy'
    else:
        return 'unhappy'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
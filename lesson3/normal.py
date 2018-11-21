# NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    f = []
    f.append(1)
    f.append(1)
    for i in range(2,m+1):
        f.append(f[i-1] + f[i-2])
    return f[n-1:m]

print(fibonacci(1,6))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(0,len(origin_list)-1):
        for j in range(i,len(origin_list)):
            if origin_list[i] > origin_list[j]:
                tmp = origin_list[i]
                origin_list[i] = origin_list[j]
                origin_list[j] = tmp
    return origin_list

s = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(s)
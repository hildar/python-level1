# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    lst = [1, 1]

    i = 2
    while i <= m:
        lst.append(lst[i - 1] + lst[i - 2])
        i += 1

    return lst[n:]


print(fibonacci(6, 11))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    j = 0
    while j < len(origin_list) - 1:
        i = 0
        while i + j < len(origin_list) - 1:
            if origin_list[i] > origin_list[i + 1]:
                # swap
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
            i += 1
        j += 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

ages = [5, 18, 17, 19, 14, 32]


# функция ключ для фильтрации
def my_func(x):
    if x < 18:
        return False
    else:
        return True


# фильтрация
def my_filter(func, lst):
    i = 0
    while i < len(lst):
        if func(lst[i]):
            pass
            print("F true")
        else:
            lst.pop(i)
            i -= 1
            print("F false")
        i += 1
    return lst


print(my_filter(my_func, ages))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


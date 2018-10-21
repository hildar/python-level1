# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

lst = [random.randint(-10, 10) for _ in range(10)]
lst_quadro = [el ** 2 for el in lst]

print("lst =", lst)
print("lst_quadro =", lst_quadro)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

lst2 = ['apple', 'orange', 'watermelon']
lst3 = ['dog-rose', 'banana', 'grapes']

lst_fruits = [el for el in lst2 + lst3]
print("lst_fruits =", lst_fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lst5 = [random.randint(-12,30) for _ in range(50)]
lst5.append(12)

lst_if = [el for el in lst5 if el % 3 == 0 and el >= 0 and el % 4 != 0]

print("lst5 =", lst5)
print("lst_if = ", lst_if)


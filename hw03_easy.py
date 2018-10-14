# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    lst = str(number).split(".")
    num_l = list(lst[1][:ndigits + 1])

    # сдвиг
    if int(num_l[ndigits]) >= 5 and int(num_l[ndigits - 1]) == 9 and ndigits != 0:
        while ndigits > 0:
            if int(num_l[ndigits - 1]) == 9 and ndigits != 1:
                ndigits -= 1
            elif int(num_l[ndigits - 1]) == 9 and ndigits == 1:
                ndigits -= 1
                lst[0] = str(int(lst[0]) + 1)  # итерация целого числа
            else:
                break
        num_l = list(lst[1][:ndigits + 1])  # срез лишнего
    elif int(num_l[ndigits]) >= 5 and ndigits == 0:
        lst[0] = str(int(lst[0]) + 1)  # итерация целого числа

    # вычисление
    if int(num_l[ndigits]) >= 5:
        num_l[ndigits - 1] = str(int(num_l[ndigits - 1]) + 1)
        num_l.pop()
    else:
        num_l.pop()

    lst[1] = ''.join(num_l)
    return float('.'.join(lst))


# проверка
i = 0
while i < 5:
    print("b =", i)
    print(my_round(2.9123456, i) == round(2.9123456, i))
    print(my_round(2.1999857, i) == round(2.1999857, i))
    print(my_round(2.9999967, i) == round(2.9999967, i))
    print(my_round(2.8999967, i) == round(2.8999967, i))
    print(my_round(2.0000102, i) == round(2.0000102, i))
    i += 1
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

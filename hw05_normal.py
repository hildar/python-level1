# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import hw05_easy as easy

while True:
    try:
        key = input('[1] - Перейти в папку\n'
                    '[2] - Просмотреть содержимое текущей папки\n'
                    '[3] - Удалить папку\n'
                    '[4] - Создать папку\n'
                    '[q] - Выход\n'
                    '-->> ')
    except Exception as cls:
        print('Ошибка ввода:', cls)

    if key == '1':
        print('Список текущих папок:', easy.cur_dirs())
        try:
            choose_dir = input('Выберите папку для перехода,\n'
                               'или "b" для перехода на уровень вверх\n'
                               '-->> ')
        except Exception as cls:
            print('Ошибка ввода:', cls)
        if choose_dir == 'b':
            try:
                choose_dir = os.getcwd()[:os.getcwd().rfind('\\')]
            except Exception as cls:
                print('Ошибка перехода:', cls)
        if os.path.isdir(choose_dir):
            os.chdir(choose_dir)
            print('Успешный переход в папку <<{}>>'.format(choose_dir))

    elif key == '2':
        print('Содержимое текущей папки:', os.listdir(), '\n')

    elif key == '3':
        print('Список текущих папок:', easy.cur_dirs())
        try:
            choose_dir = input('Выберите папку для удаления,\n'
                               '-->> ')
        except Exception as cls:
            print('Ошибка ввода:', cls)
        if os.path.isdir(choose_dir):
            easy.del_dir(choose_dir)

    elif key == '4':
        print('Список текущих папок:', easy.cur_dirs())
        try:
            new_dir = input('Введите название новой папки,\n'
                            '-->> ')
        except Exception as cls:
            print('Ошибка ввода:', cls)
        easy.make_dir(new_dir)

    elif key == 'q':
        sys.exit()

    else:
        print('Неизвестный выбор')

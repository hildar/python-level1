# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil


# Создаем папку
def make_dir(name_dir=''):
    try:
        os.mkdir(os.path.join(os.getcwd(), name_dir))
        print('Папка <<{}>> успешно создана'.format(name_dir))
        return True
    except FileExistsError:
        print('Такая папка уже существует')
        return False
    except Exception as cls:
        print('Ошибка создания папки:', cls)
        return False


# Удаляем папку
def del_dir(name_dir=''):
    try:
        os.rmdir(os.path.join(os.getcwd(), name_dir))
        print('Папка <<{}>> успешно удалена'.format(name_dir))
        return True
    except Exception as cls:
        print('Ошибка удаления:', cls)
        return False

# Запускаемый скрипт в конце файла


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def cur_dirs():
    list_dirs = []
    result_list_dirs = []

    # Вытаскиваем имена папок через функцию os.walk
    for root, dirs, files in os.walk("."):
        for name in dirs:
            list_dirs.append(dirs)

    # Убираем всё лишнее, оставляя только папки
    if list_dirs != []:
        result_list_dirs = list_dirs[0]

    return result_list_dirs


# Если это главный файл, то получаем список папок
if __name__ == '__main__':
    current_dirs = cur_dirs()
    print('Список папок - {}'.format(current_dirs))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


# Функция копирования файла
def duplicate_file(filename):
    # Необходимо выполнить проверку isfile,
    # т.к. при попытке копирования директории будет возникать ошибка
    if os.path.isfile(filename):
        newfile2 = filename + '.dupl'
        shutil.copy(filename, newfile2)			# копируй
        if os.path.exists(newfile2):
            print("Файл {} был успешно создан".format(newfile2))
            return True
        else:
            print("Возникли проблемы копирования")
            return False


# Функция удаления файла
def remove_file(filename):
    # Необходимо выполнить проверку exist, т.к. при попытке
    # удаления не существующего файла будет возникать ошибка
    if os.path.exists(filename):
        if os.path.isfile(filename):
            os.remove(filename)
            print("Файл <<{}>> успешно удален".format(filename))
            return True
        else:
            print('Отказано в доступе. Можно удалять только файлы')
            return False
    else:
        print("Файла с именем <<{}>> не существует".format(filename))
        return False


# Получаем имя текущего файла
cur_name = sys.argv[0][sys.argv[0].rfind('/') + 1:]


# Вызов главного скрипта для создания и удаления папок
# Функция будет вызвана только если это главный исполняемый файл
if __name__ == '__main__':
    key = ''
    try:
        while key != 'q':
            key = input("[1] - создать папки,\n"
                        "[2] - удалить папки,\n"
                        "[3] - дубликат исполняемого файла"
                        "[q] - выйти\n"
                        "-->> ")
            list_dir = ['dir_' + str(el) for el in range(1, 10)]

            if key == '1':
                for el in list_dir:
                    make_dir(el)

            elif key == '2':
                for el in list_dir:
                    del_dir(el)

            elif key == '3':
                duplicate_file(cur_name)
    except Exception as cls:
        print('Ошибка:', cls)

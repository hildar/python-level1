# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

list_dir = ['dir_' + str(el) for el in range(1, 10)]


# Создаем кучу папок
def make_bunch():
    try:
        for el in list_dir:
            os.mkdir(os.path.join(os.getcwd(), el))
    except FileExistsError:
        print('Такая папка уже существует')

    return print('Папки {} - {} созданы'.format(list_dir[0], list_dir[len(list_dir) - 1]))


# Удаляем сщзданную кучу папок
def del_bunch():
    try:
        for el in list_dir:
            os.rmdir(os.path.join(os.getcwd(), el))
    except Exception as cls:
        print('Exeption class =', cls)

    return print('Папки {} - {} удалены'.format(list_dir[0], list_dir[len(list_dir) - 1]))


# Вызов функций для сздания и удаления папок
key = ''
try:
    while key != 'q':
        key = input("Haжмите 1 чтобы создать папки, 2 чтобы удалить и 'q' чтобы выйти\n")
        if key == '1':
            make_bunch()
        elif key == '2':
            del_bunch()
except Exception as cls:
    print('Exeption class =', cls)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def cur_dirs():
    list_dirs = []

    # Вытаскиваем имена папок через функцию os.walk
    for root, dirs, files in os.walk("."):
        for name in dirs:
            list_dirs.append(dirs)

    # Убираем всё лишнее, оставляя только папки
    result_list_dirs = list_dirs[0]
    print(result_list_dirs)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

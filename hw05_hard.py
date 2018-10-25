# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import hw05_easy as easy
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создание копии указанного файла")
    print("rm <file_name> - удаляние указанного файла (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - замена текущей директории на указанную")
    print("ls - отображение полного пути текущей директории")
    print("af - отображение всех файлов в текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    easy.duplicate_file(file_name)


def remove_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    while True:
        try:
            case = input('Вы уверены что хотите удалить данный файл?\n'
                         'y/n -->> ')
        except Exception as cls:
            print('Ошибка ввода:', cls)
        if case == 'y':
            easy.remove_file(file_name)
            sys.exit()
        elif case == 'n':
            print('Отмена удаления')
            sys.exit()
        else:
            print('Неверный выбор')


def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        if os.path.isdir(dir_path):
            os.chdir(dir_path)
            print('Успешный переход по пути:\n'
                  '{}'.format(dir_path))
        else:
            print('Указан неверный путь')
    except Exception as cls:
        print('Ошибка перехода:', cls)


def local_dir():
    print("Полный путь текущей директории:\n", os.getcwd())


def list_dir():
    print("Все файлы в текущей директории:\n", os.listdir())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": local_dir,
    "af": list_dir
}

try:
    dir_name = sys.argv[2]
    file_name = sys.argv[2]
    # Если передано больше двух аргументов, значит либо путь к папке с пробелами,
    # либо имя файла с пробелами
    if sys.argv[3]:
        dir_name = ' '.join(sys.argv[2:len(sys.argv)])
        file_name = ' '.join(sys.argv[2:len(sys.argv)])
except IndexError:
    dir_name = None
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
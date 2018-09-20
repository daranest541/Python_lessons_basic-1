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
import shutil
import os
import sys
import re
if __name__ == '__main__' and len(sys.argv) > 1:
    #print('sys.argv = ', sys.argv)
    def print_help():
        print("help - получение справки")
        print("mkdir <dir_name> - создание директории")
        print("ping - тестовый ключ")
        print("cp <file_name> - создает копию указанного файла")
        print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
        print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
        print("ls - отображение полного пути текущей директории")



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
        if not dir_name:
            print("Необходимо указать имя файла вторым параметром")
            return
        try:
            normal_path = os.path.normpath(dir_name)
            if not os.path.exists(normal_path):
                print("Указаный файл {} не найден.".format(os.path.abspath(normal_path)))
                return
            normal_path = os.path.normpath(dir_name)
            filename, file_extension = os.path.splitext(normal_path)
            copy = '{}_copy{}'.format(filename, file_extension)
            if os.path.exists(copy):
                i = 0
                print('копия файла уже существует {}'.format(copy))
                print(os.path.exists(copy))
                while os.path.exists(copy):
                    i += 1
                    copy = '{}_copy{}{}'.format(filename, i, file_extension)
                    print('зашли в цикл {}'.format(copy))

            print(copy)
            shutil.copyfile(dir_name, copy)
        except OSError as e:
            print(e)
            return

    def clear_directory(normal_path):
        try:
            for root, dirs, files in os.walk(normal_path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            return True
        except OSError as e:
            print(e)
            return False

    def remove_file():
        if not dir_name:
            print("Необходимо указать имя файла вторым параметром")
            return
        try:
            normal_path = os.path.normpath(dir_name)
            if not os.path.exists(normal_path):
                print("Указаный файл {} не найден.".format(os.path.abspath(normal_path)))
                return
            type_delete = "файл"
            if os.path.isdir(normal_path):
                type_delete = "директорию со всеми вложенными папками и файлами"

            sure = ""
            while sure != "n" and sure != "y":
                sure = input("Вы уверены что хотите удалить {} {} (y/n): ".format(type_delete, dir_name))

            if sure == "y":
                if os.path.isdir(normal_path):
                    if clear_directory(normal_path):
                        os.rmdir(normal_path)
                        print("Директория {} удалена.".format(os.path.abspath(normal_path)))
                    else:
                        print("Ошибка удаления директории")
                        return

                else:
                    os.remove(normal_path)
                    print("Файл {} удален.".format(os.path.abspath(normal_path)))
            else:
                print("Вы не уверены)")
                return

        except OSError as e:
            print(e)
            return

    def change_directory():
        if not dir_name:
            print("Необходимо указать имя директории вторым параметром")
            return
        try:
            normal_path = os.path.normpath(dir_name)
            if not os.path.exists(normal_path):
                print("Указаная директория {} не найдена.".format(os.path.abspath(normal_path)))
                return
            if not os.path.isdir(normal_path):
                print("Указаный путь {} не является директорией.".format(os.path.abspath(normal_path)))
                return
            os.chdir(normal_path)
            print('Вы перешли в директорию ' + os.getcwd())
        except OSError as e:
            print(e)
            return

    def get_abs_current_path():
        try:
            print('Вы находитесь в дериктории ' + os.getcwd())
        except OSError as e:
            print(e)
            return

    do = {
        "help": print_help,
        "mkdir": make_dir,
        "ping": ping,
        "cp": copy_file,
        "rm": remove_file,
        "cd": change_directory,
        "ls": get_abs_current_path
    }

    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None

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
else:
    print('Скрипт запущен без аргументов или импортирован как библиотека')
